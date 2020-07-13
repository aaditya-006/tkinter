#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import random
import tkinter as tk

def dash_board():
    print('dash_board')

root = tk.Tk()

menubar = tk.Menu(root)
menubar.add_command(label="dashboard", command=dash_board)

root.config(menu=menubar)

root.mainloop()
