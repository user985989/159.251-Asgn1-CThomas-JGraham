__author__ = 'Conrad Thomas - 13236623'

import Tkinter
from Tkinter import *
import ScrolledText
import tkFileDialog
import tkMessageBox

start = Tkinter.Tk(className="Text Editor")
textArea=ScrolledText.ScrolledText(start,width=50,height=30)

def foo():
    print "s"



def open():
    file = tkFileDialog.askopenfile(parent=start,mode='rb',title="select file")

def save():
    file = tkFileDialog.asksaveasfile(mode='w')
    if file != None:
        text = textArea.get('1.0', END+'-1c') # save all text in the textArea until the (end - 1 character)
        file.write(text)
        file.close()


def about():
    info = tkMessageBox.showinfo("About","Authors: \tJade Graham\n                \tConrad Thomas\n\nVersion:\t1.x")


class searching(object):
    def __init__(self):
        self.criteria = Entry(start)
        self.searchButton = Button(start, text="Search",command=self.searchLogic)

        self.criteria.pack(side=LEFT)
        self.searchButton.pack(side=RIGHT)

    def searchLogic(self):
        self.text = textArea.get('1.0', END+'-1c')
        if self.criteria.get() in self.text:
            print 'found!!'
        else:
            print 'not found :('

# Menu generation:
menu = Menu(start)
start.config(menu=menu)

fileMenu=Menu(menu,tearoff=0)
searchMenu = Menu(menu,tearoff=0)
helpMenu = Menu(menu,tearoff=0)
###

# File menu:
menu.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="New",command=foo)
fileMenu.add_command(label="Open..",command=open)
fileMenu.add_command(label="Save",command=save)
fileMenu.add_command(label="Print",command=foo)
fileMenu.add_separator()
fileMenu.add_command(label="Exit!",command=quit)
###

# Search menu:
menu.add_cascade(label="Search", menu=searchMenu)
searchMenu.add_command(label="Search word...",command=searching)
###

# Help menu:
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About",command=about)
###


textArea.pack()
start.mainloop()