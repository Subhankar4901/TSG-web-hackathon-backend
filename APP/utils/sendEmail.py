from flask_mail import Message
from .. import mail

# the sender should allow less secure apps for this to work
# Sample usage: sendEmail(app, "test-subject", "test-body", ["recipient123@gmail.com"])
def sendEmail(messageSubject: str, messageBody: str,recipients: list):
	msg = Message(messageSubject,recipients = recipients)
	msg.body = messageBody
	mail.send(msg)
	return 'Mail Sent'
