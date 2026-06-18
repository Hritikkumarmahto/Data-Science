# A data structure is a method of organizing and storing in a computer so that it can be accessed ,processed and modified effeciently 
# python privides multiple data structure in python 


# List - List is a build in data structure that is use to store an ordered collection of items of multiple data types in a single variable.
# List is mutable - means it can be updated and modified , add, remove afte the list is created
# ordered - means list maintain the same order which they are inserted 
# index based - so the elements can be accessed using their position also support indexing and slicing 
# list manages memory automatically - List is dynamic

# ways to create a list
# using [] - 

a=[1,2,3,4,5]
print(a)

b=["banana","apple"]
print(b)


# using list constructor() - 

nums=list()
print(nums)  # will return empty list 

# creating list with elements 

numbers=list([1,2,3,4,5,6])
print(numbers)

# stirng list

name=list("hritik")
print(name)     # will break down each charater of string and pust them inside the list 

# a list can also created by passing an iterable (such as tuple , string, or another list)

alist=list((1,2,3,4,"hritik",[5,6,7,8]))   # here it will not break the string into character 

print(alist)


# creating a list with repeated elements 

a=[2]*5
b=[1]*9 
print(a) # 5 times 2
print(b) # 9 times 1


# inrernal representation of list

# python list store refrence to objects not the actual value directly 
# the list keep memory address of objects like int,float,boolean  Actual object stays seprately in memory 
# modifying a list object changes the original memory object 

# reassigning a new imutable object creates another object in memory insted of changing it 

# elements in list is accesses through 6
A=[33]*10
print(A[0]) # prints the first index elemet 

# negatice index is also supported -1 will print the last element

# element can be added through these methods

# 1 . append()   -  Adds an element at the end of the list

appendEg=[1,2,3]
appendEg.append(4)
print(appendEg)

# 2.  insert()   -  Adds element at a specific position

insertinto=[1,3]
insertinto.insert(1,2)
print(insertinto)

# 3.  extend()   -  Adds multiple elements at the end of the list 

extending=[1,2,3]
extending.extend([4,5,6])
print(extending)  

# since list is mutable so the values in the list can be updated by assigning new values using their index

extending[1]=6
print(extending)

# removing an elemtn 

#extending.remove(6) # removes the first occurence of an element 

# pop() - removes the element at the specifies index or removes last index if no index specified 

extending.pop()
print(extending)

extending.pop(0)    #removes the lement ar index 0
print(extending)


# del() - delete an element at the specified index
del extending[1] 


# clear() - removes all the elements in the list 
extending.clear()

# list can be iterated using for loop  allowing operatins to peroformed on each element 

a=[1,"hritik",3,4]
for i in a:
  print(i)

# nesteed list

a=[[2,3,4],[5,6,7]]

print(a[1][0])

for i in a:
  print(i)


# LIST comprehension 

#  
































































































































































# # Swaping two numbers using list 
# n=int(input("Enter the total no of elemets "))
# marks=[]

# for i in range (n):
#   Value=int(input("enter the elements :- "))
#   marks.append(Value)

# swap1=int(input("enter the index you want to swap "))
# swap2=int(input("enter the index 2 you want to swap with "))


# if swap1>=len(marks) or swap2>=len(marks):
#   print("Index out of range ")

# else:

#   temp=marks[swap1]
#   marks[swap1]=marks[swap2]
#   marks[swap2]=temp

# print("swaped list ")
# print(marks)


# min max

