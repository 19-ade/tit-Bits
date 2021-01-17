from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import showerror
import tkinter as tk
import tkinter.font as font

filename = None


def new_file_create():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)


def save_file():
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()


def save_as_file():
    global filename
    q = asksaveasfile(mode='w', defaultextension=".txt")
    t = text.get(0.0, END)
    try:
        q.write(t.rstrip())
    except:
        showerror(title='uh-oh', message="Unable to save the file")


def open_file():
    f = askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

def font_specifier_Helvetica():
    text.config(font="Helvetica")
def font_courier():
    text.config(font="Courier")

root = tk.Tk()
root.title("Ande editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=600)
text=Text(root, width=1000,height=1000)
text.pack()
menubar=Menu(root)
filemenu=Menu(menubar)
filemenu.add_command(label="New",command=new_file_create)
filemenu.add_command(label="open",command=open_file)
filemenu.add_command(label="Save",command=save_file)
filemenu.add_command(label="Save as ",command=save_as_file)
filemenu.add_command(label="font_helvetica",command=font_specifier_Helvetica)

filemenu.add_separator()
filemenu.add_command(label="Quit",command=root.quit)
menubar.add_cascade(label="File",menu=filemenu)

root.config(menu=menubar)
root.mainloop()