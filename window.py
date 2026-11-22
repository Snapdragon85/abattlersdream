import tkinter as tk
from tkinter import *

import command_tk

root = tk.Tk()

root.title("A Battler's Dream")
root.configure(background="navy")
root.geometry("600x600")
root.resizable(False, False)


B1 = Button(root, text="Yes", command=lambda: [command_tk.hide_button(B1), command_tk.hide_button(B2)], width=80, height=5)
B2 = Button(root, text="No", command=lambda: [command_tk.hide_button(B1), command_tk.hide_button(B2), command_tk.shutDown()], width=10, height=2)

B1.place(x=15, y=500)
B2.place(x=500, y=500)

root.mainloop()