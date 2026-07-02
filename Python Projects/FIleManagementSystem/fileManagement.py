import os
import random
import shutil

def createNewFiles():
    fileNames = []

    folderName = input("Enter the folder name: ")
    os.makedirs(folderName, exist_ok=True)

    n = int(input("Enter how many files you want to create: "))

    for i in range(n):
        fileName = input(f"Enter file {i+1} name: ")
        fileNames.append(fileName)

    fileType = input("Enter file type: ")

    for i in range(len(fileNames)):
        fileCheck = os.path.exists(os.path.join(folderName, f"{fileNames[i]}.{fileType}"))

        if not fileCheck:
            with open(os.path.join(folderName, fileNames[i] + "." + fileType), "w"):
                print(f"File '{fileNames[i]}' created successfully.")
        else:
            print(f"File '{fileNames[i]}' already exists.")

    print("Operation completed.")


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
    folderList = os.listdir()

    print("Here are your folders:")
    for folder in folderList:
        print(folder)

    folderName = input("Enter the folder name you want to delete: ")

    if os.path.exists(folderName):
        shutil.rmtree(folderName)
        print("Folder deleted successfully.")
    else:
        print("Folder does not exist.")


def deleteFile():
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

    print("Here are your files:")

    for file in fileList:
        print(file)

    fileName = input("Enter the file name you want to delete: ")

    if os.path.isfile(fileName):
        os.remove(fileName)
        print("File deleted successfully.")
    else:
        print("File does not exist.")

    os.chdir("..")


while True:
    print("""
Choose an operation:
1. Create new folder
2. Add content into file
3. Delete folder
4. Delete file
5. Exit
""")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        createNewFiles()

    elif choice == 2:
        addContent()

    elif choice == 3:
        deleteFolder()

    elif choice == 4:
        deleteFile()

    elif choice == 5:
        print("Thank you.")
        break

    else:
        print("Invalid choice. Try again.")


  