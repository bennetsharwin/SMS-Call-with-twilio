from twilio.rest import Client
#Go to twilio.com to get the below credentials.
#make sure to fill them before running the program.
ACCOUNT_SID = ''
AUTH_Token = ''
TWILIO_PHONE = ''
My_PHONE = ''

client = Client(ACCOUNT_SID, AUTH_Token)

def send_sms(message, to_phone):
    data = client.messages.create(
        body=message,
        from_=TWILIO_PHONE,
        to=to_phone
    )
    print(data.price)


send_sms('This Is A Price Test Message', My_PHONE)
