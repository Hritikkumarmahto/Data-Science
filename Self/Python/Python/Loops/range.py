# The range function returns an immutable sequence of numbers, commonly used for looping a specific number of times 
# This set of numbers has its own data type called range 
# range (start, stop, steps)

# the start argument can be bydafault 0 if we wnt give the start and only give the stop range(10)

# range (10) one argument - will considet that as stop 
# range (1,10) two argument - will consider that start and stop  and stpes will be 1

# range are often used in for loops to iterate over a sequence of numbers 

for i in range(10): # iterate over a sequence of numbers
  print(i)


# like the otehr sequence the range can also be slice to extract subsequence 

r=range(10)
print(r[2])
print(r[:3])   # this will print 0 to 3 

# membership testing with the in operator.

r= range(10,99,1)
print(2 in r)  # false when the number is not present 
print(34 in r) # true when the number is present 

# len() we use the len function to get the number of element present in the range 

r=range(0,99)
print(len(r))   # total no of elements 



