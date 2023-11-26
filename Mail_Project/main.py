from flask_mail import Message
from app import app
from config import mail
from flask import render_template


@ app.route('/')
def index():
	msg = Message(
			'Hello user welcome..',
			sender=('Shrikant Mane', 'shrikant99.mane.com'),
			recipients=['shrikant101.mane@gmail.com'],

			)
	msg.html = render_template("Home.html")
	mail.send(msg)
	return 'sent'

@app.route('/reset')
def reset():
	msg = Message(
		'Reset your password .',
		sender=('Shrikant Mane', 'shrikant99.mane.com'),
		recipients=['shrikant101.mane@gmail.com'],

	)
	msg.html = render_template("reset.html")
	mail.send(msg)
	return 'sent'

if __name__ == '__main__':
	app.run(debug = True)

