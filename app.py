from flask import Flask, request, jsonify
app = Flask(__name__)

from datetime import datetime
from twilio.rest import TwilioRestClient
from twilio.twiml.messaging_response import MessagingResponse
from twilio import twiml
from twilio.rest import Client
account_sid = 'twilio_sid_goes_here'
auth_token = 'twilio_token_goes_here'
client = Client(account_sid, auth_token)


@app.route('/')
def homepage():
    return "hii"


@app.route('/sms', methods=['GET', 'POST'])
def sms_reply():
    print(request.form['Body'])
    body = request.form['Body']
    resp = MessagingResponse()
    resp.message(body)
    return str(resp)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
