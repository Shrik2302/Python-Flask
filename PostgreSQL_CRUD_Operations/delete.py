import psycopg2

try:
    connection = psycopg2.connect(user='postgres_user',
                                  password='Postgres_user_pasword',
                                  host='hostname',
                                  port='port',
                                  database='database_name')

    cursor = connection.cursor()
    delete_query = "DELETE FROM employee WHERE emp_id = 16"
    cursor.execute(delete_query)
    connection.commit()
    count = cursor.rowcount
    print(count)
except(Exception, psycopg2.Error) as error:
    print("ERROR")
    print(error)

finally:
    if connection:
        connection.close()
        print("connection closed")

