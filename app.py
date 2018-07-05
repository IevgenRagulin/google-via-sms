import os
from flask import Flask, request, jsonify
app = Flask(__name__)
import requests
import json

from datetime import datetime
from twilio.rest import TwilioRestClient
from twilio.twiml.messaging_response import MessagingResponse
from twilio import twiml
from twilio.rest import Client
client = Client(os.environ['TWILIO_SID'], os.environ['TWILIO_AUTH_TOKEN'])


@app.route('/')
def homepage():
    return "hii"


@app.route('/sms', methods=['GET', 'POST'])
def sms_reply():
    print(request.form['Body'])
    body = request.form['Body']
    resp = MessagingResponse()
    google_response = requests.get('https://www.googleapis.com/customsearch/v1?key='+os.environ['GOOGLE_API_KEY']+'&cx='+os.environ['CUSTOM_SEARCH_CONSOLE']+'&q='+body).content
    google_response = json.loads(google_response)
    print(google_response)
    resp.message(google_response['items'][0]['snippet'])
    return str(resp)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
