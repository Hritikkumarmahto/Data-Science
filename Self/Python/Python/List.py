# LIst is a build in data type that is use to store set of values

marks= [25.09,45,23,23]
print(marks)
print(type(list))

# it can store the values of diffrent data types ( int, float, string)

address=["Kishnganj","Bihar",855108]

print(address[1])
print(address[2])

print(len(address)) # returns the sise of list 


# string are immutable - Means you cannot change the value or index of string 
# List are mutable = we can change the index values 

list2=[ "Hritik" ,"this", "side" ]
print(list2)
list2[1]="Mahto"
print(list2)

# ------------------------------------------------------------------------------

# List slicing is also possible in list 

# Similar to string slicing 

# List_name(strting_index, Ending_Index)

print(list2[1:2]) # will slice the first and pring the rest 

print(list2[2:])

print(list2[:-1])

# ------------------------------------------------------------------------------
# Methods in list -- Function in list

list3=["hritik",1,"mahto",0]

# append() 


list3.append(855108)  # will add the element at the end of the list
print(list3)


# ------------------------------------------------------------------------------

# sort() 


list4=[1,4,2,1,4,0,3,-11,98,-88]
print("before sorting",list4)

list4.sort() # sort the list in ascending order but the list should contain similar data type
print("after sorting ")
print(list4)



list5 = ["hritik", "kumar", "mahto",'a','b','c'] ## this will also get sort because this containe same string type

list5.sort()
print(list5)

# ------------------------------------------------------------------------------


# sort(reverse=True) 

list5.sort(reverse=True) # this is will sort the list in descending order

print(list5)


list5.sort(reverse=False)
print(list5)

# ------------------------------------------------------------------------------

# reverse()

list5.reverse()
print(list5)

# ------------------------------------------------------------------------------


# insert()

list5.insert(2,"kishanganj")  # will insert the element at the index given 
print(list5)

list5.insert(3,"Bihar")  # will insert the element at the index given 

print(list5)

# ------------------------------------------------------------------------------

# remove()

list5.remove("hritik") # remove the first occurence of the element whenwver it will aper 

print(list5)

list5.append("hritik")

list5.insert(3,"hritik")

print(list5)

list5.remove("hritik")  # removed the first occurence of the element 
print(list5)


# ------------------------------------------------------------------------------

# pop()

list5.pop(3) # removes the element at the index (index)
print(list5)
 

# sort

list5.sort(reverse=True)
print(list5)

list5.index('a',3)  # to check if the elemetn came after 3rd index 
