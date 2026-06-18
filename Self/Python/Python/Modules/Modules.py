# consider a module same  as a code library
# A file containing set of function you want to incldue in your application

# we can use the module code by importing the  file using import statement 
import myModule   # this is the another file we are importig usig import 

myModule.greeting("Hritik")

# the module can contain all types of variables and data type 
a=myModule.person1(["age"])
print(a)

# there are many built in module we can just import and use them 
# eg importing platfrom 

import platform

x = platform.system()
print(x)

# Note: The dir() function can be used on all modules, also the ones you create yourself.


from myModule import person1
# When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]
