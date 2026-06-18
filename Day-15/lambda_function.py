
odd_eve =lambda x: "even" if x%2==0 else "odd"
a=int(input("enter the number "))
res=odd_eve(a)
print(res)

verify_use= lambda age: "eligible" if age>=18 else  "not eligible"
age_Input=int(input("enter age"))
res_age=verify_use(age_Input)
print(res_age)

# Multiple operations 

master_function=lambda a,b:[a+b, a-b,a*b, a//b , a%b]
numbers=master_function(12,34)
print(numbers)

# Fileter function 

def check_marks(marks):
  return marks>=30

marks_list=[25,4512,6,2,12324,6,6,5,32232]
res=filter(check_marks,marks_list)
print(list(res))


# using lambda fubnction 
marks_list=[25,4512,6,2,12324,6,6,5,32232]
res=filter(lambda x: x>=30 ,marks_list)
print(list(res))


# writing whole code in one line 
# using lambda fubnction 
print(list(filter(lambda x: x>=30 ,[25,45,6,34,12324,6,6,2332,32,32]))) # passign list in the same line 
