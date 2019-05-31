from Flask import flask
from flask_mail import Mail,Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = ooptica.ist
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = request
app.config['MAIL_PASSWORD'] = 'request.POST["email"]'
app.config['MAIL_DEFAULT_SENDER'] = None
app.config[''] = None
app.config[''] = None
app.config[''] = None
app.config[''] = None

mail = Mail(app)

@app.route('/')
def index():
	nameofperson = request.POST["name"]
	emailofperson = request.POST["email"]
	subjectofperson = request.POST["subject"]
	messageofperson = request.POST["message"]
	
	msg = Message(subjectofperson, sender= emailofperson, recipients:['info@ooptica.ist'])
	msg.body = messageofperson
	mail.send(msg)
	
	return 'Message has been sent!'
	
if __name__ == '__main__':
	app.run()