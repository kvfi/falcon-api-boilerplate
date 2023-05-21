import logging
import smtplib
from email.message import EmailMessage

from falcon_api_boilerplate.utils.config import get_config

log = logging.getLogger(__name__)


def send_email(from_name: str, from_email: str, to: str = None, subject: str = None, body: str = ''):
    smtp_server = get_config('smtp.main.server')
    port = 587  # For starttls
    username = get_config('smtp.main.username')
    password = get_config('smtp.main.password')

    tos = [to]
    ccs = []

    msg = EmailMessage()

    msg['From'] = f'{from_name} <{from_email}>'
    msg['Subject'] = subject
    msg['To'] = ','.join(tos)
    msg['Cc'] = ','.join(ccs)
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body.encode())

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(username, password)
        server.send_message(msg)
