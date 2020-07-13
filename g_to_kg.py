#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import tkinter as tk

def convert():
    gram = ent_input.get()
    lbl_result["text"] = f"{float(gram)/1000}"

window = tk.Tk()

window.columnconfigure([0,1,2,3,4], weight=1, minsize=50)
window.rowconfigure(0, weight=1, minsize=50)

ent_input = tk.Entry(master=window)
ent_input.grid(row=0, column=0)

lbl_gram = tk.Label(master=window, text="gram")
lbl_gram.grid(row=0, column=1)

lbl_convert = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=convert)
lbl_convert.grid(row=0, column=2)

lbl_result = tk.Label(master=window, text="")
lbl_result.grid(row=0, column=3)

lbl_kilogram = tk.Label(master=window, text="kilogram")
lbl_kilogram.grid(row=0, column=4)

window.mainloop()
