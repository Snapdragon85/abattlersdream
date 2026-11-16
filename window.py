from tkinter import *
from tkinter import ttk

print("Working!")

root = Tk()

root.title("A Battler's Dream")
root.geometry('360x360')

lbl = Label(root, text = "Game Working!")
lbl.grid()

def clicked():
    lbl.configure(text = "boo")

btn = Button(root, text = "Spooky button D:", command=clicked)
btn.grid(column=0, row=1)


root.mainloop()