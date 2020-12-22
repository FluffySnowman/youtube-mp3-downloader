import tkinter
from tkinter import *


window = tkinter.Tk()

#Adding widgets

label1 = Label(window, text = "Link: ")
label1.pack( side = LEFT)

entrybox1 = Entry(window, bd = 5)
entrybox1.pack(side = RIGHT)


window.mainloop()