# # server.py
# from flask import Flask, request, abort
# from zendesk_first_responder_crew.crew import ZendeskFirstResponderCrew  # your Crew class

# app = Flask(__name__)

# @app.route('/webhook', methods=['POST'])
# def zendesk_webhook():
#     # 1) Grab the JSON body
#     payload = request.get_json(silent=True)
#     if not payload:
#         # Tell Zendesk it was a bad request so it won’t retry forever
#         return abort(400, "Invalid JSON")

#     # 2) (Optional) log it so you can inspect the shape
#     app.logger.info("Received Zendesk payload:\n%s", payload)

#     # 3) Fire off your Crew
#     try:
#         ZendeskFirstResponderCrew().crew().kickoff(inputs=payload)
#     except Exception as e:
#         app.logger.error("Crew kickoff error: %s", e)

#     # 4) Ack immediately
#     return "", 200

# if __name__ == '__main__':
#     # Make sure PORT matches your ngrok/localtunnel
#     app.run(host="0.0.0.0", port=3000, debug=True)
"""---------------------"""
# server.py
# from flask import Flask, request, abort
# import threading
# from zendesk_first_responder_crew.crew import ZendeskFirstResponderCrew

# app = Flask(__name__)

# def _run_crew(payload):
#     try:
#         ZendeskFirstResponderCrew().crew().kickoff(inputs=payload)
#     except Exception as e:
#         app.logger.error("Crew kickoff error: %s", e)

# @app.route('/webhook', methods=['POST'])
# def zendesk_webhook():
#     # 1) Parse JSON (force=True will abort with 400 on invalid JSON)
#     payload = request.get_json(force=True)

#     # 2) ACK Zendesk immediately
#     #    (even if payload is empty dict[], you still return 200)
#     threading.Thread(target=_run_crew, args=(payload,), daemon=True).start()
#     return "", 200

# if __name__ == '__main__':
#     # debug=False in prod so you don’t leak the debugger
#     app.run(host="0.0.0.0", port=3000, debug=True)


'''-----------------------------------'''

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

