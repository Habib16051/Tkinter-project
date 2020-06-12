from tkinter import *      #Tkinter Module

root = Tk()        #This is TK class and this is it's object

newframe = Frame(root)  #creating Frame
newframe.pack()

otherframe = Frame(root)
otherframe.pack(side=BOTTOM)

button1 = Button(newframe, text="Click here", fg="Green") #Creating Button
button2 = Button(otherframe, text="Click here", fg ="Red")

button1.pack()          #packeting the whole process
button2.pack()

root.mainloop()