from tkinter import *
import time
import sys
import datetime as dt
from datetime import timedelta

ABOUT_TEXT = "Go Home program\n \n Version 2.0 beta\n \n How to use:\n Adjust time value by clicking on it.\n Left-click to add 1 minute\n Shift+Left-click to add 15 minutes\n Right-click to substract 1 minute\n Shift+Right-click to substract 15 minutes\n"

#Global variables
    #Entry widget number
enum = 0
    #Entry widget value export
eexp = 0

def Set_Enum_1(event):
    global enum
    enum = 1
    
def Set_Enum_2(event):
    global enum
    enum = 2

def Export1():
    global eexp
    if enum == 1:
        eexp = str(e1.get())
    else:
        eexp = str(e2.get())
    
#Add 1 minute to timer
def AddTime1():
    v1 = eexp
    v1_h, v1_m = v1.split(':') 
    v1_h1 = int(v1_h)
    v1_m1 = int(v1_m) + 1
    
    if v1_m1 > 59:
        v2_h = int(v1_h1 + (v1_m1 // 60))
        v2_m = int(v1_m1 - 60)
    elif v1_h1 > 22:
        v2_h = 22
        v2_m = v1_m1
    elif v1_h1 < 2:
        v2_h = 2
        v2_m = v1_m1
    else:
        v2_h = v1_h1
        v2_m = v1_m1
  
    time_add = (str(dt.timedelta(hours=v2_h, minutes=v2_m)))[:-3]
    
    if enum == 1:
        e1.configure(state="normal")
        e1.delete(0,END)
        e1.insert(0,time_add)
        e1.configure(state="readonly")
    
    else:
        e2.configure(state="normal")
        e2.delete(0,END)
        e2.insert(0,time_add)
        e2.configure(state="readonly")

#Add 15 minutes to timer
def AddTime15():
    v1 = eexp
    v1_h, v1_m = v1.split(':') 
    v1_h1 = int(v1_h)
    v1_m1 = int(v1_m) + 15
    
    if v1_m1 > 59:
        v2_h = int(v1_h1 + (v1_m1 // 60))
        v2_m = int(v1_m1 - 60)
    elif v1_h1 > 22:
        v2_h = 22
        v2_m = v1_m1
    elif v1_h1 < 2:
        v2_h = 2
        v2_m = v1_m1
    else:
        v2_h = v1_h1
        v2_m = v1_m1
        
    time_add = (str(dt.timedelta(hours=v2_h, minutes=v2_m)))[:-3]
        
    if enum == 1:
        e1.configure(state="normal")
        e1.delete(0,END)
        e1.insert(0,time_add)
        e1.configure(state="readonly")
    
    else:
        e2.configure(state="normal")
        e2.delete(0,END)
        e2.insert(0,time_add)
        e2.configure(state="readonly")
    
def SubTime1():
    v1 = eexp
    v1_h, v1_m = v1.split(':') 
    v1_h1 = int(v1_h)
    v1_m1 = int(v1_m) - 1
    
    if v1_m1 < 0:
        v1_m1 = 59
        v2_h = int(v1_h1 - 1)
        v2_m = int(v1_m1)
    elif v1_h1 > 22:
        v2_h = 22
        v2_m = v1_m1
    elif v1_h1 < 2:
        v2_h = 2
        v2_m = v1_m1
    else:
        v2_h = v1_h1
        v2_m = v1_m1
        
    time_add = (str(dt.timedelta(hours=v2_h, minutes=v2_m)))[:-3]
        
    if enum == 1:
        e1.configure(state="normal")
        e1.delete(0,END)
        e1.insert(0,time_add)
        e1.configure(state="readonly")
    
    else:
        e2.configure(state="normal")
        e2.delete(0,END)
        e2.insert(0,time_add)
        e2.configure(state="readonly")
    
def SubTime15():
    v1 = eexp
    v1_h, v1_m = v1.split(':') 
    v1_h1 = int(v1_h)
    v1_m1 = int(v1_m) - 15
    
    if v1_m1 < 0:
        v1_m1 = v1_m1 + 60
        v2_h = int(v1_h1 - 1)
        v2_m = int(v1_m1)
    elif v1_h1 > 22:
        v2_h = 22
        v2_m = v1_m1
    elif v1_h1 < 2:
        v2_h = 2
        v2_m = v1_m1
    else:
        v2_h = v1_h1
        v2_m = v1_m1
        
    time_add = (str(dt.timedelta(hours=v2_h, minutes=v2_m)))[:-3]
        
    if enum == 1:
        e1.configure(state="normal")
        e1.delete(0,END)
        e1.insert(0,time_add)
        e1.configure(state="readonly")
    
    else:
        e2.configure(state="normal")
        e2.delete(0,END)
        e2.insert(0,time_add)
        e2.configure(state="readonly")
        
def AddTime1c(event):
    Export1()
    AddTime1()
    
def AddTime15c(event):
    Export1()
    AddTime15()
    
def SubTime1c(event):
    Export1()
    SubTime1()
    
def SubTime15c(event):
    Export1()
    SubTime15()
    
#This section is for minutes only!
    
#Add 1 minute to timer
def AddTime1m(event):
    v1 = str(e3.get())
    v1_m1 = int(v1) + 1
    
    if v1_m1 < 59:
        v2_m = v1_m1
    else:
        v2_m = 59
  
    time_add = (str(dt.timedelta(minutes=v2_m)))[2:-3]
    e3.configure(state="normal")
    e3.delete(0,END)
    e3.insert(0,time_add)
    e3.configure(state="readonly")

#Add 15 minutes to timer
def AddTime15m(event):
    v1 =str(e3.get())
    v1_m1 = int(v1) + 15
    
    if v1_m1 < 59:
        v2_m = v1_m1
    else:
        v2_m = 59
        
    time_add = (str(dt.timedelta(minutes=v2_m)))[2:-3]
    e3.configure(state="normal")
    e3.delete(0,END)
    e3.insert(0,time_add)
    e3.configure(state="readonly")
      
def SubTime1m(event):
    v1 =str(e3.get())
    v1_m1 = int(v1) - 1
    
    if v1_m1 < 30:
        v2_m = 30
    else:
        v2_m = v1_m1
        
    time_add = (str(dt.timedelta(minutes=v2_m)))[2:-3]
    e3.configure(state="normal")
    e3.delete(0,END)
    e3.insert(0,time_add)
    e3.configure(state="readonly")
    
def SubTime15m(event):
    v1 =str(e3.get())
    v1_m1 = int(v1) - 15
    
    if v1_m1 < 30:
        v2_m = 30
    else:
        v2_m = v1_m1
        
    time_add = (str(dt.timedelta(minutes=v2_m)))[2:-3]
    e3.configure(state="normal")
    e3.delete(0,END)
    e3.insert(0,time_add)
    e3.configure(state="readonly")    

def bQuit():
    name = quit()
    print (name)
    
def About():
    about = Toplevel()
    about.title("About")
    inside = Label(about, text=ABOUT_TEXT )
    inside.pack(side="top", fill="both")
    leave = Button (about, text="I GET IT", command=about.destroy)
    leave.pack(side="bottom", fill="both")

if __name__ == "__main__":

    main = Tk()
    main.resizable = (width = FALSE, height = FALSE)
    menu = Menu(main)
    main.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Exit", command=main.quit)

    helpmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About...", command=About)
    
    
    main.title("Go Home!")
    main["padx"] = 2
    main["pady"] = 2 
    
    # Create a text frame to hold the text Label and the Entry widget
    textFrame = Frame(main)
    textFrame.pack()
       
    #Create a Label in textFrame
    l1 = Label(textFrame)
    l1["text"] = "Enter time of arrival:"
    l1.grid(row=0, column=0)

    # Create an Entry Widget in textFrame
    e1 = Entry(textFrame)
    e1["width"] = 5
    e1.bind("<Enter>", Set_Enum_1 )
    e1.bind("<Button-1>", AddTime1c )
    e1.bind("<Shift-1>", AddTime15c )
    e1.bind("<Button-3>", SubTime1c )
    e1.bind("<Shift-3>", SubTime15c )
    e1.grid(row=0, column=1)
    e1.insert(0, "6:00")
    e1.config(bg="white", state="readonly")
    
    #Create a Label in textFrame
    l2 = Label(textFrame)
    l2["text"] = "How long will you work?:"
    l2.grid(row=1, column=0)
    
    # Create an Entry Widget in textFrame
    e2 = Entry(textFrame)
    e2["width"] = 5
    e2.bind("<Enter>", Set_Enum_2 )
    e2.bind("<Button-1>", AddTime15c )
    e2.bind("<Button-3>", SubTime15c )
    e2.grid(row=1, column=1)
    e2.insert(0, "8:00")
    e2.config(bg="white", state="readonly")

    l3 = Label(textFrame)
    l3["text"] = "And lunch? :"
    l3.grid(row=1, column=4)
    
    e3 = Entry(textFrame)
    e3["width"] = 2
    e3.bind("<Button-1>", AddTime1m )
    e3.bind("<Shift-1>", AddTime15m )
    e3.bind("<Button-3>", SubTime1m )
    e3.bind("<Shift-3>", SubTime15m )
    e3.grid(row=1, column=5)
    e3.insert(0, "30")
    e3.config(bg="white", state="readonly")
    
    l4 = Label(textFrame)
    l4["text"] = "minutes"
    l4.grid(row=1, column=6)
    

    textFrame.pack()
    
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
    tmin = dt.datetime(year=1999, month=1, day=1, hour=0, minute=0, second=0)
    
#time values calculation and check
    time_lost = dt.datetime.strptime(str(t_now), str(fmt)) - dt.datetime.strptime(t_ar, fmt)
    time_lost1 = dt.datetime.strptime(str(time_working), str(fmt)) - dt.datetime.strptime(str(time_lost), str(fmt))
    time_home = dt.datetime.strptime(str(t_now), str(fmt)) + time_lost1
    time_print = dt.datetime.time(time_home)
    time_total = tmin + time_lost1
    showtime1 = (time_total).time()

#exceptions handling 
    while True:
            set1 = time_total.year
            if set1 < 1999:
                print_finished = "Go Home"
            else: 
                print_finished = showtime1
            break
        
    if print_finished != showtime:["text"]
    showtime["text"] = print_finished
    showtime.after(200, tick1)
tick1()

main.mainloop()
