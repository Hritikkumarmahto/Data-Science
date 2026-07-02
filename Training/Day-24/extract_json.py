import json
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="Hritik@1234")
cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS Products")

cursor.execute("USE Products")

print("Database created successfully (or already exists).")


with open("Training\Day-24\product.json", "r") as file:
    data = json.load(file)

product = data["products"][0]

columns = []

for key, value in product.items():
    if isinstance(value, (list, dict)):
        continue

    if isinstance(value, int):
        dtype = "INT"
    elif isinstance(value, float):
        .
        dtype = "FLOAT"
    else:
        dtype = "TEXT"

    columns.append(f"{key} {dtype}")

query = f"CREATE TABLE IF NOT EXISTS Products ({', '.join(columns)})"

cursor.execute(query)

cursor.execute("SHOW TABLES")

tables = cursor.fetchall()

for table in tables:
    print(table[0])
    
cursor.execute("DESCRIBE Products")

columns = cursor.fetchall()

for column in columns:
    print(column)

print("Table created successfully.")





