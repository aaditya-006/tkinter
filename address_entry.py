#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import tkinter as tk

window = tk.Tk()

window.title("address entry form")

#window.rowconfigure(0, weight=1, minsize="50")
#window.columnconfigure(0, weight=1, minsize="75")

labels = ['address', 'first_name', 'last_name', 'phone']

frame = tk.Frame(master=window, borderwidth=4)
frame.pack()
for index, value in enumerate(labels):
    label = tk.Label(master=frame, text=value+':')
    ent = tk.Entry(master=frame)
    label.grid(row=index, column=0, sticky='e')
    ent.grid(row=index, column=1)

frm_button = tk.Frame()
frm_button.pack(padx=5, pady=5, fill=tk.X)

btn_submit = tk.Button(master=frm_button, text="submit")
btn_submit.pack(padx=5,pady=5, side=tk.RIGHT)
btn_clear = tk.Button(master=frm_button, text="clear")
btn_clear.pack(padx=5,pady=5, side=tk.RIGHT)

def handle_keypress(event):
    print(event.char)

window.bind("<Key>", handle_keypress)

def handle_button(event):
    print('left mouse button clicked')

btn_submit.bind("<Button-1>", handle_button)

window.mainloop()

