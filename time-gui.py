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
    e1["width"] = 5
    e1.grid(row=0, column=1)
    e1.insert(0, "6:00")
    e1.config(bg="white")
    
    #Create a Label in textFrame
    l2 = Label(textFrame)
    l2["text"] = "How long will you work?:"
    l2.grid(row=1, column=0)
    
    # Create an Entry Widget in textFrame
    e2 = Entry(textFrame)
    e2.bind("<Key>", validateTextInputSize)
    e2["width"] = 5
    e2.grid(row=1, column=1)
    e2.insert(0, "8:00")
    e2.config(bg="white")

    l3 = Label(textFrame)
    l3["text"] = "And lunch? :"
    l3.grid(row=1, column=4)
    
    e3 = Entry(textFrame)
    e3.bind("<Key>", validateTextInputSize)
    e3["width"] = 2
    e3.grid(row=1, column=5)
    e3.insert(0, "30")
    e3.config(bg="white")
    
    l4 = Label(textFrame)
    l4["text"] = "minutes"
    l4.grid(row=1, column=6)
    
    textFrame.pack()
    
def getTime()

    now = dt.datetime.now
    h1 = str(now.hour) 
    m1 = str(now.minute) 
    s1 = str(now.second) 

    # arrival time 
    while True: 
        try: 
            t_in =str(e1.get()) 
            t_in_h, t_in_m = t_in.split(':')  
            val1 = int(t_in_h) 
            val2 = int(t_in_m) 
            break 
        except (ValueError): 
            t_in_h = "06" 
            t_in_m = "00" 
            #print("No or wrong input - using standard time - 6:00") 
        break 

    # work time     
    while True: 
        try: 
            t_work = str(e2.get()) 
            t_work_h, t_work_m = t_work.split(':')  
            val3 = int(t_work_h) 
            val4 = int(t_work_m) 
        except (ValueError): 
            t_work_h = "08" 
            t_work_m = "00" 
            #print("No or wrong input - using standard time - 8:00") 
        break 
    
    # lunch break 
    while True:
        try:
            t_lunch1 = int(e3.get()) 
        except (ValueError): 
            t_lunch1 = int("30") 
        break 

    #variables preparation 
    t_now = h1 + ":" + m1 + ":" + s1 
    t_ar= t_in_h + ":" + t_in_m + ":00" 
    t_m = dt.timedelta(minutes=int(t_work_m)) + dt.timedelta(minutes=int(t_lunch1)) 
    t_w_h, t_w_m, t_w_s = str(t_m).split(':') 
    time_working = str(int(t_work_h) + int(t_w_h)) + ":" + str(t_w_m) + ":00" 
    fmt = '%H:%M:%S' 
    
    #time values calculation and check 
    time_lost = dt.datetime.strptime(str(t_now), str(fmt)) - dt.datetime.strptime(t_ar, fmt) 
    time_lost1 = dt.datetime.strptime(str(time_working), str(fmt)) - dt.datetime.strptime(str(time_lost), str(fmt)) 
    time_home = dt.datetime.strptime(str(t_now), str(fmt)) + time_lost1 
    time_print = dt.datetime.time(time_home) 
    
clock = Label(main, font=('times', 20, 'bold'), bg='green')
clock.pack(fill=BOTH, expand=1)
def tick():
    s = dt.datetime.time(time_home) 
    if s != clock["text"]:
        clock["text"] = s
    clock.after(200, tick)
tick()
main.mainloop()
