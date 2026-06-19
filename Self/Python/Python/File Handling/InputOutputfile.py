# # Open read and close file 

# # cahracter & meaning

# # 'r' - open for reading (default)
# # 'w' - open for writing, truncating the file first
# # 'x' - create a new file and open it for writing 
# # 'a' - open for writing, appending to the end of the file if exist 
# # 'b' - binary mode 
# # 't' - Text mode (default)
# # '+' - open a disk file for updating ( reading and writing )


# f=open("Self\Python\Python\demo.txt","r")
# data=f.read()
# print(data)

# data=f.read(5)
# print(data)  # this will read first 5 character of the file 

# line1=f.readline()
# print(line1)   # this will print first line of the file 

# line2=f.read()
# print(line2)   #this will print the line 2 because we are  

# # if we are reading the file first then readline will not print anything 

# print(type(data))
# f.close()   # always close the file 


# writing to a file using w will ovveride 

# f=open("Self\Python\Python\demo.txt",'w')
# f.write("I am from kishanganj Bihar ")  # this overrides the entire file 
# f.close()

# append using a - add data to next line 

f=open("Self\Python\Python\demo.txt",'a')
f.write("This is my area and nobedy intrupts here ")     # adds content in the same file and same line
f.write("\n Get lost ")    # this will add the text in the next line because we are using \n
f.close()

# if we use w or a for writig and file dont exist then python automatically creates that file for us 

f=open("data.txt",'w')
f.close()


# using r+ we can read and write at the same time the stream will positioned at the begining of the file 
f=open("Self\Python\Python\demo.txt",'r+')   # no truncate
f.write("this is hritik")  # this will ovverride the existing first line  
print(f.read())


# using w+ we can read and write 

f=open("Self\Python\Python\demo.txt",'w+')   # truncate
f.write("this is hritik")  # this will ovverride the existing first line  
print(f.read())

# using a+ we can read and write 

f=open("Self\Python\Python\demo.txt",'a+')   # truncate
f.write("this is hritik")  # this will read and append at the file so thte pointer will be at the end 
print(f.read())



# with syntax

