from app import sms_client

sending_phone = '+12165849532'

def send_sms(receiving_phone, text_body):
    sms_client.messages.create(
        to=receiving_phone,
        from_=sending_phone,
        body=text_body
    )