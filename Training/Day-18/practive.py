# Wap to remove last word from the string
def removeLast(str1):
 str2=str1.split()    # splits the words 
 str2.pop()
 return " ".join(str2)

str1=input(("enter the string"))
print(removeLast(str1))


# WAP to remove word if vowel is present 

def removeVowel(str1):
 str2=str1.split()

 result=[]

 for i in str2:
  flag=True
  for ch in str2:
   if ch in "aeiouAEIOU":
    flag=True
    break
  if flag:
   result.append(i)

  return result
 
 str1=input("enter the string ")
 removeVowel(str1)

  
   

str1=input("Enter s string ")
print(removeVowel(str1))


#  3. waf to count total white space in string 

def removeWhiteSpace(str1):
  str2=" "
  for i in str1:
   if i ==" ":
    str1.pop(i)
  return "".join(str1)
str1=input("enter the string ")
print(removeWhiteSpace(str1))


    