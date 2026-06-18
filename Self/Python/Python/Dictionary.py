# DIctionary are use to store data balues in key:value pairs 
# these are unordered, mutable( changable) and dont allow duplicate keys 
# there is no index in dictionary


# key : values
# name: "Hritik"
# roll:118

dict={
  "name":"Hritik",
  "Address":"Kishanganj", # string value
  "Pincode":855108,
  "age":23,           # int value
  "marks":99.99,      # float value
  "is_adult":True,     #bollean Vlaue

  "subject":["python","java",11,"c++",2.99]   ,  # list datatype

  "tuples":("programing","sql",4455,"Noida")    # tuples 

  # key cannot be list or tuple
}
print(dict)  # to print whole dict

print(dict["name"]) # to print specific vlaue using the key

print(dict["subject"])

print(dict["tuples"])

# To change the value

dict["address"]="Bihar" # address updared to bihar 

print(dict["address"])

# can alos add key : value pair in already present dictonary

dict["surname"]="mahto" # added in the last of the dictionary 

print(dict["surname"])



# we can also creatre null dictniory

null_dict={}
null_dict["name"]="Hritik Kumar Mahto"  # added value in null dictionary

print(null_dict["name"])






# Nested Dictionary

# we can also create a value of key to dictionary 

nested_dict = {
  "name":"hritik",
  "details":{  # here we have created a  nesteed dictniory mens stored multiple values into key
    "age":23,
    "address":"Kishanganj",
    "education":"be-cse"
  }
}
print(nested_dict)

print(nested_dict["details"]["address"])  # to acccess the values of the dictionary inside the nested dictionary




#------------------------------------------------------------------------

# Methods() in Dictionary


# 1. keys() -  return all keys 

print(dict.keys()) # this will only print the keys inside the dictniory 


# 2 . values() - this will return the vlaues inside the dictionary

print(dict.values())

pairs=list()


# 3. items() - return all key value pairs as tuple 

print(dict.items()) # return all key values ad tuple 

# 4. get("key") # return the key according to value

print(dict.get("keys"))   # if we dint use get we will get en error saying none



# 5. update()
 # in thsi we can pass new dictionary or add new key value pairs inside the dictionary


               
dict.update({"city":"Kishanganj"}) # here is how we can add key values pair in a dictionary
print(dict)


dict3={
  "city":"Kishanganj",
  "pincode":855108
}

dict.update(dict3) # here we are insering the whole dictionary 

print(dict)


# practice 

dictonary9={
  "cat":"a pet animal",
  "lion":"a wildaminal",
  "horse":[" a fast animal","also can  be multicolor"] # this is a list type whihc is stored in a dictionary 


}
print(dictonary9)
print(dictonary9["cat"])
print(dictonary9["horse"])

sub1=input("enter the subject name ")
sub1_marks=int(input("enter sub 1 marks "))
sub2=input("enter the sub2 name")
sub2_marks=int(input("enter marks of sub2"))
sub3=input("ente the thirs sub name")
sub3_marks=int(input("enter sub 1 marks"))

dicrionary_marks={
  sub1:sub1_marks,
  sub2:sub2_marks,
  sub3:sub3_marks

}
print(dicrionary_marks)

  