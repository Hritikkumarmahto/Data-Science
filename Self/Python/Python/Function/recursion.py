# when a function call iteself repeatedly called a recursion 

def show(n):
  if n==0:  # this is the base case 
    return  # will return to previous 
  print(n)  # print the number 
  show(n-1) # calling the function again with n-1 
show(5)

# facorial using recursion 

def factorail(n):
  if(n==1 or n==0):
    return 1
  else:
    return n*factorail(n-1)
  
print(factorail(5))

# calculate sum using recursion

def recurse_summ(n):

  if n==0:
    return
  return recurse_summ(n-1)+n
  
printsum=recurse_summ(5)
print(printsum)