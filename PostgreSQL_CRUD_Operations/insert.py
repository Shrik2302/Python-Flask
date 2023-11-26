import psycopg2
try:
    connection = psycopg2.connect(user='postgres',
                                  password='root',
                                  host='localhost',
                                  port='5432',
                                  database='basic')
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
