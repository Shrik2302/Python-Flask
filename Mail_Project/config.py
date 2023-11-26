from flask_mail import Mail
from app import app

# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sender_mail_address'
app.config['MAIL_PASSWORD'] = 'Provide_Mail_Password_Here'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

