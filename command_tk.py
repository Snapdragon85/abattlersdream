import tkinter as tk
from tkinter import *

confirm = 0

def hide_button(widget):
    widget.place_forget()


def show_button(widget):
    widget.pack()
    
def shutDown():
    exitProgram = exit()
    exitProgram.pack()

def confirm():
    global confirm
    confirm = 1

def deny():
    global confirm
    confirm = 0