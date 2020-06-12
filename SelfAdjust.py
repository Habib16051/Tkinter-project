from tkinter import *

root = Tk()

label1 = Label(root, text ="Python", bg="Green", fg="Yellow")
label2 = Label(root, text ="Django", bg="Blue", fg="White")

label1.pack(fill=X)
label2.pack(side=LEFT, fill =Y)



root.mainloop()