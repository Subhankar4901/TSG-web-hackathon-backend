from flask_mail import Message
from .. import app, mail
from threading import Thread

# function which will be excuted in threads
def send_email_thread(msg):
	with app.app_context():
		mail.send(msg)

# the sender should allow less secure apps for this to work
# Sample usage: sendEmail("test-subject", "test-body", ["recipient1@gmail.com","recipient2@gmail.com",..])
def sendEmail(messageSubject: str, messageBody: str, recipients: list):
	with app.app_context():
		for recipient in recipients:          
			msg = Message(messageSubject, recipients = [recipient])
			msg.body = messageBody
			thr = Thread(target=send_email_thread, args=[msg])
			thr.start()
	return 'Mails Sent'