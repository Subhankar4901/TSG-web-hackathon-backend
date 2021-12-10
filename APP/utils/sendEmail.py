from flask.app import Flask
from flask_mail import Mail, Message

# Sample usage: sendEmail(app, "test-subject", "test-body", ["recipient123@gmail.com"])
def sendEmail(app: Flask, messageSubject: str, messageBody: str, recipients: list):
	mail = Mail(app)
	msg = Message(
					messageSubject,
					sender = app.config['MAIL_USERNAME'],
					recipients = recipients
				)
	msg.body = messageBody
	mail.send(msg)
	return 'Sent'
