import psycopg2

try:
    connection = psycopg2.connect(user='postgres',
                                  password='root',
                                  host='localhost',
                                  port='5432',
                                  database='basic')

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

