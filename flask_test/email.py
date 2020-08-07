from flask_mail import Message 
from flask_test import mail

def send_message(message):
    print(message.get('name'))    
    msg = Message(message.get('subject'), sender = message.get('email'),
            recipients = ['asibubernard@gmail.com'],
            body= message.get('message')
            )
    mail.send(msg)