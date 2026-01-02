from tkinter import *
from functools import partial
import webbrowser

def printDetails(usernameEntry) :
    usernameText = usernameEntry.get()
    print("user entered :", usernameText)
    return

#window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('ASSIGNMNENT 10')

#label
label1= Label(tkWindow, text="Enter what you want to search : ")
#entry for user input
dataEntry = Entry(tkWindow)

#define callable function with printDetails function and usernameEntry argument
printDetailsCallable = partial(printDetails, dataEntry)

#submit button
submitButton = Button(tkWindow, text="SEARCH", command=webbrowser.open('https://www.youtube.com/'))

#place label, entry, and button in grid
label1.grid(row=0, column=0)
dataEntry.grid(row=0, column=1) 
submitButton .grid(row=1, column=1)  

#main loop
tkWindow.mainloop(dataEntry)