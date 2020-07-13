#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import tkinter as tk

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

window = tk.Tk()

for key, value in border_effects.items():
    frame = tk.Frame(master=window, relief=value, borderwidth=10)
    frame.pack(fill=tk.BOTH)
    label = tk.Label(master=frame, text=key, fg="white", bg="black")
    label.pack()

window.mainloop()
