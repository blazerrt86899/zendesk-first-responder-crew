# server.py
from flask import Flask, request, abort
import threading
import os
import requests
from zendesk_first_responder_crew.crew import ZendeskFirstResponderCrew

app = Flask(__name__)

def post_internal_note(ticket_id: str, response_file: str = "final_response.md"):
    """
    Reads the AI-generated response from the specified markdown file and posts it
    as an internal note to the given Zendesk ticket.
    """
    subdomain = os.getenv("ZENDESK_SUBDOMAIN")
    zendesk_user = os.getenv("ZENDESK_EMAIL")
    zendesk_token = os.getenv("ZENDESK_API_TOKEN")
    with open(response_file, "r") as f:
        note_body = f.read()
    url = f"https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_id}.json"
    auth = (f"{zendesk_user}/token", zendesk_token)
    payload = {
        "ticket": {
            "comment": {
                "body": note_body,
                "public": False
            }
        }
    }
    response = requests.put(url, auth=auth, json=payload)
    response.raise_for_status()
    print(f"✅ Internal note added to ticket {ticket_id}")

def _run_crew(payload):
    try:
        ZendeskFirstResponderCrew().crew().kickoff(inputs=payload)
        ticket_id = payload.get("ticket_id")
        if ticket_id:
            post_internal_note(ticket_id)
        else:
            app.logger.error("No ticket_id found in payload!")
    except Exception as e:
        app.logger.error("Crew kickoff or Zendesk note error: %s", e)

@app.route('/webhook', methods=['POST'])
def zendesk_webhook():
    payload = request.get_json(force=True)
    threading.Thread(target=_run_crew, args=(payload,), daemon=True).start()
    return "", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)

