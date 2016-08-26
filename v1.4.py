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


# Add selected text to clipboard
def copy():
    global textArea
    try:
        # if something has previously been copied, delete it
        if start.clipboard_get() is not None:
            start.clipboard_clear()

        # add selected text to the clipboard
        selected = textArea.get(SEL_FIRST,SEL_LAST)
        start.clipboard_append(selected)
    except TclError:
        pass

# Remove selected text and add it to the clipboard
def cut():
    try:
        if start.clipboard_get() is not None:
            start.clipboard_clear()
        selected = textArea.get(SEL_FIRST,SEL_LAST)

        # delete selected text from screen and add it to clipboard
        textArea.delete(SEL_FIRST,SEL_LAST)
        start.clipboard_append(selected)
    except TclError:
        pass

# Paste previously copied text
def paste():
    clipboard = start.clipboard_get()
    # check if the clipboard has something in it
    if clipboard is not None:
        textArea.insert(END,clipboard)
    else:
        pass

# Generate a new file
def new():
    if tkMessageBox.askyesno("New File", "Save file before overwriting?"):
        save()
        textArea.delete("1.0",END)
    else:
        textArea.delete("1.0",END)

# Open a file
def open():
    file = tkFileDialog.askopenfile(parent=start,mode='rb',title="Select file")
    if file is not None:
        txt = file.read()
        textArea.delete("1.0",END)
        textArea.insert("1.0",txt)


# Opens a file explorer to save the text to a file
saved=False
def save():
    global saved
    file = tkFileDialog.asksaveasfile(mode='w')
    if file is not None:
        saved=True
        text = textArea.get('1.0', END+'-1c') # save all text in the textArea until the (end - 1 character)
        file.write(text)
        file.close()

# Check if file has been saved then send to default printer
def toPrinter():
    if (saved):
        os.startfile(file.name, "print")
    else:
        save()
        toPrinter()

# Get current time and date and display it
def timedate():
    global date
    td = date.strftime('%I:%M %p %d/%m/%Y')
    textArea.insert(END,td)

# Show relevant information about application
def about():
    legalInfo = "\n\nRedistribution and use in source and binary forms, with or \nwithout modification, " \
                "are permitted provided that the \nfollowing conditions are met: \n1. Redistributions " \
                "of source code must retain the above \n copyright notice, this list of conditions and " \
                "the following \ndisclaimer.\n2. Redistributions in binary form must reproduce the above \n " \
                "copyright notice, this list of conditions and the following \ndisclaimer in the " \
                "documentation and/ or other materials \n provided with the distribution."
    info = tkMessageBox.showinfo("About","Authors: \tJade Graham\n                \tConrad Thomas\n\nVersion:\t1.4"+legalInfo)


# Search for a single word within the text
class searching(object):
    def __init__(self):
        # Entry field and button for searching
        self.criteria = Entry(start)
        self.searchButton = Button(start, text="Search",command=self.searchLogic)

        self.criteria.pack(side=LEFT)
        self.searchButton.pack(side=RIGHT)

    def searchLogic(self):
        # get all text from textArea then split it and store in self.words
        self.textbox = textArea.get('1.0', END+'-1c')
        self.words = self.textbox.split(" ")

        self.end = textArea.index("end-1c") # set the end of the text as self.end

        self.search = self.criteria.get()
        self.found = textArea.search(self.search,"1.0",END)

        # if the specified search criteria is found:
        if self.found:
            # find all the occurrences of the search criteria
            while self.found:
                for word in self.words:
                    if self.search == word:
                        wordPos = self.found.split(".")

                        # if wordPos doesn't have length of two, all occurrences have been found
                        if len(wordPos) == 2:
                            linenum = wordPos[0]
                            startPos = wordPos[1]
                            endPos = int(wordPos[1]) + (len(self.search)-1)
                        else:
                            break

                        foundmsg = tkMessageBox.showinfo("Search results", "'"+self.search+"' found on:\nLine: "+str(linenum)+"\nPosition: "+str(startPos)+"-"+str(endPos))

                        self.found = textArea.search(self.search, str(linenum)+"."+str(endPos),END)

            # Remove search field and button after search is complete
            self.criteria.destroy()
            self.searchButton.destroy()

        # if the search criteria is not found:
        else:
            notfound = tkMessageBox.showinfo("Search results", "'"+self.search+"' not found.")
            self.criteria.destroy()
            self.searchButton.destroy()


# Menu generation:
menu = Menu(start)
start.config(menu=menu)

fileMenu=Menu(menu,tearoff=0)
editMenu = Menu(menu,tearoff=0)
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

# Edit Menu:
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)
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

# Program Start
textArea.pack()
start.mainloop()