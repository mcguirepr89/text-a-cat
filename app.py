from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from catify import catify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def sms_reply():
    """Respond to incoming messages with a catified reply."""
    incoming_msg = request.form.get('Body')
    cat_response = catify(incoming_msg)

    resp = MessagingResponse()
    resp.message(cat_response)
    return str(resp)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
