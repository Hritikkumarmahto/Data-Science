# for loop is used for sequential traversal. for traversing list, tuple, strings etc
# to traverse a list we use for loop and to change or manipulate the value we use while loop 
# for loop in list

nums=[1,2,3,4,5,98,5,43]

for i in nums:
  print(i)     # this will print values present in each index not the 

print("*** tuple *****")
# for loop in tuple

tup=(3,4,5,65,6,6)
for t in tup:
  print(t)


print("*** for loop with else *****")


# for loop with else 
# we can also use for loop with else so it will print after traversing 

for t in tup:
  print(t)
else:
  print(" not printint")  # here is how we can use else inside for loop and this will run after completing for loop 


# else will not work if we use break condition 

# rane function - range function returns a sequence of numbers, starting from 0 by default and increments by 1 by default , and stops before specified number.

# range( start, end, steps) - this is how range function works 

# range doesnt include ending number 


print ( " **** Range function ***** ")

for element in range(10):   # giving a specified number where to reach 
  print(element*2)

print("*****giving values of start and stop ****** ")

for element in range(1,21): 
  print(element)


print("**** giving  steps also ****** ")

for i in range( 1,20,19):  # will include 1 but exclude 19
  print(i)


print("printing 100 to 1")
for i in range( 100, 0, -1):  # step size can be negative also if we want it into decreasing order
  print(i)



# PASS statement
# pass is a null statement that does nothing. it is used as a placeholder for future code 

for element in range(10):
  pass

# we can also use pass inside if else condition if we dont want to execute the condition


n = int(input("ernter a number "))
sum=0
i=0
while i<=n:
  sum+=i
  i+=1
print("sum is ",sum)

factorialx=1
for fact in range(1,n):
  factorialx*=fact
print(factorialx)
