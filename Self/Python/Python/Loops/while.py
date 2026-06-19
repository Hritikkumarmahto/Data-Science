# the while loop executes the set of statements as long as a condition is true



# i=1
# while i<=10:  # here i is called iterator whihc iterates from the starting to end 
#   print("hello")
#   i+=1   # remember to increase the variable i else the loop will contiye to  



# to print upto 100

# while i<=100:
#   print(i)
#   i+=1

num=1
n=10
while num<=10:
  print("here is thei",num*n)
  num+=1


# to print the length of the list 
list=[1,2,3,4,19]

lenght=len(list)-1
j=0

while j<=lenght:
  print(list[j])
  j+=1


# serch the   number x in a tuple using 

tuple=(1,3,4,2,45,"hritik")

t=0
size=len(tuple)

# while t<size:
#   if tuple[t]==45:
#     print("found at index",t)
#   t+=1

# Break - break keyword is use to termninate the loop when encountered

while t<size:
  print(tuple[t])
  if tuple[t]==3:
    break  # this will stop the program when it will find 3 in the tuple 
  t+=1


# continue  - terminates execution in the current iteration and continues execution of the loop wth the next iteration

while t<size:
  if tuple[t]==3:
    t+=1
    continue  # this will escape prining 3 continuing printing rest basically continue breaks the code written below it and continuing next 
  print(t)
  t+=1
  