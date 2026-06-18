
string1=input("Enter the string ")

def vowels(s):
  resStr=""
  for i in range(len(s)):
    if s[i] in 'aeiouAEIOU':
      resStr+=s[i]
  return resStr

print(vowels(string1))

def vowels_and_indexes(s):
    for i in range(len(s)):
        if s[i] in "aeiouAEIOU":
            print(s[i], "at index", i)

vowels_and_indexes(string1)

