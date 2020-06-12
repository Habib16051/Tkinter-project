from tkinter import *
import tkinter.messagebox

root=Tk()

tkinter.messagebox.showinfo("Titile", "Wow! This is awesome!")

response = tkinter.messagebox.askquestion("Question 1: ", "Would you like to get a cup of coffee? !")

if response=='yes':
    print("Here is your Coffee Sir!")
root.mainloop()
