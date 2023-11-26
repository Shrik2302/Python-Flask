import psycopg2

try:
    connection = psycopg2.connect(user='postgres_user_name',
                                  password='postgres_user_password',
                                  host='hostname',
                                  port='port_number',
                                  database='database_name')

    cursor = connection.cursor()
    update_query = """UPDATE employee SET emp_name=%s where emp_id = %s """

    cursor.execute(update_query,('sunil', 16))
    connection.commit()
    print(cursor.rowcount)
except (Exception, psycopg2.Error) as error:
    print("ERROR")
    print(error)

finally:
    if connection:
        connection.close()
        print("connection closed")

    else:
        print("Connection was not completed")
