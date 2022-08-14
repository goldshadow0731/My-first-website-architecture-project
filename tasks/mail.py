from celery import Task
from flask_mail import Message

from base_api import app
from base_api import mail_app


class SendMail(Task):
    def run(self, title, body, reciver, sender=None, attachments=None):
        with app.app_context():
            msg = Message(
                title,
                recipients=reciver if isinstance(reciver, list) else [reciver],
                body=body,
                attachments=attachments)
            mail_app.send(msg)
        return title, body, reciver
