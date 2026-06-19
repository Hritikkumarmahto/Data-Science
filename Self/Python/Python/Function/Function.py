# function is a group of statement that is use to perform a specific task

# function are block of code to perform specific task when it is caled 

# types of function 
# 1. take nothing return nothing
# 2. take something return nothing 
# 3. take nothing return something 
# 4. take something return something 

# Argurments ad parameters 
# 1. default paramaters
# 2. positional argument 
# 3. keyword argument
# 4. arbitary arguments 

# lamda function ( anonymous function )

# hcf high order function

# by default every function retunr none value
 
# def keyword is use to create function
# function defination 
def func_name(parameter1,paremeter2):  # this is how we define a function whihc contains group of statements
  sum=parameter1+paremeter2
  print(sum)
  return sum          # return keyword is use to return something from the function

func_name(13,12) #these are the argumenet means real values which will called by the functiona as a perameter

print(func_name(23,45)) # here we are using the return sum which was done by the function


# Non parametrised function
def print_hello():
  print("print_hello")

output=print_hello()
print(output) # this will return none because the function is not returning anything 



# WAP to get average of three numbrs using function  
def average(a,b,c):
  average=(a+b+c)/3
  return average

average_of_three_num=average(2,3,4)  # passing argument into dunction to calcuclater average
print(int(average_of_three_num))



# Types of function 

# 1. Built in functions- print(), len(), type(), range() 
# 2. User defined function - function defined by the user  


# default parameters 

def fun_product(a,b=3): # here b is defined as a default parameter  
  print(a*b)
  return a*b

fun_product(3) # here we have passed the value of a only for b the value will be default 

# but we cannot write default argument firs then passing argument for another 
  
# def fun_product(a=2,b): # here a is defined as a default parameter  whihc will throw a error 
#   print(a*b)
#   return a*b


def print_length(list):
  length_of=len(list)
  return length_of

length_of_list=print_length([1,2,3,4,5])

print("lenght of the list is ")
print(length_of_list)


# print the list in same line 
def print_list_in_single_line(list):
  for item in list:

    print(item,end=" ")
  return 
print("printing the lsit in same line")
print_in=print_list_in_single_line([1,23,4,5,5,21,1])
print(print_in)

# find factorial of n

def find_factorial(n):
  factor=1
  for i in range (1,n+1):
    factor*=i
  return factor

print("factorial is ")
print(find_factorial(5))


# convert usd into inr
def convert_currency(inr):
  usd=95
  print(usd*inr)

inr=int(input("enter inr "))
print(" usd to inr is ")
convert=convert_currency(inr)

# check the number is odd or even 
def odd_even_check(num):
  if num%2==0:
    print("number is even")
  else:
    print("this is a odd number")
  
print(odd_even_check(9))


# positional arguments means all the arguments pased in a funciton should be in same postion as function

# the order matters with the positional arguments 


# swithching te position can change the result 

# Mixing Positional and Keyword Arguments
# You can mix positional and keyword arguments in a function call.

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)


# passsing diffrent data types 
# we can also sent any data type as an argument to a function - stirng,int,list,tuple,dictionary 

# the data type will be preserved inside the function


def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]   # here we are creating list data type
my_function(my_fruits)    # here we are passing the list into the function for operatuo



# Sending a dictionary as an argument:

def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)



# Functions can return values using the return statement:


def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)

# FUNCTION can return diffent data types 

def myfunction_for_datatypes():
  return [1,23,4,"hritik"]

data_types_access=myfunction_for_datatypes()
print(" the list elemetns are  -----")
print(data_types_access[3])







# # function are block of code to perform specific task when it is caled 

# # types of function 
# # 1. take nothing return nothing
# # 2. take something return nothing 
# # 3. take nothing return something 
# # 4. take something return something 

# # Argurments ad parameters 
# # 1. default paramaters
# # 2. positional argument 
# # 3. keyword argument
# # 4. arbitary arguments 

# # lamda function ( anonymous function )

# # hcf high order function

# # by default every function retunr none value

# def add(a,b):
#   c=a+b
#   return c   # this will return only the result not two retirns 
#   return "hello"

# print(add(12,b=19))  # we can alos use assign operator to send the arguments 



