import pymysql

mysql_connection = pymysql.connect(
    user="root",
    host="localhost",
    password="Hritik@1234",
    database="Training"
)

cursor = mysql_connection.cursor()

table_name = input("Enter table name: ").strip()

cursor.execute("SHOW TABLES")
tables = [table[0] for table in cursor.fetchall()]

if table_name in tables:
    cursor.execute(f"DROP TABLE {table_name}")
    print(f"Table '{table_name}' dropped successfully.")

query = f"""
CREATE TABLE {table_name}
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20),
    address VARCHAR(20)
)
"""

cursor.execute(query)
print(f"Table '{table_name}' created successfully.")

insert_query = f"""
INSERT INTO {table_name} (name, address)
VALUES
('Hritik', 'Delhi'),
('Rahul', 'Noida'),
('Aman', 'Ghaziabad'),
('Priya', 'Mumbai'),
('Neha', 'Pune')
"""

cursor.execute(insert_query)

mysql_connection.commit()

print("5 records inserted successfully.\n")

cursor.execute(f"SELECT * FROM {table_name}")

data = cursor.fetchall()

print("Table Data:")
for row in data:
    print(row)

cursor.close()
mysql_connection.close()