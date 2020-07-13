#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import random
import tkinter as tk


def roll():
    res = random.randint(1,6)
    lbl_num["text"] = f"{res}"



window = tk.Tk()

window.rowconfigure(1, weight=1, minsize=50)
window.columnconfigure(0, weight=1, minsize=50)

lbl_num = tk.Label(master=window, text="0")
lbl_num.grid(row=0, column=0, sticky="news")

btn_roll = tk.Button(master=window, text="roll", command=roll)
btn_roll.grid(row=1, column=0, sticky="news")
window.mainloop()


