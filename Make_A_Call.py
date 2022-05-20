#Only calls to verified numbers can be made, unless you upgrade from the trial version in twilio.
from twilio.rest import Client

ACCOUNT_SID = 'ACc19b7e18b19735a11fbed453f5edf011'
AUTH_Token = 'd59b2a88a3d87fecce43308891838a93'
TWILIO_PHONE = '+13253357225'
My_PHONE = '+917994026917'

client = Client(ACCOUNT_SID, AUTH_Token)

def send_sms(message, to_phone):
    data = client.messages.create(
        body=message,
        from_=TWILIO_PHONE,
        to=to_phone
    )
    print(data.price)


#send_sms('This Is A Price Test Message', My_PHONE)

def make_call(to_phone):
    call = client.calls.create(
        twiml='<Response><Say>Ahoy, World!, This is a call from anonymous!</Say></Response>',
        to=to_phone,
        from_=TWILIO_PHONE
    )
    print("Total Cost: ", call.price)
    print("SID: ", call.sid)

make_call(My_PHONE)     