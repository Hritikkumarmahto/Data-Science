# str1="Hritik Is a good boy"
# str2=""
# for i in range(len(str1)):
#   if str1[i] in "aeiouAEIOU":
#     print(i,str1[i])



# b=[1,2,3,4,5.12,15]
# res=[val for val in b if val>10 ]
# print(res)

# list2=[i for i in range(10)]
# print(list2)

# c=[(x,y) for x in range(10) for y in range(10)]
# print(c)

# list1=[1,2,3,4,56]
# even=["even" if i%2==0 else "odd" for i in list1 ]
# print(list1)

# string1="this is 1 3 python 13231"

# res= [i for i in string1 if i.isdigit() ]
# print(res)
# res=[i for i  in string1 if i.isdigit()]


# list1=[1,2,3,4,5]
# list2=[]
# for i in list1:
#   if i%2==0:
#     list2.append(f"{i},even")
#   else:
#     list2.append(f"{i},odd")

# print(list2)


# list1=["python programing"]
# list2=[]

# for i in list1:
#   words=i.split()
#   words.reverse()
#   list2.append(" ".join(words))

# print(list2)

# lsit1=["python programing"]
# list2=[]

# for i in list1:
#   words=i.split()
#   words.reverse()
#   list2.append("".join(words))
# print(list2)


# for i in list1:
#   words=i.split()
#   words.reverse()
#   list2.append("".join(words))

# print(list2)


list1=["python programing"]

# s=list1[0]
# chars=list1(s)

# temp=chars[0]
# chars[0]=chars[-1]
# chars[-1]=chars[0]

# res="".join(chars)

# print(res)


for i in list1:
  
  res=""
  for j in i:
    if j !="h" and j!= "g":
      res+=j

print(res)


i=0
while i <len(list1):
  res=""
  j=0
  while j<(len(list1[i])):
    if list1[i][j]!="h" and list1[i][j]!="g":
      res+=list1[i][j]

    j+=1
  print(res)
  i+=1
