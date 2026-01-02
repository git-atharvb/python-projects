from tkinter import *
root=Tk(className=" LOGIN")

l1=Label(root,text="Enter Username",font=("Times New Roman",30))
l1.pack(anchor="center",side="top")

e1=Entry(root,font=("Times New Roman",30))
e1.pack(anchor="center",side="top")

l2=Label(root,text="Enter Password",font=("Times New Roman",30))
l2.pack(anchor="center",side="top")

e2=Entry(root,font=("Times New Roman",30),show="*")
e2.pack(anchor="center",side="top")

#label for displaying space
lA=Label(root,text=" ",font=("Times New Roman",10))
lA.pack(anchor="center",side="top")

def store():
    user=e1.get()
    password=e2.get()
    print(user,password)
    if user=="atharv" and password=="pass":
        f=open("data.txt","+at")
        print("Username : {} Password : {}".format(user,password))
        f.write(f"\n Username : {user} \n Password : {password}")
        # print("Username : %s Password : %s"%(user,password))
        # print(f"Username : {user} Password : {password}")
        l3["text"]="Data Added Successfully!"
    else: l3["text"]="Enter correct crediantials"


b1=Button(root, text="LOGIN",font=("Times New Roman",15),bg="orange",command=store)
b1.pack(anchor="center",side="top")

#label for displaying
l3=Label(root,text=" ",font=("Times New Roman",30))
l3.pack(anchor="center",side="top")

b=Button(root,text="Exit",font=("Times New Roman",15),command=root.destroy)
b.pack(anchor="center",side="top")

root.mainloop()