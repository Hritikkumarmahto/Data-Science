# ==========================================
# 1. Switch values of two integers
# ==========================================
n1 = int(input("Enter first integer: "))
n2 = int(input("Enter second integer: "))

n1, n2 = n2, n1

print("n1 =", n1)
print("n2 =", n2)

# ==========================================
# 2. Switch values of two strings
# ==========================================
char1 = input("Enter first string: ")
char2 = input("Enter second string: ")

char1, char2 = char2, char1

print("char1 =", char1)
print("char2 =", char2)

# ==========================================
# 3. Switch one string value with one integer value
# ==========================================
n1 = int(input("Enter integer value: "))
char2 = input("Enter string value: ")

temp = n1
n1 = char2
char2 = temp

print("n1 =", n1)
print("char2 =", char2)

# ==========================================
# 5. Update balance after deposit
# ==========================================
current_balance = float(input("Enter current balance: "))
deposit_balance = float(input("Enter deposit amount: "))

print("Before Deposit =", current_balance)

current_balance += deposit_balance

print("After Deposit =", current_balance)

# ==========================================
# 6. Update balance after withdrawal
# ==========================================
balance = float(input("Enter balance: "))
withdrawal = float(input("Enter withdrawal amount: "))

balance -= withdrawal

print("Balance after withdrawal =", balance)

# ==========================================
# 7. Increase shopping cart items by 3
# ==========================================
cart_items = int(input("Enter cart items: "))

cart_items += 3

print("Updated cart items =", cart_items)

# ==========================================
# 8. Apply a 20% discount to a price
# ==========================================
price = float(input("Enter price: "))

discounted_price = price - (price * 20 / 100)

print("Price after discount =", discounted_price)

# ==========================================
# 9. Calculate student percentage
# ==========================================
obtain_marks = float(input("Enter obtained marks: "))
out_of = float(input("Enter total marks: "))

percentage = (obtain_marks / out_of) * 100

print("Percentage =", percentage)

# ==========================================
# 10. Calculate total and average of 4 subjects
# ==========================================
s1 = float(input("Enter subject 1 marks: "))
s2 = float(input("Enter subject 2 marks: "))
s3 = float(input("Enter subject 3 marks: "))
s4 = float(input("Enter subject 4 marks: "))

total = s1 + s2 + s3 + s4
average = total / 4

print("Total =", total)
print("Average =", average)

# ==========================================
# 11. Calculate average of 3 numbers
# ==========================================
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

average = (num1 + num2 + num3) / 3

print("Average =", average)

# ==========================================
# 12. Calculate profit or loss percentage
# ==========================================
cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))

if sp > cp:
    profit = sp - cp
    profit_percent = (profit / cp) * 100
    print("Profit Percentage =", profit_percent)
else:
    loss = cp - sp
    loss_percent = (loss / cp) * 100
    print("Loss Percentage =", loss_percent)

# ==========================================
# 13. Calculate simple interest
# ==========================================
principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))

si = (principal * rate * time) / 100

print("Simple Interest =", si)

# ==========================================
# 14. Calculate compound interest
# ==========================================
principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))

amount = principal * ((1 + rate / 100) ** time)
ci = amount - principal

print("Compound Interest =", ci)

# ==========================================
# 15. Calculate tax on income
# ==========================================
income = float(input("Enter income: "))
tax_rate = float(input("Enter tax rate: "))

tax = (income * tax_rate) / 100

print("Tax =", tax)

# ==========================================
# 16. Calculate percentage increase or decrease
# ==========================================
initial_value = float(input("Enter initial value: "))
final_value = float(input("Enter final value: "))

change = ((final_value - initial_value) / initial_value) * 100

print("Percentage Change =", change)

# ==========================================
# 17. Convert boolean to integer
# ==========================================
value = input("Enter True or False: ")

if value.lower() == "true":
    print(int(True))
else:
    print(int(False))

# ==========================================
# 18. Convert float to string
# ==========================================
num = float(input("Enter float value: "))

