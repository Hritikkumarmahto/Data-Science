# str="hello world"

# print(str[1:9])

# dtr2="Hritik Kumar Mahto"

# print(dtr2[4:8])

# str2="hritik"
# print(str2[-5:-2])

str3="Python is a high level programing language."

# endswith
print(str3.endswith('e'))  # return true if the string ends with the charachter
print(str3.endswith('programing ')) # retrun falsew because the string is not ending wiht the word 
print(str3.endswith("."))



# capitalize()

str4=str3.capitalize()  #convert the first letter of the sentence into capital letter
print(str4) 

str2="""python is programing . 
this is high level
      """
print(str2.capitalize())  # here is line break but not capitalizing the second sentence 



# Replace()

string5="This is example of replace ment"  # this replace the charachter with the other character given in the function
print(string5.replace("t","o"))
print(string5.replace("a","x"))


# Find()

string6="this is what you are looking for "  # retrun the first index of ther searched word / occurence

print(string6.find("what"))
print(string6.find("this"))

# count

print(string6.count("o")) # counts ther occurence of the substr in the string
print(string6.find("is"))
print(string6.find("look"))