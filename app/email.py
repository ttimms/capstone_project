from flask_mail import Message
from app import mail

def send_email(email, text_body):
    msg = Message(subject='ALERT', sender=("CoPilot", mail.MAIL_USERNAME), recipients=[email])
    msg.body = text_body
    mail.send(msg)