#!/usr/bin/python

import Tkinter
import tkMessageBox

top = Tkinter.Tk()

def helloWorld():
    tkMessageBox.showinfo("Welcome","Hello World")

B = Tkinter.Button(top, text="Hello", command = helloWorld)

B.pack()

top.mainloop()
