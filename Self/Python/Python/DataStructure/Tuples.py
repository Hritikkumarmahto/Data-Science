# this is a built in data tyoe that let us create immutable sequence of values same like string 


tuple1=(1,2,3,4,45,)
print(tuple1)

#tuple1[0]=9 # this is not allowed in tuple because tuple is immutable 

# but we can access as the similar wau as we use to access the data in list 

print(tuple1[0])
print(tuple1[4])


tuple2=(1,) # we have to add comma if we want to make it behve like tuple if not then it will behave like int for single element 


# ---------------------------------------------------
# in tuple SLICING works same as it woeks in string and list

print(tuple1[1:4])


#-------------------------------------------------------------

# Tuple Methods

# 1. index(el) 

tuple2=(1,2,3,3,3,1,12,12,12)
print(tuple2.index(3)) # retun the rfirst occurence of the element

# 2. count() 
print(tuple2.count(12)) # counts the total number of element in the tuple 



a1=input("entet first ")
a2=input("enter senbcod")
a3=int(input("enter number"))

list=[a1,a2,a3]
print(list)


list1=list.copy()
list1.reverse()

if list1==list:
  print("palindrom")
else:
  print("not a palindrom")
    