str_value = str(num)

print("String =", str_value)

# ==========================================
# 19. Convert Celsius to Fahrenheit
# ==========================================
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Fahrenheit =", fahrenheit)

# ==========================================
# 20. Convert Fahrenheit to Celsius
# ==========================================
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9

print("Celsius =", celsius)

# ==========================================
# 21. Convert integer to binary
# ==========================================
num = int(input("Enter integer: "))

print("Binary =", bin(num))

# ==========================================
# 22. Calculate area of a triangle
# ==========================================
base = float(input("Enter base: "))
height = float(input("Enter height: "))

area = 0.5 * base * height

print("Area =", area)

# ==========================================
# 23. Calculate perimeter of a square
# ==========================================
side = float(input("Enter side: "))

perimeter = 4 * side

print("Perimeter =", perimeter)

# ==========================================
# 24. Calculate diameter of a circle
# ==========================================
radius = float(input("Enter radius: "))

diameter = 2 * radius

print("Diameter =", diameter)

# ==========================================
# 25. Calculate volume of a cube
# ==========================================
side = float(input("Enter side: "))

volume = side ** 3

print("Volume =", volume)

# ==========================================
# 26. Calculate surface area of a cuboid
# ==========================================
l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
h = float(input("Enter height: "))

surface_area = 2 * ((l*b) + (b*h) + (l*h))

print("Surface Area =", surface_area)

# ==========================================
# 27. Square of sum (x + y)^2
# ==========================================
x = float(input("Enter x: "))
y = float(input("Enter y: "))

result = (x + y) ** 2

print("Result =", result)

# ==========================================
# 28. x^2 - 4x + 4
# ==========================================
x = float(input("Enter x: "))

result = (x ** 2) - (4 * x) + 4

print("Result =", result)

# ==========================================
# 29. (a + b)(a - b)
# ==========================================
a = float(input("Enter a: "))
b = float(input("Enter b: "))

result = (a + b) * (a - b)

print("Result =", result)

# ==========================================
# 30. a^3 + b^3
# ==========================================
a = float(input("Enter a: "))
b = float(input("Enter b: "))

result = (a ** 3) + (b ** 3)

print("Result =", result)

# ==========================================
# 31. (x - y)^2
# ==========================================
x = float(input("Enter x: "))
y = float(input("Enter y: "))

result = (x - y) ** 2

print("Result =", result)

# ==========================================
# 32. x^3 - y^3
# ==========================================
x = float(input("Enter x: "))
y = float(input("Enter y: "))

result = (x ** 3) - (y ** 3)

print("Result =", result)

# ==========================================
# 33. User Profile Output
# ==========================================
name = input("Enter Name: ")
age = input("Enter Age: ")
city = input("Enter City: ")
hobby = input("Enter Hobby: ")

print(f"Meet {name}, a {age}-year-old enthusiast from {city}.")
print(f"When not busy with daily tasks, {name} loves spending time {hobby}.")
print(f"Life in {city} keeps {name} energetic and curious every single day.")
print(f"With coding as a passion, the future looks creative and inspiring for {name} in the {city} City.")

# ==========================================
# 34. Professional Information
# ==========================================
full_name = input("Enter Full Name: ")
profession = input("Enter Profession: ")
quote = input("Enter Favorite Quote: ")
experience = input("Enter Years of Experience: ")

print("----------------------------------")
print("Name       :", full_name)
print("Profession :", profession)
print("Experience :", experience, "years")
print('Quote      : "' + quote + '"')
print("----------------------------------")

# ==========================================
# 35. Movie Ticket
# ==========================================
movie = input("Enter Movie Name: ")
viewer = input("Enter Viewer Name: ")
seat = input("Enter Seat Number: ")
time = input("Enter Show Time: ")

print("\n🎟 Movie Ticket")
print("------------------------")
print("Movie   :", movie)
print("Name    :", viewer)
print("Seat No :", seat)
print("Time    :", time)
print("Enjoy the show!")
print("------------------------")