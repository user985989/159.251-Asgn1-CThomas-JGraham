import Tkinter
from Tkinter import Menu
import ScrolledText
import tkFileDialog
import tkMessageBox

start = Tkinter.Tk(className="Text Editor")
textArea=ScrolledText.ScrolledText(start,width=50,height=30)
def foo():
    print "s"
def open():
    file = tkFileDialog.askopenfile(parent=start,mode='rb',title="select file")
menu = Menu(start)
start.config(menu=menu)
fileMenu=Menu(menu,tearoff=0)
menu.add_cascade(label="File",menu=fileMenu)

fileMenu.add_command(label="New",command=foo)
fileMenu.add_command(label="Open..",command=open)
fileMenu.add_command(label="Save",command=foo)
fileMenu.add_command(label="Print",command=foo)
fileMenu.add_separator()
fileMenu.add_command(label="Exit!",command=foo)
search = Menu(menu)
menu.add_cascade(label="Search", menu=search)
search.add_command(label="search a word",command=foo)
helpMenu=Menu(menu)
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About",command=foo)


textArea.pack()
start.mainloop()