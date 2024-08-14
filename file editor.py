"in the name of allah"
import tkinter as tk
from tkinter.filedialog import askopenfilename,asksaveasfilename
def open_file():
    fielpath=askopenfilename(filetypes=[("text files","*.txt"),("all files","*.*")])
    if not filepath:
        return
    txt_edit.delelte(1.0,tk.end)
    with open(fielpath,"r")as input_fiel:
        txt_dit.insert(tk.end,text)
    window.tilte(f"ext editor application-{filepath}")
def save_file():
    filepath=asksavefilename(defaultextension="txt",
                             filetypes=[("text file",".txt"),("all files","*.*")])
    if not filepath:
        return
    with open(filepath,"w")as output_file:
        text=txt_edit.get(1.0,tk.end)
        output_file.write(text)
    window.title(f"text editor application -{filepath}")
window=tk.Tk()
window.title("text editor application")
window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)
txt_edit=tk.Text(window)
fr_buttons=tk.Frame(window,relief=tk.RAISED,bd=2)
btn_open=tk.Button(fr_buttons,text="open_file",
                   command=open_file)
btn_save=tk.Button(fr_buttons,text="save as",
                   command=save_file)
btn_open.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
btn_save.grid(row=2,column=0,sticky="ew",padx=5,pady=5)
fr_buttons.grid(row=0,column=1,sticky="nsew")
window.mainloop()