import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="Hritik@1234",
    database="college"
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM students")

row = cursor.fetchone()

print(row)