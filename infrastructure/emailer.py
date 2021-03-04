from threading import Thread
from flask_mail import Message

from app import app
from app import mail

def send_async_email(app, msg):
  with app.app_context():
    try:
      mail.send(msg)
    except ConnectionRefusedError:
      raise InternalServerError("[MAIL SERVER] not responding.")

def send_email(subject, sender, recipients, body_text, body_html):
  msg = Message(subject, sender=sender, recipients=recipients)
  msg.body = body_text
  msg.html = body_html
  Thread(target=send_async_email, args=(app, msg)).start()