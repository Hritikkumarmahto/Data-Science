# # Wap to take start point and end poitn by user and only print all even numbers

# num1=int(input("Enter first number "))
# num2=int(input("Enter second number "))

# while num1<=num2:
#   if num1%2==0:
#     print(num1)
#   num1+=1


string1=input("enter the string - ")
size=len(string1)
i=0

while i<size:
  print(string1[i], end=" ")
  i+=1

j=size-1
print("reversed ")
while j>=0: 
  print(string1[j],end=" ")
  j-=1
