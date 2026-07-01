import os
import random
import shutil

def createNewFiles():
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

def addContent():
    folderList = os.listdir()

    print("Here are your folders:")
    for folder in folderList:
        print(folder)

    folderName = input("Enter the folder name in which your file is: ")

    if folderName in folderList:
        os.chdir(folderName)
    else:
        print("Folder does not exist.")
        return

    fileList = os.listdir()

    print("Files are:")
    for file in fileList:
        print(file)

    inputFile = input("Enter the file name in which you want to add content: ")

    if inputFile not in fileList:
        print("File does not exist.")
        os.chdir("..")
        return

    randomNumber = random.randint(1000, 9999)

    employeeName = input("Enter employee name: ")
    code = f"{randomNumber}-{employeeName[:4]}"

    n = int(input("How many additional fields do you want to write? "))

    with open(inputFile, "a") as file:
        file.write(f"ID: {code}\n")
        file.write(f"Name: {employeeName}\n")

        for i in range(n):
            fieldName = input(f"Enter field name {i+1}: ")
            fieldValue = input(f"Enter value for {fieldName}: ")
            file.write(f"{fieldName}: {fieldValue}\n")

    print("Content written successfully.")

    os.chdir("..")

def deleteFolder():
  list4 = os.listdir()

  print("Here are your folders")
  for i in list4:
    print(i)
  folderCheckTodelete = input("Enter the folder name in which you want to delete:- ")

  
  # for folders in list4:
  #   if folders==folderCheckTodelete:
  #     # os.rmdir(folderCheckTodelete)
  #     shutil.rmtree(folders)
  #     print("Folder deleted sucessfully ")
  #     break
  #   else:
  #       print("folder don't exist ")
  if os.path.exists(folderCheckTodelete):
    shutil.rmtree(folderCheckTodelete)
    print("folder deleted sucessfully ")
  else:
    print("Folder dosn't exist")


def deleteFile():
  list5=os.listdir()

  print("here are the filders ")

  for folders in list5:
    print(folders)

  fileCheck=input("enter the folder Name in which your file is:- ")


  if fileCheck in list5:
      os.chdir(fileCheck)
  else:
    print("Folder does not exist")
    return
  
  list6=os.listdir()
  print("here are your files :-")

  for i in list6:
    print(" ",i)
  fileInput=input("enter thea file name you want to deltet:- ")

  if os.path.exists(fileInput):
    os.remove(fileInput)
    print("folder deleted sucessfully ")
  else:
    print("Folder dosn't exist")
  
while True:
  print("""enter the operation you want to perfor
        1. Create new folder'
        2. Add content into new file 
        3. Delete folder 
        4. Delete file
        5. exit """)

  input1=int(input("enter you choice :- "))
  if input1==1:
    createNewFiles()
  elif input1==2:
    addContent()
  elif input1==3:
    deleteFolder()
  elif input1==4:
    deleteFile()
  elif input1==5:
    break
  else:
    print("Invailed choice, Try Again")



