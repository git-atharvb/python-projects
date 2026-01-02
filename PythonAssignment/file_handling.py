#file handling
#opening a file
f = open("abc.txt","+w") #creates a file using w mode
f.write("Welcome Back")
f.seek(0) #gets the cursor at opening in opened file
print(f.readlines())
f.close()

# f1=open("src.txt","+r")
# f2=open("new.txt","w")

# data=f1.read()
# f1.write(data)

# f1.seek(0)
# print(f1.readlines())