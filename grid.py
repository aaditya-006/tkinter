#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import tkinter as tk

window = tk.Tk()

for i in range(4):

    window.columnconfigure(i, weight=1, minsize=50)
    window.rowconfigure(i, weight=1, minsize=75)

    for j in range(4):
        frame = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=4)
        frame.grid(row=i, column=j,
                   padx=5, pady=5,
                   sticky="nesw") # sticky=s/w/e/n
        label = tk.Label(master=frame, text=f"row:{i},col:{j}", bg="black", fg="white")
        label.pack()

window.mainloop()
