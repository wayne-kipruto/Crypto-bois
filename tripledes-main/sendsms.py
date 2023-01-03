import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID'] = 'AC1e6a6de7e1b7d2f392bf8b0417c71781'
auth_token = os.environ['TWILIO_AUTH_TOKEN'] = 'aceae949f9b1f2898f3d0bd092f730d1'
client = Client(account_sid, auth_token)
def send_sms(the_body,to):

    message = client.messages.create(
                              body=the_body,
                              from_='+18284714013',
                              to= to
                          )
    return message.sid
# 5bc6a91fffa84fddeccac854d6f53ae6984c619682f20ba7d21a79925d6768bb


