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

def foo():
    print "s"

def new():
    if tkMessageBox.askyesno("New File", "Save file before overwriting?"):
        save()
        textArea.delete("1.0",END)
    else:
        textArea.delete("1.0",END)

def open():
    file = tkFileDialog.askopenfile(parent=start,mode='rb',title="Select file")
    if (file.name.endswith(".odt")):

        global doc
        doc=load(file.name)
        doc.save(file.name,TRUE)
        textArea.insert(INSERT,doc) #will only load instance of odt..

saved=False
def save():
    global saved
    file = tkFileDialog.asksaveasfile(mode='w')
    if file != None:
        saved=True
        text = textArea.get('1.0', END+'-1c') # save all text in the textArea until the (end - 1 character)
        file.write(text)
        file.close()


def toPrinter():
    if (saved):
        os.startfile(file.name, "print")
    else:
        save()
        toPrinter()

def timedate():
    global date
    td = date.strftime('%I:%M %p %d/%m/%Y')
    textArea.insert(END,td)

def about():
    info = tkMessageBox.showinfo("About","Authors: \tJade Graham\n                \tConrad Thomas\n\nVersion:\t1.2")




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


textArea.pack()
start.mainloop()
