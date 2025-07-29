# server.py
from flask import Flask, request, abort
from zendesk_first_responder_crew.crew import ZendeskFirstResponderCrew  # your Crew class

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def zendesk_webhook():
    # 1) Grab the JSON body
    payload = request.get_json(silent=True)
    if not payload:
        # Tell Zendesk it was a bad request so it won’t retry forever
        return abort(400, "Invalid JSON")

    # 2) (Optional) log it so you can inspect the shape
    app.logger.info("Received Zendesk payload:\n%s", payload)

    # 3) Fire off your Crew
    try:
        ZendeskFirstResponderCrew().crew().kickoff(inputs=payload)
    except Exception as e:
        app.logger.error("Crew kickoff error: %s", e)

    # 4) Ack immediately
    return "", 200

if __name__ == '__main__':
    # Make sure PORT matches your ngrok/localtunnel
    app.run(host="0.0.0.0", port=3000, debug=True)



# server.py

# from flask import Flask, request, abort

# app = Flask(__name__)

# @app.route('/webhook', methods=['POST'])
# def zendesk_webhook():
#     # 1) Grab the JSON body
#     payload = request.get_json(silent=True)
    
#     if not payload:
#         return abort(400, "Invalid JSON")
    
#     # 2) Print payload to console
#     print("==== Received Zendesk Payload ====")
#     print(payload)
#     print("===================================")
    
#     # Optionally also log it via Flask's logger
#     app.logger.info("Received Zendesk payload:\n%s", payload)
    
#     # 3) Respond OK
#     return "", 200

# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=3000, debug=True)

