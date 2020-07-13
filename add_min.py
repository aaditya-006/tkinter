#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import tkinter as tk

window = tk.Tk()

def decrease():
    cur = int(lbl_value["text"])
    lbl_value["text"] = f"{cur-1}"

def increase():
    cur = int(lbl_value["text"])
    lbl_value["text"] = f"{cur+1}"

window.rowconfigure(0, weight=1, minsize=50)
window.columnconfigure([0,1,2], weight=1, minsize=50)

frame = tk.Frame(master=window)


btn_min = tk.Button(master=window, text="-", command=decrease)
btn_min.grid(row=0, column=0, sticky="news")

lbl_value= tk.Label(master=window, text="0")
lbl_value.grid(row=0, column=1, sticky="news")

btn_add = tk.Button(master=window, text="+", command=increase)
btn_add.grid(row=0, column=2, sticky="news")
window.mainloop()
