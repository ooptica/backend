from flask import Flask, request
from flask_mail import Mail,Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

@app.route('/', methods=['POST'])
def datahandle():
# TODO: replace those
	username = request.form["sender_name"]
	useremail = request.form["sender-email"]
	app.config['MAIL_USERNAME'] = username # enter your name here
	app.config['MAIL_DEFAULT_SENDER'] = useremail # enter your email here
	app.config['MAIL_PASSWORD'] = '' # enter your password here
	return request.form["sender-email"]


mail = Mail(app)

@app.route('/send-mail', methods=['POST'])
def send_mail():
	sender_name = request.form["sender_name"]
	sender_mail = request.form["sender_mail"]
	subject = request.form["sender_subject"]
	body = request.form["sender_body"]
	

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