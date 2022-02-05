import smtplib
from collections import namedtuple
from email.message import EmailMessage

from decouple import config

from .. import celery_app

MailSchema = namedtuple("MailSchema", ["sender", "destinatary", "subject", "body"])


@celery_app.task
def send_confirmation_mail(mail_schema):
    s = smtplib.SMTP(host=config("MAIL_HOST"), port=config("MAIL_PORT"))
    s.starttls()
    s.login(mail_schema.sender, config("MAIL_PWD"))

    message = EmailMessage()
    message["From"] = mail_schema.sender
    message["To"] = mail_schema.destinatary
    message["Subject"] = mail_schema.subject
    message.set_content(mail_schema.body)

    return s.send_message(message)
