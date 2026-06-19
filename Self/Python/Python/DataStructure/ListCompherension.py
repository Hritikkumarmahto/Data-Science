# # List comprehension is a sort way to create a list in python using one line of code
# # it helps write clean and re


# # Syntax
# # {expression for item in iterable}
# # Without comprehension 

# numbers=[]
# for i in range (1,6):
#   numbers.append(i)
# print(numbers) 

# # with list comprehension 

# numbers=[i for i in range (1,10)]

# print(numbers)

# # printing number of square using list comphrension 

# squares=[i**2 for i in range (1,5)]
# print(squares)


# a = [1, 2, 3, 4, 5]
# res = [val for val in a if val % 2 == 0]
# print(res)


# checkEvenOdd=[(i, "Yes even"  if i%2==0 else "not even") for i in range (1,100)]
# print(checkEvenOdd)

# # function to check even and odd 
# def even_odd(a, b):
#     numbers = [
#         [i for i in range(a, b) if i % 2 == 0],   # Even numbers
#         [i for i in range(a, b) if i % 2 != 0]    # Odd numbers
#     ]
#     return numbers

# print(even_odd(1, 10))


# # prining name if character is present 
# list_name=["Hritik","Rohan","Mamai", "Hello"]
# def check_char(list_name,ch):
    
#     checkchar=[i for i in list_name if ch in i]
#     return(checkchar)
# ch=input("enter the char ")
# print(check_char(list_name,ch))


# creaete database using list

import pymysql

dbconnection=pymysql.connect(host="localhost", user="root", passwd="Hritik@1234")

mycursor=dbconnection.cursor()

list_name=["hritik","Mahto","Kumar"]



for i in  list_name:
   mycursor.execute(f"create database if not exists {i}")
print("data Bases created sucessfully ")

mycursor.execute("show databases")

for i in mycursor.fetchall():
  print(i)
mycursor.execute("drop database mahto")

dbconnection.commit()