# def add(a,b):
#   return a+b
# def subtraction(a,b):
#   return a-b
# def multi(a,b):
#   return a*b
# def div(a,b):
#   return a/b

# print( "please select the operation you want to perform  ")
# print("Press + to add")
# print("Press - to subtract")
# print("Press x to multiply")
# print("press / for division")
# choice=input("please select you choice ")

# num1=int(input("enter first number"))
# num2=int(input("enter second number"))




# if(choice=='+'):
#   res=add(num1,num2)
#   print(res)
# elif choice=='-':
#   res=subtraction(num1,num2)
#   print(res)
# elif choice=='x':
#   res=multi(num1,num2)
#   print(res)
# elif choice=='/':
#   res=div(num1,num2)
#   print(res)

# else:
#   print("invailed operation ")



# # positional arguments means all the arguments pased in a funciton should be in same postion as function

# # the order matters with the positional arguments 


# # swithching te position can change the result 

# # Mixing Positional and Keyword Arguments
# # You can mix positional and keyword arguments in a function call.

# def my_function(animal, name, age):
#   print("I have a", age, "year old", animal, "named", name)

# my_function("dog", name = "Buddy", age = 5)


# # passsing diffrent data types 
# # we can also sent any data type as an argument to a function - stirng,int,list,tuple,dictionary 

# # the data type will be preserved inside the function


# def my_function(fruits):
#   for fruit in fruits:
#     print(fruit)

# my_fruits = ["apple", "banana", "cherry"]   # here we are creating list data type
# my_function(my_fruits)    # here we are passing the list into the function for operatuo



# # Sending a dictionary as an argument:

# def my_function(person):
#   print("Name:", person["name"])
#   print("Age:", person["age"])

# my_person = {"name": "Emil", "age": 25}
# my_function(my_person)



# # Functions can return values using the return statement:


# def my_function(x, y):
#   return x + y

# result = my_function(5, 3)
# print(result)

# # FUNCTION can return diffent data types 

# def myfunction_for_datatypes():
#   return [1,23,4,"hritik"]

# data_types_access=myfunction_for_datatypes()
# print(" the list elemetns are  -----")
# print(data_types_access[3])

# # A function that returns a tuple 

def mty_function():
  return (10,20,20)

a,b,c=mty_function()

print(a,b,c)

# positionnal arguments 
# A positional argument is an argument that is passed to a function based on its position (order).
# we can specify that a function can have only positional arguments to specify positional argument only add, / after arguments.

def greet(name, age):
    print("Name:", name)
    print("Age:", age)

greet("Hritik", 22)

#  greet(22, "Hritik")  # this is a wrong order to pass an argument 

# The / in a function definition is used to specify positional-only arguments.

def my_func(name,/):
  print("hello",name)
my_func("hritik")

# Without /
def greet(name, age):
    print(name, age)

greet("Hritik", 22)          # Works
greet(name="Hritik", age=22) # Also works

# The arguments can be passed either by position or by keyword.

# with /

def greeet(name,age, /): # here name and age are position only argument 
   print(name, age)  

greeet("hritik",23)  # works because this is in position 

greet(name="hritik",age=23) # this will not work because this only accepts positional argument not keyword argument 

# Why use /?
# 1. Force users to pass arguments in order  
def func(a, b, /, c, d):
    pass

func(1, 2, 3, 4)          # ✅
func(1, 2, c=3, d=4)      # ✅
func(a=1, b=2, c=3, d=4)  # ❌ 


# keyword only argument   

# to specify that a function can have only  keyword arguments, add *, before the arguments  

def my_funct(*,name):
   return name
my_func(name="hritik") # here we are passing only keyword argumetn because the keyword only accepts it 

# without * we are allowed to use positional arguments even if the function excepts the keyword arguments:
def my_function(*, name):
  print("Hello", name)

my_function("Emil")  # With *,, you will get an error if you try to use positional arguments:

# combining positional only and keyword only argument 
# yes we can apply both type of argument in same function

# arguments before / are positonal argumetn and argument after * are positional arguments   

def my_funct(a,b,/,*d,e,f):
   return a+b+c+d+e+f
