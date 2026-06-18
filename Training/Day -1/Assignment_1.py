# Basic Variable Swapping 
# 1. Switch values of two integers 

# num1=int(input())
# num2=int(input())


# print(f"Before swaping n1 - {num1} n2 - {num2}")


# temp=num1
# num1=num2
# num2=temp

# print(f"after swaping n1 - {num1} n2 - {num2}")


# 2. Switch values of two strings (characters) 

# str1=str(input())
# str2=str(input())

# print(f"Before swaping str1 {str1} str2 {str2}")

# strtemp=str1
# str1=str2
# str2=strtemp

# print(f"after swaping str1 {str1} str2 {str2}")

# 3. Switch one string value with one integer value 

# str1=str(input())
# num1=int(input())

# print(f"before swap str {str1} and num is {num1}")


# strtoint =int(num1)
# num1=str(str1)
# str=strtoint

# print (f" after swaping str {str} and num is {num1}")


# 5. Update balance after deposit 

# current_balance=int(input("Enter your current balance:- "))
# deposit_balance=int(input("Enter your deposit ammount:- "))


# new_balance=current_balance+deposit_balance
# print(f"Your ammount has deposit sucessfully ")
# print(f"Your current balace is {new_balance}")

# 6. Update balance after withdrawal 

#current_balance=int(input("Enter your current balance:- "))
# withdrawal_ammount=int(input("Enter your withdrawal ammount:- "))


# new_balance=current_balance -withdrawal_ammount
# print(f"Your ammount has withdrawal sucessfully ")
# print(f"Your current balace is {new_balance}")


# 7. Increase shopping cart items by 3 

# Items_in_cart=int(input("entr how many items are in the cart currently - "))

# afterAdding=int(input("How many more items you want to enter in your card - "))

# print(f"your items are added sucessfully , Current total carts are {Items_in_cart+afterAdding}")



# #Apply a 20% discount to a price 

# price=int(input("enter the price of the item - "))
# discount=int(input("enter total discount in the product in % - "))

# discounted_price= price/100*discount

# price_after_discount= price-discounted_price

# print(f"Price after discount = {price_after_discount}")


# Academic Calculations 
# 9. Calculate student percentage

# total_marks=int(input("Enter total marks - "))
# marks_obtain=int(input("enter the marks you got - "))

# percentage=marks_obtain/total_marks*100

# print(f" total percentage is {percentage}")

# 10. Calculate total and average of 4 subjects 

# sub1= int(input("enter the marks of 1st subject - "))
# sub2= int(input("enter the marks of 2nd subject - "))
# sub3= int(input("enter the marks of 3rd subject - "))
# sub4= int(input("enter the marks of 4th subject - "))


# total=sub1+sub2+sub3+sub4
# average=total/4

# print(f"total average of the numbers are {average}")


# num1=int(input("enter number 1"))
# num2=int(input("enter number 2"))
# num3=int(input("enter number 3"))

# average = num1+num2+num2/3

# Finance & Business Calculations 
# 12. Calculate profit or loss percentage 

# cost_price=int(input("Enter the cost of the item - "))
# selling_price=int(input("enter the sellig price of the item "))

# profit=selling_price-cost_price

# print(f"total = {profit}")

# #  Calculate simple interest 

# principle=int(input("Enter principle ammount - "))
# rate=int(input("enter rate of intrest - "))
# time=int(input("enter total duration - "))

# simple_intrest= principle*rate*time/100
# compound_intrest = principle * (1 + rate / 12) ** (12 * time)

# print(f"Simple intrest is {simple_intrest}")
# print(f"compound intrest is {compound_intrest}")

# #15. Calculate tax on income 

# income=int(input("enter you income "))
# tax_rate=int(input("enter TAX rate"))

# ammount_after_tax=(income*tax_rate)/100
# print(f"Ammount after tax deduction is {ammount_after_tax}")

# #16. Calculate percentage increase or decrease 

# initial_value=int(input("enter initial value "))
# final_value=int(input("enter final value "))

# percentage_change=((final_value-initial_value)/initial_value)*100

# print(f"percentage_change {percentage_change}")
# print("")


# #17. Convert boolean to integer 

# boolen_value=True
# print(f"after conversion {int(boolen_value)}")


# Convert float to string

float_value=float(input("Enter float value "))

print(f"after conversion {str(float_value)}")

# Celcious to feranhite

temp_in_cel=int(input("Enter the tempreture "))
