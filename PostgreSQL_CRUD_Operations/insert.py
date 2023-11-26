import psycopg2
try:
    connection = psycopg2.connect(user='postgres_username',
                                  password='postgres_user_passwerd',
                                  host='host_name',
                                  port='port_number',
                                  database='database_name')
    cursor = connection.cursor()
    query = ("INSERT INTO employee VALUES (%s,%s,%s,%s,%s,%s)")
    values = (16, 'ajay', 'lead', '2022-06-09', '15:00:00', '{"name":"ajay","role":"lead"}')
    cursor.execute(query, values)
    connection.commit()
    count = cursor.rowcount
    print("Row count:", count)

except (Exception, psycopg2.Error) as error:
    print("Error")
    print(error)

finally:
    if connection:
        connection.close()
        print("connection closed")
