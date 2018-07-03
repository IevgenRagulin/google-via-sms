import os
from flask import Flask, request, jsonify
app = Flask(__name__)

from datetime import datetime
from twilio.rest import TwilioRestClient
from twilio.twiml.messaging_response import MessagingResponse
from twilio import twiml
from twilio.rest import Client
client = Client(os.environ['TWILIO_SID'], os.environ['TWILIO_AUTH_TOKEN'])


@app.route('/')
def homepage():
    print(os.environ['TWILIO_SID'])
    print(os.environ['TWILIO_AUTH_TOKEN'])
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
