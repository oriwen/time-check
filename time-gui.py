from tkinter import *
import time
import sys
import datetime as dt
from datetime import timedelta

# quit and save button - to be done
def bQuits():
    name = quit()
    print (name)

# quit button
def bQuit():
    name = quit()
    print (name)

# about button - to be checked
def About():
    about = Toplevel()
    about.title("About")
    toplevel.focus_set()
    inside = Label(t, text= "Go Home program\n \n Version 2.0 beta\n \n How to use:\n Adjust time value by clicking on it.\n Left-click to add 1 minute\n Shift+Left-click to add 15 minutes\n Right-click to substract 1 minute\n Shift+Right-click to substract 15 minutes\n")
    inside.pack(side="top", fill="both")

# adding 1 or 15 minutes to time specified - to be done
def AddTime():
    #insert function to add 1 and 15 minutes

# substracting 1 or 15 minutes to time specified - to be done   
def SubTime():
    #insert function to substract 1 and 15 minutes

if __name__ == "__main__":

    main = Tk()
    main.resizable(width=FALSE, height=FALSE)
    root.geometry('{}x{}'.format(<150>, <150>))
   
   # Upper cascade menu 
    menu = Menu(main)
    main.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Exit", command=main.quit)

    helpmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About...", command=About)

   # Main window     
    main.title("Main Widget")
    main["padx"] = 40
    main["pady"] = 2 
    
    textFrame = Frame(main)
    textFrame.pack()
    
    # Label - Time of arrival
    l1 = Label(textFrame)
    l1["text"] = "Enter time of arrival:"
    l1.grid(row=0, column=0)

    # Time of arrival - entry widget
    e1 = Entry(textFrame)
    e1["width"] = 5
    e1.bind("<Button-1>", AddTime1 )
    e1.bind("<Shift-1>", AddTime15 )
    e1.bind("<Button-3>", SubTime1 )
    e1.bind("<Shift-3>", SubTime15 )
    e1.grid(row=0, column=1)
    e1.insert(0, "6:00")
    e1.config(bg="white")
   
    # Label for lenght of work
    l2 = Label(textFrame)
    l2["text"] = "How long will you work?:"
    l2.grid(row=1, column=0)
    
    # Lenght of work - entry widget
    e2 = Entry(textFrame)
    e2["width"] = 5
    e2.bind("<Button-1>", AddTime1 )
    e2.bind("<Shift-1>", AddTime15 )
    e2.bind("<Button-3>", SubTime1 )
    e2.bind("<Shift-3>", SubTime15 )
    e2.grid(row=1, column=1)
    e2.insert(0, "8:00")
    e2.config(bg="white")

    # Label for lunchtime lenght
    l3 = Label(textFrame)
    l3["text"] = "And lunch? :"
    l3.grid(row=1, column=4)

    # Lunchtime - entry widget    
    e3 = Entry(textFrame)
    e3["width"] = 2
    e3.bind("<Button-1>", AddTime1 )
    e3.bind("<Shift-1>", AddTime15 )
    e3.bind("<Button-3>", SubTime1 )
    e3.bind("<Shift-3>", SubTime15 )
    e3.grid(row=1, column=5)
    e3.insert(0, "30")
    e3.config(bg="white")

    # Label for lunchtime unit of measure   
    l4 = Label(textFrame)
    l4["text"] = "minutes"
    l4.grid(row=1, column=6)
    
    textFrame.pack()

# Just clock - to be removed in final version    
clock = Label(main, font=('times', 20, 'bold'), bg='green')
clock.pack(fill=BOTH, expand=1)

def tick():
    s = time.strftime('%H:%M:%S') 
    if s != clock["text"]:
        clock["text"] = s
    clock.after(200, tick)
tick()

# Display time left in work - update acc. to PC version
showtime = Label(main, font=('times', 20, 'bold'), bg='yellow')
showtime.pack(fill=BOTH, expand=1)

def tick1():
    now = dt.datetime.now()
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
        break
    
# work time    
    while True:
        try:
            t_work = str(e2.get())
            t_work_h, t_work_m = t_work.split(':') 
            val3 = int(t_work_h)
            val4 = int(t_work_m)
            break
        except (ValueError):
            t_work_h = "08"
            t_work_m = "00"
        break
    
# lunch break
    while True:
        try:
            t_lunch = e3.get()
            break
        except (ValueError):
            t_lunch = "30"
        break
    
#variables preparation
    t_now = h1 + ":" + m1 + ":" + s1
    t_ar= t_in_h + ":" + t_in_m + ":00"
    t_m = dt.timedelta(minutes=int(t_work_m)) + dt.timedelta(minutes=int(t_lunch))
    t_w_h, t_w_m, t_w_s = str(t_m).split(':')
    time_working = str(int(t_work_h) + int(t_w_h)) + ":" + str(t_w_m) + ":00"
    fmt = '%H:%M:%S'

#time values calculation and check
    time_lost = dt.datetime.strptime(str(t_now), str(fmt)) - dt.datetime.strptime(t_ar, fmt)
    time_lost1 = dt.datetime.strptime(str(time_working), str(fmt)) - dt.datetime.strptime(str(time_lost), str(fmt))
    time_home = dt.datetime.strptime(str(t_now), str(fmt)) + time_lost1
    time_print = dt.datetime.time(time_home)
    showtime = time_lost1 - dt.datetime.timedelta.days(time_lost1)

    if print_finished != showtime["text"]:
        showtime["text"] = print_finished
        showtime.after(200, tick1)
tick1()

main.mainloop()
