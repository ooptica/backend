#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, request, abort, Response
from flask_mail import Mail, Message
import os

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#
app = Flask(__name__, static_folder='static', static_url_path='')
app.config.from_object('config')

app.config['MAIL_SERVER'] = 'smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

# TODO: replace those
#app.config['MAIL_USERNAME'] =  'info@ooptica.ist' # enter your name here
#app.config['MAIL_DEFAULT_SENDER'] = 'info@ooptica.ist' # enter your email here
#app.config['MAIL_PASSWORD'] = '' # enter your password here

mail = Mail(app)

@app.route('/send-mail', methods=['POST'])
def send_mail():
	sender_name = request.form["sender_name"]
	sender_mail = request.form["sender_mail"]
	subject = request.form["sender_subject"]
	body = request.form["sender_body"]
	

	# Send mail to ooptica
	msg = Message(subject, sender = [sender_mail] , recipients=['info@ooptica.ist'])
	msg.body = body
	mail.send(msg)

	# Send another mail to sender
	thanks_msg = Message("Thanks for your message.", recipients=[sender_mail])
	thanks_msg.body = "We thank you for your message..."
	mail.send(thanks_msg)

	return 'Message has been sent!'

@app.route('/', methods=['GET'])
def home():
    return app.send_static_file("index.html")
    
@app.route('/face-filter', methods=['GET'])
def face_filter():
    return app.send_static_file("face-filter.html")
    
@app.errorhandler(404)
def not_found_error(error):
    return app.send_static_file("404.html"), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    