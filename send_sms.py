from twilio.rest import Client
import os
TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

message = client.messages.create(
    to="+16503463236",
    from_="+16502279500",
    body="Hello from iCareMagicBox!!")

print(message.sid)    