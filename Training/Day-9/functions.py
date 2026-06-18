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
 