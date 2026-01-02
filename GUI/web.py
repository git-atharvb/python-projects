import webbrowser as wb

# import tkinter as tk
from tkinter import *
root = Tk() #access functions from class Tk
#can use className="" to change name of window
root.title("Hello World") #change name of window 

#input entry
e=Entry(root,font=("Times New Roman",30))
e.pack(anchor="center",side="top")

#function get data from input entry and display in terminal
def display():
    query=e.get()
    print(query)
    wb.open("https://www.google.com/search?q="+query)

#button declaration
b=Button(root,text="SEARCH",font=("Times New Roman",25),command=display,bg="red",activebackground="blue",fg="white")
# b.grid(row=0,column=4) 
#def : row=0 and column=0
# b.place(x=100,y=100)   
# #place is used on basis of X and Y axis and values are based on pixels
b.pack(anchor="center",side="top")

#exit button
b=Button(root,text="Exit",font=("Times New Roman",25),command=root.destroy)
b.pack(anchor="center",side="top")
root.mainloop()  #creates a new window in output