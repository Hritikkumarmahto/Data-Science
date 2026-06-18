# List comprehension is a sort way to create a list in python using one line of code
# it helps write clean and re


# Syntax
# {expression for item in iterable}
# Without comprehension 

numbers=[]
for i in range (1,6):
  numbers.append(i)
print(numbers) 

# with list comprehension 

numbers=[i for i in range (1,10)]

print(numbers)

squares=[i**2 for i in range (1,5)]
print(squares)

str1=[1,2,3,4]
str2=str1.reverse()
print(str2)