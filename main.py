import os
from redis import Redis
from rq import Queue
from sendgrid import SendGridAPIClient

from build_email import send_message

sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

q = Queue(connection=Redis())

emails = ['adamxtaylor+1@gmail.com', 'adamxtaylor+2@gmail.com', 'adamxtaylor+3@gmail.com']

for email in emails:
    q.enqueue(send_message, sendgrid_client, email)