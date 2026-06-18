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
    choice = input(
        f"Table '{table_name}' already exists.\n"
        "Press Y to drop and recreate or N to continue: "
    ).upper()

    if choice == "Y":
        cursor.execute(f"DROP TABLE {table_name}")

        cursor.execute(f"""
        CREATE TABLE {table_name}
        (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50),
            address VARCHAR(100)
        )
        """)

        mysql_connection.commit()
        print("Table recreated successfully.")
else:
    cursor.execute(f"""
    CREATE TABLE {table_name}
    (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        address VARCHAR(100)
    )
    """)
    mysql_connection.commit()
    print("Table created successfully.")

while True:

    print("\n===== MENU =====")
    print("1. Insert Record")
    print("2. View Records")
    print("3. Update Record")
    print("4. Delete Record")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter Name: ")
        address = input("Enter Address: ")

        cursor.execute(
            f"INSERT INTO {table_name}(name,address) VALUES(%s,%s)",
            (name, address)
        )

        mysql_connection.commit()
        print("Record inserted successfully.")

    elif choice == "2":

        cursor.execute(f"SELECT * FROM {table_name}")
        records = cursor.fetchall()

        if records:
            print("\nID\tNAME\tADDRESS")
            print("-" * 30)

            for row in records:
                print(f"{row[0]}\t{row[1]}\t{row[2]}")
        else:
            print("No records found.")

    elif choice == "3":

        id_ = int(input("Enter ID to update: "))
        new_name = input("Enter New Name: ")
        new_address = input("Enter New Address: ")

        cursor.execute(
            f"UPDATE {table_name} SET name=%s,address=%s WHERE id=%s",
            (new_name, new_address, id_)
        )

        mysql_connection.commit()

        if cursor.rowcount > 0:
            print("Record updated successfully.")
        else:
            print("ID not found.")

    elif choice == "4":

        id_ = int(input("Enter ID to delete: "))

        cursor.execute(
            f"DELETE FROM {table_name} WHERE id=%s",
            (id_,)
        )

        mysql_connection.commit()

        if cursor.rowcount > 0:
            print("Record deleted successfully.")
        else:
            print("ID not found.")

    elif choice == "5":

        print("Exiting...")
        break

    else:
        print("Invalid choice.")

cursor.close()
mysql_connection.close()