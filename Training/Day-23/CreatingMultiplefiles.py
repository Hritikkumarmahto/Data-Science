import os

choice=input("want to Create New directry Yes/no")
list1=[]
if choice=='y':
  folder_name=input("enter the folder name : - ")
  newFolder = folder_name
  os.makedirs(newFolder, exist_ok=True)
  n=int(input("enter How many files you want to create "))  
  for i in range(n):
    k=input(f"enter the {i+1} file name:- ")
    list1.append(k) 

  filetype=input("which file type you wnat to create :-  ")

  for i in range(len(list1)):
    filecheck = os.path.exists(os.path.join(newFolder, f"{list1[i]}.{filetype}"))

    if not filecheck:
     with open(os.path.join(newFolder,list1[i]+"."+filetype),"w") as f:
      print(f"file created {list1[i]} ")
    else:
      print("file already exists")
  print("operations created ")

else:
  
  n=int(input("enter How many files you want to create "))
  for i in range(n):
    k=input(f"enter the {i+1} file name:- ")
    list1.append(k)

  filetype=input("which file type you wnat to create :-  ")

  for i in range(len(list1)):
    filecheck= os.path.exists(f"{i}+{filetype}")
    
  if not filecheck:
    with open(list1[i]+"."+filetype,"w") as f:
      print(f"file created {list1[i]} ")
  else:
      print("file already exists")
  print("operations created ")
