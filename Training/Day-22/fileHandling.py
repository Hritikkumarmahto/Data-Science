# f=open("strics.txt","x")
f=open("strics.txt","w")
f.write("2this is Hritik this side ")
f.close


# context manager

with open("manager.txt","w+") as file:
  file.write("hello this is hritik this side")
  file.seek(0)
  r=file.read() # read(+) will add 
  print("file created and written in it ")
  print(f"file creates contet {r}")


with open("demo.txt", "w") as f:
    f.write("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since 1966, when designers at Letraset and James Mosley, the librarian at St Bride Printing Library in London, took a 1914 Cicero translation and scrambled it to make dummy text for Letraset's Body Type sheets. It has survived not only many decades, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised thanks to these sheets and more recently with desktop publishing software like Aldus PageMaker and Microsoft Word including versions of Lorem Ipsum.""")

with open("demo.txt", "r") as f, open("newDemo.txt", "w") as t: 
    for i in f.read():
        if i not in "/.,';][]-=+_!@#$%^&*1234567890":
            t.write(i)

with open("newDemo.txt", "r") as t:
    print(t.read())
;//
