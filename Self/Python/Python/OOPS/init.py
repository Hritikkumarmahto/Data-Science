# __init__ method 
# All class have build in mathod called init which is always executed when the class is being initiated.
# The init method is use to assign values to object properties, or to perform iperations that are necessary when the object is being created 

# basically init function is called constructor 
class person:
  def __init__(self, name,age):  # self should be the first argument in init function because if refers to the object whihc is being created
    self.names=name
    self.ages=age
    print(self)   # printing self will print location 

p1=person("Hritik",23)    # here p1 is refering to self 
print(p1)              # both self and p1 objects liocation will be same because sef is refering the object crearion
print(p1.ages)
print(p1.names)

p2=person("mahto",98)
print(p2)       # now for p2 the locaiton will also same 
print(p2.names) 
print(p2.ages)

# the __intit__method will called automatically every time when the class is being use to create new object 
# if we dont creare constructor python will automatically create a constructor 
# also the self can be name anything 
# when ever we create any object the constructor is called 

# Class and instance attribute
class student:
  college="CU"

  def __init__(self,name,marks):
    self.student_name=name
    self.student_marks=marks

s1=student("hritik",23)

print(student.college)    # this is also how we can print the college name from student class this is called class attribute
print(s1.college)   # this will also print the college name this is called object attribute
print(s1.student_name,s1.student_marks)
# object attribut > class attributes , attributes are nothing just variables of the class


# methods are functions that  belongs to object 

class student:
  def __init__(self,name,marks,age,marks_suject):
    self.student_name=name
    self.student_marks=marks
    self.student_age=age
    self.markss=marks_suject

  def get_name(self):
    print(self.student_name)
  
  def get_marks(self):
    print(self.student_marks)
  
  def get_age(self):
    print(self.student_age)

name=input("enter student name ")
marks=input("enter student marks ")
age=input("enter student age ")
subject_marks=[87,97,563,423]

s1=student(name,marks,age)
s1.get_name()
s1.get_marks()
s1.get_age()



# static methods 
# method that dont use the self parameter work at class level

class studnet: 
  @staticmethod   # decorator 
  def college():
    print("abc college ")




# Abstraction - Hiding the details of a class and showing the essential features to the user.
# Encapsulation - Wrapping data into a sigle unit 