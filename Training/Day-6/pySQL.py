import pymysql
mysql_conncetion=pymysql.connect(user="root",host="localhost",password="Hritik@1234")

cursor=mysql_conncetion.cursor()

cursor.execute("create database Training")
#cursor.execute("show databases")

for i in cursor.fetchall():
  print(i)
