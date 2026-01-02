import webbrowser as wb
from tkinter import *

root=Tk()
root.title(" Assignment 11 Course")
l1=Label(root,text="Which course you want to enquiry about : ",font=("Times New Roman",30))
l1.pack(anchor="center",side="top")

e1=Entry(root, font=("Times New Roman",22))
e1.pack(anchor="center",side="top")

l2=Label(root,text="Where did you find its advertisement ?",font=("Times New Roman",30))
l2.pack(anchor="center",side="top")

op1=Radiobutton(root,text="Instagram",font=("Times New Roman",30))
op1.pack(anchor="center",side="top")

op2=Radiobutton(root,text="Youtube",font=("Times New Roman",30))
op2.pack(anchor="center",side="top")

def searchResults():
    query = e1.get()
    print("Opening results in browser for ",query)
   
    wb.open("https://www.udemy.com/courses/search/?src=ukw&q="+query)
    wb.open("https://support.udemy.com/hc/en-us/articles/229232187-Learning-With-Udemy-FAQ")

l3=Label(root,text="Opening FAQ page also",font=("Times New Roman",30))
l3.pack(anchor="center",side="top")

b1=Button(root,text="Search",font=("Times New Roman",30),command=searchResults)
b1.pack(anchor="center",side="top")

root.mainloop()