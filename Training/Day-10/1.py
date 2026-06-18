def function(s):
  count=0
  for i in s:
    count+=1

  if count%2==0:
    return s[count//2]+s[count//2+1]
  else:
    return s[count//2]

print(function("Hritik"))


def function(s):
    count = 0

    for i in s:
        count += 1

    if count % 2 == 0:
        return s[count//2 - 1] + s[count//2]
    else:
        return s[count//2]

print(function("Hritik"))