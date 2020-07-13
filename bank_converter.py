#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import tkinter as tk

window = tk.Tk()

window.rowconfigure(0, weight=1, minsize=100)
window.columnconfigure(0, weight=1, minsize=100)

btns = ['dashboard', 'convert', 'push', 'pulled reports', 'settings', 'help']

frm_nav_bar = tk.Frame(master=window, relief=tk.RAISED, bd=5)
frm_nav_bar.grid(row=0, column=0, sticky="new")
for index, values in enumerate(btns):
    btn = tk.Button(master=frm_nav_bar, text=values, width=10, height=10)
    #btn.grid(column=index, row=0, padx=10, sticky="ew")
    btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

btn_tmp = tk.Button(master=window, text="tmp")
btn_tmp.grid(column=0, row=1, sticky="ew")

window.mainloop()
