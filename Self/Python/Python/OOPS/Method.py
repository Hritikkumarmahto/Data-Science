# del keyword is use to delete the object
# __ is use to make the attribute private


class studetn:
  def __hello(self):
    print("hello world")
  def welcome(self):
    self.__hello()
s1=studetn()
print(s1.welcome())

# when one class derived the properties and method of another class(parent/base )

class student:
  def student_age(self):
    print("23 ")
  def student_class(self):
    print("student class is BE")

class details(student):
  def __init__(self,name):
    self.name=name
  def print_name(self):
    return self.name
  
d=details("Hritik")
d.print_name()
d.student_age()
d.student_class()


# Types of Inheritance 
# 1. Single Inheritance 

class student:
  def student_age(self):
    print("23 ")
  def student_class(self):
    print("student class is BE")

class details(student):
  def __init__(self,name):
    self.name=name
  def print_name(self):
    return self.name
  
d=details("Hritik")
d.print_name()
d.student_age()
d.student_class()

# 2. Multilevel Inheritance
class student:
  def student_age(self):
    print("23 ")
  def student_class(self):
    print("student class is BE")

class details(student):
  def __init__(self,name):
    self.name=name
  def print_name(self):
    return self.name
  
class admission(details):
  def tookAdmission(self,status):
    self.status=status
   
  

a=admission("Yes He is ")
a.tookAdmission("Yes")
a.print_name()
a.student_age()
a.student_class() 
print(a.status)


# 3. Multiple Inheritance

class A:
  def printA(self):
   print("hello this is calss A")
class B:
  def PrintB(self):
    print("This is class B")
class C(A,B):
  def PrintC(self):
    print("This is calss c")

c1=C()
c1.PrintC()
c1.PrintB()
c1.printA()

# Super Method() 
# super method is a method which is use to access the method of the parent class

# class A:
#     def __init__(self, Alphabet):
#         self.Alphabet = Alphabet

#     def printA(self):
#         print("Hello this is class A")


# class B:
#     def PrintB(self):
#         print("This is class B")


# class C(A, B):
#     def __init__(self, Alphabet):
#         super().__init__(Alphabet)

#     def PrintC(self):
#         print("This is class C")


# c1 = C("YES")

# c1.printA()
# c1.PrintB()
# c1.PrintC()

# print(c1.Alphabet)

# class method
# A method that belongs to class itself not an individual object 
# Normal method uses self( object )

class student:
  college="CU"

  @classmethod
  def showCollege(cls):
    print(cls.college)

student.showCollege()



# property method 
# property let you call the methods like a variable 

class student:
  
  @property
  def callName(self):
    return "Hritik"
  
s=student()

print(s.callName)   # here is we are calling method like a variable notice we havent use ()


class student:
  
  def __init__(self):
    self._marks=0
  
  @property        # this is use to read  # updated read   # latest value 
  def marks(self):
    return self._marks
  
  @marks.setter     # this is use to write  automatically updates and return updated variable value
  def marks(self,value):
    if 1<= value <=100:
      self._marks=value
    else:
      print("Invaied marks")

s=student()

s.marks=23
print(s.marks)

s.marks=232

# Polymorphism 


# when same method works dirrently with diffrent object

class dog:
  def sound(self):
    print( "bark") 
  

class cat:
  def sound(self):
    print("meow")
  
d=dog()
c=cat()

d.sound()    # same method are giving difffrent output x  
c.sound()



odd_eve =lambda x: "even" if x%2==0 else "odd"
a=int(input("enter the number "))
res=odd_eve(a)
print(res)

verify_use= lambda age: "eligible" if age>=18 else  
age_Input=int(input("enter age"))
res_age=verify_use(age_Input)
print(res_age)

# Multiple operations 

master_function=lambda a,b:[a+b, a-b,a*b, a//b , a%b]
numbers=master_function(12,34)
print(numbers)