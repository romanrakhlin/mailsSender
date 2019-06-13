import smtplib
import os
import mimetypes
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# def to send mail
def send_email(addr_from, password, addr_to):
    msg_subj = input("Subject: ")  # subject of message
    msg_text = input("Text: ")  # text of message
    msg = MIMEMultipart()
    msg['From'] = addr_from
    msg['To'] = addr_to
    msg['Subject'] = msg_subj

    body = msg_text
    msg.attach(MIMEText(body, 'plain'))

    # for gmail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(addr_from, password)
    server.send_message(msg)
    server.quit()

_from = input("Gmail: ")  # input gmail
_password = input("password: ")  # input gmail password
_to = input("from: ")  # input mail where we wanna send message (any mails)

# sending...
send_email(_from, _password, _to)