print(my_func(2,3,d=13,e=34,f=90))


# *args and **kwargs

# by default a function must be called with the correct number of arguments 
# however you may not know how many that will passed into the your function 

# *args and ** kewargs - allows user to accepts unknown number of arguments 

# Aribitary Arguments - *args 
# if we dont know how many arguments will be passed into your add * before the perammeter name 
# this way the function can recieve tuple of arguments and can  access the items accordingly


def myfunct(*a):
   print( " my name is hritik",a[2])

my_function("mahto","kumar","hritik")

# Aribitry arguments are often sortend to *args in python 

# *arge this perameter allow the function to accept any number of positional arguments 
# inside the function the, args behave like tuple containing all the passed arguments.

def myfunct(*args):
   print(type(args))
   print([1]) # here is how we can access individualt elements here 
   print([0])
   print([2])
myfunct("hritik","mahto","kumar")

# using *args before regular perameters * args
# regular parameter must come before *args

def my_funct(greeting,*names):
   for i in names:
      print(greeting,i)
my_funct("hello","hritik","kumar","rohit")   # hello assigned to greeting and rest are collected in names

# it can be useful when we have to calculate sum of any numbers

def sum_of_any_number(*numbers):
   total=0
   for i in  numbers:
      total+=i
   return total
sum_of_any_number(1,2,3,4,4)
sum_of_any_number(1,2)

# finding the maximum values 

def max_num(*numbers):
   
   if(len(numbers)==0):
      return None
   max_num_is=numbers[0]

   for i in numbers:
      if i>max_num_is:
         max_num_is=i
   return max_num_is
print(max_num(1,2,3,4,5,56))





# Abitrary keywords arguments // **kwargs

# if you dont know how many keyword argument will be passed in the function. Add ** two asterisks before the perameter name

# this wahy the function will recieve a dictionary of arguments and can access the items accordingly 

def keyDUnction(**name):
   print(name["lname"],"hist first name is",name["firstname"])
keyDUnction(firstname="hritik",lname="mahto")



# **kwargs argument allow the function to acccept any number of keyword arguments inside a function 
# inside a function **kwargs becomes a dictionary containing all the keyword arguments  


def my_function(**name):
   print("my name is ",name["name"])
   print("my age is ",name["age"])

print(my_function(name="hritik",age="23"))

# we can combine regular arguments and with **kwargs 
# but regular argument must come befoer **kwargs

def myfunction(name,**address):
   print("name is ",name)
   print("address is",address["post"],address["pincode"],address["vill"])
  
print(myfunction(name="hritik", post="powakhali",pincode="855108",vill="fulbari"))

# we cna also use *args and **kwargs in same function 

# the order must be - regular parameter, *args, **kwargs

def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")


# * and ** can also use when calling a function to unpack (expend ) a list or dictionary into seprate arguments 

# unpacking list with * 

def my_function(a,b,c):
   return a+b+c
numbers=[1,34,52]
result=my_function(*numbers) # same as myfunction(1,2,4)

print(result)


# same to unpack dictionary we can use **

def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")

# scope 
# a variable created inside a function called local scope and it will only accessable inside the scope 

# but the local variable will accesable in a function inside the function

def my_function():
   x=100
   def my_function2():
      print(x) # here we are accessing the variable inside a function of function
   my_function2
my_function() 


# a variable created outside the function but inside the python code called a global variable and can be used by anyone 

x=200
def my_function():
   print(x) # here we are accessing inside the function
my_function()

print(x) # accessing outside function


# variable namina
# if we create local and gloabal variable with same name pythion will treat them seprately , the local variable will avaliabel inside the functio  and the global will accessable outside the function 

x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)


# global keyword

# if you are stuck in a local variable and you have tp creeate a global variable you can use global keyword to create global variable
def myfunc():
  global x
  x = 300

myfunc()

print(x)

# Also, use the global keyword if you want to make a change to a global variable inside a function.


# nonlocal keyword 
# if you use nonlocal keyword, the variable will belong to the outer funtion not the imediate function 

def myFunction():
   x=100
   def mySecondFUnction():
      nonlocal x  # this is a  non lcoal function means it belongs to the outer function( myFunction) not the secnond function
      x=200
   mySecondFUnction()
   return x
