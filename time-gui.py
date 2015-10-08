from tkinter import *
import time
import sys
import datetime as dt
from datetime import timedelta

def validateTextInputSize(event):
    """ Method to Validate Entry text input size """

    global TEXT_MAXINPUTSIZE
        
    if (event.widget.index(END) >= TEXT_MAXINPUTSIZE - 1):
        event.widget.delete(TEXT_MAXINPUTSIZE - 1)        
        
def displayText():
    """ Display the Entry text value. """

    global entryWidget

    if entryWidget.get().strip() == "":
        tkMessageBox.showerror("Tkinter Entry Widget", "Enter a text value")
    else:
        tkMessageBox.showinfo("Tkinter Entry Widget", "Text value =" + entryWidget.get().strip()) 

if __name__ == "__main__":

    main = Tk()
    
    main.title("Main Widget")
    main["padx"] = 40
    main["pady"] = 2 
    
    # Create a text frame to hold the text Label and the Entry widget
    textFrame = Frame(main)

    #Create a Label in textFrame
    l1 = Label(textFrame)
    l1["text"] = "Enter time of arrival:"
    l1.grid(row=0, column=0)

    # Create an Entry Widget in textFrame
    e1 = Entry(textFrame)
    e1.bind("<Key>", validateTextInputSize)
    e1["width"] = 2
    e1.grid(row=0, column=1)
    e1.insert(0, "6")
    e1.config(bg="white")
    
    l2 = Label(textFrame)
    l2["text"] = ":"
    l2.grid(row=0, column=2)
    
    e2 = Entry(textFrame)
    e2.bind("<Key>", validateTextInputSize)
    e2["width"] = 2
    e2.grid(row=0, column=3)
    e2.insert(0, "00")
    e2.config(bg="white")
    
    #Create a Label in textFrame
    l3 = Label(textFrame)
    l3["text"] = "How long will you work?:"
    l3.grid(row=1, column=0)
    
    # Create an Entry Widget in textFrame
    e3 = Entry(textFrame)
    e3.bind("<Key>", validateTextInputSize)
    e3["width"] = 2
    e3.grid(row=1, column=1)
    e3.insert(0, "8")
    e3.config(bg="white")
    
    l4 = Label(textFrame)
    l4["text"] = ":"
    l4.grid(row=1, column=2)
    
    e4 = Entry(textFrame)
    e4.bind("<Key>", validateTextInputSize)
    e4["width"] = 2
    e4.grid(row=1, column=3)
    e4.insert(0, "00")
    e4.config(bg="white")

    l5 = Label(textFrame)
    l5["text"] = "And lunch? :"
    l5.grid(row=1, column=4)
    
    e5 = Entry(textFrame)
    e5.bind("<Key>", validateTextInputSize)
    e5["width"] = 2
    e5.grid(row=1, column=5)
    e5.insert(0, "30")
    e5.config(bg="white")
    
    l6 = Label(textFrame)
    l6["text"] = "minutes"
    l6.grid(row=1, column=6)
    
    textFrame.pack()
    
clock = Label(main, font=('times', 20, 'bold'), bg='green')
clock.pack(fill=BOTH, expand=1)
def tick():
    s = time.strftime('%H:%M:%S')
    if s != clock["text"]:
        clock["text"] = s
    clock.after(200, tick)
tick()
main.mainloop()
