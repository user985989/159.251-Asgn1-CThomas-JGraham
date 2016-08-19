__author__ = 'Conrad Thomas - 13236623'

from tkinter import *
#import tkinter as tk

root = Tk()
root.title("Text Editor")
txt = StringVar()

# Save function
def save():
    print('File saved.')



# Open function
def open():
    fname = Entry(root,textvariable=txt).pack()
    def x():
        fname.pack_forget()

    confirm = Button(root,text='Open',command=x).pack()


def y():
    global fname
    fname.destroy()

def newFile():
    newfile = Entry(root,textvariable=txt).pack()
    confirm = Button(root,text='Create',command=None).pack()

def test():
    text = txt.get()
    if text.endswith('.txt'):
        filename = text+' found.'
        lab = Label(root,text=filename).pack()
    else:
        notfound = text+' not found.'
        lab = Label(root,text=notfound).pack()

    return


menubar = Menu(root)

#menubar.add_command(label="File")
#menubar.add_command(label="View")

fileMenu = Menu(menubar, tearoff=0)
fileMenu.add_command(label="Open",command=open)
fileMenu.add_command(label="Save",command=save)
fileMenu.add_command(label="New File",command=newFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="File", menu=fileMenu)

root.config(menu=menubar)

textbox = Text(root,height=10,width=30)
textbox.pack()
textbox.insert(END,"enter text here")


root.mainloop()