print(x)






# The LEGB Rule
# Python follows the LEGB rule when looking up variable names, and searches for them in this order:

# Local - Inside the current function
# Enclosing - Inside enclosing functions (from inner to outer)
# Global - At the top level of the module
# Built-in - In Python's built-in namespace
# Example
# Understanding the LEGB rule:

x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)


# a decorator is a function which add extra functionalities to another function without changing its original code
# decorators let you add extra behaviour to a function, without changing the actual code
# a decorator is a function that takes another function as input and returns a new function


# define the decorators first then apply it @decorator_name as input above the function

def changeCase(func):
  def innerFunction():
    return func().upper()
  return innerFunction

@changeCase            # this is how we add decorator 
def myfunction():      #the myfunction function is being decorated with the changecase function'][=]
  return "hello hritik"
print(myfunction)

# a decorator can be called multiple times. Just pace the decorator above the function you want to decorate 

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())


# When you call:

print(myfunction())

# you're actually calling:

# print(myinner())

# what  is a wrapper function 
def myinner():
    return func().upper()

# here myinnder function is wrapper function
# it wraps around the original function and adds extra behaviour 

# myfunction()
#     ↓
# myinner()
#     ↓
# func()
#     ↓
# "Hello Sally"
#     ↓
# .upper()
#     ↓
# "HELLO SALLY"

# Decorator - a function that takes another function as input ,adds extra functionality and returns the modified function 
# wrapper class- The inner function inside a decorator that actually executes the original function and extra behaviour 




# arguments in decorator function
# function that requires argument can also be decorated, just make sure you have to pass the argumetns to the wrapper function 


def changecase(func):
  def innerFUnc(x):
    print("befre calling chagnecase",x)
    return func().upper()
    print("after changecase ")
  return innerFUnc

@changeCase
def myFunction(name):
  return name

# *args and **kwargs 
# some time the decorator function have no control over the argument passed from the decorator function 
# to solve this we can use *args and **kwargs function to wrapper function so the wrapper function can accept any number of arguments and pass them to the decorator function 


def changecase(func):
  def innerfunct(*args,**kwargs):
    return func(*args,**kwargs).upper()
  return innerfunct

@changeCase 
def myFunction(name):
  return name
print(myFunction)


# Decorators with arguments 
# Decortators can accept theie own arguments by adding another wrapper clevel

def casechange(n):
  def casechaange(func):
    def innerfunction():
      if n==1:
        a=func.lower()
      else:
        a=func.upper()
      return a
    return myinner
  return changeCase


        
# we can also use multiple decorators 
# we can use multiple decoratrs into same function this is done by placing the decorator call on top of each other 
# Decorators are called in the reverse order, starting with the one closest to the function 
  
# One decorator for upper case, and one for adding a greeting:

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())

# preserving metadata 
# function in python has metadata that can be accessed using the __name__ and __doc__ attribute

# Normmally a function's name cab be returned using __name__

def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

# when a function is decorated the metsdata of the original function is lost 

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)   # here the output will be innerFunction 


# To fix this, Python has a built-in function called functools.wraps that can be used to preserve the original function's name and docstring.

# Import functools.wraps to preserve the original function name and docstring.

import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)


# lambda function 
# a lambda function can take any number of argument in a small anonymous  function 
# a lambda function can take any nuber if arguments but can have only one expression 

# syntax= lambda argumrnts :expression

# the expression is executed and the result is returned 

# Add 10 to argument a, and return the result:

x= lambda a:a+10

print(x(5)) # we are passing 5 to the function 

# Multiply argument a with argument b and return the result:

x= lambda a,b:a*b
print(x(2,5))

# multiple argimetns 

lamdafunction=lambda a,b,c,d:a+b+c+d
print(lamdafunction(1,2,3,4))

# we can use lambda function inside a function
def myfunc(n):
  return lambda a : a * n


def myfunction(n):
  return lambda a:a*n
dublethenumber=my_function(2)
print(dublethenumber(11))



# use the same function definition to make both functions, in the same program:

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


# Use lambda functions when an anonymous function is required for a short period of time.

# Lambada functions are commonly used with build in functiuon like map(),filter(), and sorted().

