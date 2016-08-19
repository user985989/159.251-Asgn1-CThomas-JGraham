import Tkinter

import ScrolledText

start = Tkinter.Tk(className="Text Editor")
textArea=ScrolledText.ScrolledText(start,width=50,height=30)

textArea.pack()
start.mainloop()