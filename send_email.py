from flask import Flask, request
from flask_mail import Mail,Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

# TODO: replace those
app.config['MAIL_USERNAME'] = 'kenan.soylu@ooptica.ist'  # enter your email here
app.config['MAIL_DEFAULT_SENDER'] = 'kenan.soylu@ooptica.ist' # enter your email here
app.config['MAIL_PASSWORD'] = '' # enter your password here

mail = Mail(app)

@app.route('/send-mail', methods=['POST'])
def send_mail():
	options = request.form["options"]
	sender_name = options["sender_name"]
	sender_mail = options["sender_mail"]
	subject = options["sender_subject"]
	body = options["sende_body"]

	# Send mail to ooptica
	msg = Message(subject, recipients=['info@ooptica.ist'])
	msg.body = body
	mail.send(msg)

	# Send another mail to sender
	thanks_msg = Message("Thanks for your message.", recipients=[sender_mail])
	thanks_msg.body = "We thank you for your message..."
	mail.send(thanks_msg)

	return 'Message has been sent!'
	
if __name__ == '__main__':
	app.run()