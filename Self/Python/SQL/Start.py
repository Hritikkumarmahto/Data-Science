import pymysql

mydbconnect=pymysql.connect(host="localhost",user="root",password="Hritik@1234")

myCursor=mydbconnect.cursor()

myCursor.execute("CREATE DATABASE IF NOT EXISTS Testing")

if myCursor.rowcount>0:
  print("database already exist ")
else:
  print("Database created sucessfully")
  for db in myCursor:
    print(db)

myCursor.execute("USE Testing")

CreateTable="""CREATE TABLE IF NOT EXISTS class (
            roll_no INT PRIMARY KEY, 
            name varchar(40),
            address varchar(30),
            detasils varchar(30), 
            pincode int)"""

myCursor.execute(CreateTable)
print("Table created sucessfully ")

# insert data 

# rollno=int(input("enter roll no "))
# name=input("enter name ")
# address=input("enter address")
# details=input("enter the details ")
# pincode=int(input("enter pincode"))

insertData="INSERT INTO class (roll_no,name,address,detasils,pincode) VALUES (%s,%s,%s,%s,%s)"

# myCursor.execute(insertData,(rollno,name,address,details,pincode))

Values=(142,"Hritik","kishanganj","Bihar",9899)

print(myCursor.rowcount," Inserted")
myCursor.execute(insertData,Values)

mydbconnect.commit()

# showing full table data 

print ("Here is the complete table data")

showQuery="select * from class"

myCursor.execute(showQuery)

showResult=myCursor.fetchall()

for i in showResult:
  print(i)

# showing only roll no from the table

showName="select roll_no from class"

myCursor.execute(showName)

nameRes=myCursor.fetchall()

for x in nameRes:
  print (x)

#  where condition to show the data

whereQuery = "select pincode as pin from class where pincode=855108 LIMIT 1"
myCursor.execute(whereQuery)

wereRes = myCursor.fetchall()

for w in wereRes:
    print(w[0])

mydbconnect.close()




