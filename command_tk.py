import tkinter as tk
from tkinter import *


def hide_button(widget):
    widget.pack_forget()


def show_button(widget):
    widget.pack()
    
def shutDown():
    exitProgram = exit()
    exitProgram.pack()