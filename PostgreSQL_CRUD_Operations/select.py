import psycopg2

try:
    connection = psycopg2.connect(user='postgres',
                                  password='root',
                                  host='localhost',
                                  port='5432',
                                  database='basic')

    cursor = connection.cursor()
    cursor.execute("SELECT * from employee ORDER BY emp_id")
    rows = cursor.fetchall()
    # print(rows)
    for row in rows:
        print("emp id :",row[0])
        print("emp_name :", row[1])
        print("role :",row[2])
        print("joining date :", row[3])
        print("start_time :", row[4])
        print("details :", row[5])
        print()
except Exception as ex:
    print("ERROR")
    print(ex)

else:
    print("connection closed")
    connection.close()
