from tkinter import  *


root=Tk()

canvas = Canvas(root, height=100, width=200)
canvas.pack()

newline= canvas.create_line(0,0,50,100)

otherline= canvas.create_line(10,10,100,200, fill = "Pink")

root.mainloop()