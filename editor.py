#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    filepath = askopenfilename(filetypes=[("text file", "*.txt"), ("all files", "*.*")])
    if not filepath:
        return
    txt.delete("1.0", tk.END)
    with open(filepath, "r") as fp:
        text = fp.read()
        txt.insert("1.0", text)
    window.title(f"Editor: {filepath}")

def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("text files", "*.txt"), ("all files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        output_txt = txt.get(1.0, tk.END)
        output_file.write(output_txt)
    window.title(f"Editor: {filepath}")

window = tk.Tk()
window.title("Editor")


window.columnconfigure(1, weight=1, minsize=800)
window.rowconfigure(0, weight=1, minsize=800)

txt = tk.Text(window)

frm_btns = tk.Frame(window, relief=tk.RAISED, borderwidth=4)

btn_open = tk.Button(master=frm_btns, text="open", command=open_file)
btn_save= tk.Button(master=frm_btns, text="save", command=save_file)

btn_open.grid(column=0, row=0, sticky="ew", pady=10, padx=5)
btn_save.grid(column=0, row=1, sticky="ew", pady=5)

frm_btns.grid(column=0, row=0, sticky="sn")
txt.grid(column=1, row=0, sticky="news")
window.mainloop()
