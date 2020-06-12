from tkinter import *

root =Tk()

def HandlingButton():
    print("You clicked there!")

button= Button(root, text="Click here", command = HandlingButton ,fg="Green")
button.pack()

root.mainloop()