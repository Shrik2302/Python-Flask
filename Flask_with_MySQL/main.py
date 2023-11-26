from app import app
from config import mysql
from flask import jsonify
from flask import flash, request


@app.route('/add', methods=['POST'])
def add_data():
	content = request.get_json()
	name = content['name']
	email = content['email']
	phone = content['phone']
	address = content['address']
	cur = mysql.connection.cursor()
	cur.execute("INSERT INTO rest_emp(name, email, phone, address) VALUES (%s, %s, %s, %s)",
				(name, email, phone, address))
	mysql.connection.commit()
	cur.close()
	return 'success'


@app.route('/get', methods=['GET'])
def get_data():
	cur = mysql.connection.cursor()
	cur.execute("SELECT * FROM rest_emp")
	myresult = cur.fetchall()
	respon = jsonify(myresult)
	respon.status_code = 200
	cur.close()
	return respon


@app.route('/get/<int:id>')
def get_emp(id):
	try:
		cur = mysql.connection.cursor()
		cur.execute("SELECT * FROM rest_emp WHERE id = %s", (id,))
		myresult = cur.fetchone()
		respon = jsonify(myresult)
		respon.status_code = 200
		cur.close()
		return respon
	except Exception as e:
		print(e)
	finally:
		pass


@ app.route('/update', methods=['PUT'])
def update_emp():
	try:
		content = request.get_json()
		id = content['id']
		name = content['name']
		email = content['email']
		phone = content['phone']
		address = content['address']
		cur = mysql.connection.cursor()
		cur.execute("UPDATE rest_emp SET name=%s, email=%s, phone=%s, address=%s WHERE id=%s",
					(name, email, phone, address, id))
		mysql.connection.commit()
		respon = jsonify("employee updated succesfully...")
		respon.status_code = 200
		cur.close()
		return respon
	except Exception as e:
		print(e)
	finally:
		pass


@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_emp(id):
	try:
		cur=mysql.connection.cursor()
		cur.execute("DELETE FROM rest_emp WHERE id = %s", (id,))
		mysql.connection.commit()
		respon = jsonify("employee deleted succesfully...")
		respon.status_code = 200
		cur.close()
		return respon
	except Exception as e:
		print(e)
	finally:
		pass


if __name__ == '__main__':
	app.run()