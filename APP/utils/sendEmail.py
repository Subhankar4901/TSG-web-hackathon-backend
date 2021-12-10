from flask_mail import Mail, Message

# the sender should allow less secure apps for this to work
# Sample usage: sendEmail(app, "test-subject", "test-body", ["recipient123@gmail.com"])
def sendEmail(mail: Mail, messageSubject: str, messageBody: str, sender: str, recipients: list):
	msg = Message(
					messageSubject,
					sender = sender,
					recipients = recipients
				)
	msg.body = messageBody
	mail.send(msg)
	return 'Mail Sent'
