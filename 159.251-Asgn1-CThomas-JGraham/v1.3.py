#Authors Jade Graham, Conrad Thomas.

from odf.opendocument import *
import Tkinter
from Tkinter import *
import ScrolledText
import tkFileDialog
import tkMessageBox
import datetime
import os


date = datetime.datetime.now()

start = Tkinter.Tk(className="Text Editor")
textArea=ScrolledText.ScrolledText(start,width=50,height=30)



# New file function
def new():
    if tkMessageBox.askyesno("New File", "Save file before overwriting?"):
        save()
        textArea.delete("1.0",END)
    else:
        textArea.delete("1.0",END)

# Open file function
def open():
    file = tkFileDialog.askopenfile(parent=start,mode='rb',title="Select file")
    if file is not None:
        txt=file.read()
        textArea.delete("1.0",END)
        textArea.insert("1.0",txt)

saved=False
# Save file function
def save():
    file = tkFileDialog.asksaveasfile(mode='w')
    if file != None:
        text = textArea.get('1.0', END+'-1c') # save all text in the textArea until the (end - 1 character)
        file.write(text)
        file.close()
    global saved
    saved=True

# Print function
def toPrinter():
    if (saved):
        os.startfile(file.name, "print")
    else:
        save()
        toPrinter()

# Time function
def timedate():
    global date
    td = date.strftime('%I:%M %p %d/%m/%Y')
    textArea.insert(END,td)

# About function
def about():
    info = tkMessageBox.showinfo("About","\tVersion:\t1.3\n Copyright (c) 2016 , Conrad Thomas, Jade Graham\n All rights reserved. \nRedistribution and use in source and binary forms, with or \nwithout modification, are permitted provided that the \nfollowing conditions are met: \n1. Redistributions of source code must retain the above \n copyright notice, this list of conditions and the following \ndisclaimer.\n2. Redistributions in binary form must reproduce the above \n copyright notice, this list of conditions and the following \ndisclaimer in the documentation and/ or other materials \n provided with the distribution.")


class searching(object):
    def __init__(self):
        self.criteria = Entry(start)
        self.searchButton = Button(start, text="Search",command=self.searchLogic)

        self.criteria.pack(side=LEFT)
        self.searchButton.pack(side=RIGHT)

    def searchLogic(self):
        self.text = textArea.get('1.0', END+'-1c')
        if self.criteria.get() in self.text:
            found = tkMessageBox.showinfo("Search results", "'"+self.criteria.get()+"' found.")
            self.criteria.destroy()
            self.searchButton.destroy()
        else:
            notfound = tkMessageBox.showinfo("Search results", "'"+self.criteria.get()+"' not found.")
            self.criteria.destroy()
            self.searchButton.destroy()


# Menu generation:
menu = Menu(start)
start.config(menu=menu)
fileMenu=Menu(menu,tearoff=0)
searchMenu = Menu(menu,tearoff=0)
viewMenu = Menu(menu,tearoff=0)
helpMenu = Menu(menu,tearoff=0)
###

# File menu:
menu.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="New",command=new)
fileMenu.add_command(label="Open..",command=open)
fileMenu.add_command(label="Save",command=save)
fileMenu.add_command(label="Print",command=toPrinter)
fileMenu.add_separator()
fileMenu.add_command(label="Exit!",command=quit)
###

# Search menu:
menu.add_cascade(label="Search", menu=searchMenu)
searchMenu.add_command(label="Search word...",command=searching)
###

# View Menu:
menu.add_cascade(label="View", menu=viewMenu)
viewMenu.add_command(label="Time/Date...",command=timedate)
###

# Help menu:
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About",command=about)
###

#Program start
textArea.pack()
start.mainloop()