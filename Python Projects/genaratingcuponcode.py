# generate 10 cupon code 1-4 alphabet and 4-8 digit
# eg: asdd1234


import random

def generate_cupon():
  letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  numbers = "0123456789"

  chars = random.choices(letters, k=4) + random.choices(numbers, k=4)

  coupon = ''.join(chars)

  return coupon

for i in range(1,10):
  print(generate_cupon())

