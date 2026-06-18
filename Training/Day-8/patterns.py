rows = int(input("enter a number "))

# for i in range(rows):
#     for j in range(rows):
#         if j == 0 or j == rows-1 or i == rows/2:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


for i in range(rows):
    for j in range(rows):
        if j == 0 or i == 0 or i == rows // 2 or i == rows - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