# Using map() function applies to every item in an iterable:

numbers=[1,2,3,4,5]
doubles=list(map(lambda x:x*2 , numbers))   # 
print(doubles)   

# filter 
# the filter() function creates a list of items for which a function returns True:

# filter out odd numbers form a list 

odds=list(filter(lambda x:x%2!=0,numbers))
print(odds)

# using lambda with sorted()
# the sorted function can be use to custom sorting 

# sort a list of tuples by the second element '

name=[("hitik",4),("kumart",2),("mahto",1)]
sorted_names=sorted(name,key=lambda x:x[1])
print(sorted_names)

# Fibonacci Sequence
# The Fibonacci sequence is a classic example where each number is the sum of the two preceding ones. The sequence starts with 0 and 1:

# 0, 1, 1, 2, 3, 5, 8, 13, ...

# The sequence continues indefinitely, with each number being the sum of the two preceding ones.

# We can use recursion to find a specific number in the sequence:

# Example
# Find the 7th number in the Fibonacci sequence:

def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))
# Recursion with Lists
# Recursion can be used to process lists by handling one element at a time:

# Example
# Calculate the sum of all elements in a list:

def sum_list(numbers):
  if len(numbers) == 0:
    return 0
  else:
    return numbers[0] + sum_list(numbers[1:])

my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))
# Example
# Find the maximum value in a list:

def find_max(numbers):
  if len(numbers) == 1:
    return numbers[0]
  else:
    max_of_rest = find_max(numbers[1:])
    return numbers[0] if numbers[0] > max_of_rest else max_of_rest

my_list = [3, 7, 2, 9, 1]
print(find_max(my_list))

# Recursion Depth Limit
# Python has a limit on how deep recursion can go. The default limit is usually around 1000 recursive calls.

# Example
# Check the recursion limit:

import sys
print(sys.getrecursionlimit())
# If you need deeper recursion, you can increase the limit, but be careful as this can cause crashes:

# Example
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

# Generator function that can pause and resume their execution 

# when a generator funciton is called, it returns a generator object, which is an iterator.

# the code inside the generator is not executed yet is only compiled. The function only executes when we iterate over the generator 

def myGEnerator():
  yield 1   # insted of using return generator use the yield keyword 
  yield 2
  yield 3
for value in myGEnerator():
  print(value)

# it allow user to iterate over the data without storing the dataset into memory 


# when yield is encountered the function state is saved, and the value is returned. The next time the generator is called, it continues from where it left off

def count_upto_n(n):
  count=1
  while count<=n:
    yield count    # insted of return we use yield  # here yield is encountered so the state of the ducntion wil be saved 
    count+=1
for num in count_upto_n(5):
  print(num)

# unlike return as which terminate the function ,
# yield pauses it and can be called multiple times.


# generators saves memory because it generates value on the fly insted of storing everything in the memory 
# so is is ueful for large dataset 

# using next() with generators 

# we can use next() to iterate through the generator

def simple_gen():
  yield "email"
  yield "phome"
  yield "hello"

gen=simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))    # this will raise StopIteration exception
 
  # when there is no more value left the generator raise a StopIteration exception

# generator expression 
# we can create generator using generators expression with parenthesis insted of square brackets


Generator Expressions
Similar to list comprehensions, you can create generators using generator expressions with parentheses instead of square brackets:

Example
List comprehension vs generator expression:

# List comprehension - creates a list
list_comp = [x * x for x in range(5)]
print(list_comp)

# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))
# Example
# Using a generator expression with sum:

# Calculate sum of squares without creating a list
total = sum(x * x for x in range(10))
print(total)
# Fibonacci Sequence Generator
# Generators can be used to create the Fibonacci sequence.

# It can continue generating values indefinitely, without running out of memory:

# Example
# Generate 100 Fibonacci numbers:

def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

# Get first 100 Fibonacci numbers
gen = fibonacci()
for _ in range(100):
  print(next(gen))
# Generator Methods
# Generators have special methods for advanced control:

# send() Method
# The send() method allows you to send a value to the generator:

# Example
def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello")
gen.send("World")
# close() Method
# The close() method stops the generator:

#Example
def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()
