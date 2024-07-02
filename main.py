
from tkinter import *

def doSomthing(event):
    print("You press " + event.keysym)
    label.config(text=event.keysym)

window = Tk()

window.bind("<Key>", doSomthing)

label = Label(window, font=("Helvetica", 100))
label.pack()

window.mainloop()
