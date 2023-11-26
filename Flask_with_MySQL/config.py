from app import app
from flask_mysqldb import MySQL


app.config['MYSQL_HOST'] = 'hostname'
app.config['MYSQL_USER'] = 'user_name'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'database_name'

mysql = MySQL(app)
