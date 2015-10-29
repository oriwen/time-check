import tkinter as tk
from tkinter import ttk
import time
import sys
import datetime as dt
from datetime import timedelta
import shelve

#Global variables
    #Entry widget number
enum = 0
    #Entry widget value export
eexp = 0

def popupmsg():
    popup = tk.Tk()
    popup.wm_title("!")
    label = tk.Label(popup, text="Not yet implemented")
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()
    
def popupabout():
    popup = tk.Tk()
    popup.wm_title("About")
    label = tk.Label(popup, text="Go Home! v2.0Beta2 \n \n created by Adam Slivka \n \n For licence see LICENCE.TXT \n For detailed info about program, controls and \n all its parts see README.TXT and User_manual.rtf")
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop() 
    
class TimeWindow(tk.Tk):
        
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        tk.Tk.wm_title(self, "Go Home! Testing version")
 
#This may work on windows...must try.... 
        cvar1m = tk.IntVar()
        
        try:
            safem = shelve.open("config")
            cvar1_tempm = safem["1s"]
            cvar1m.set(cvar1_tempm)
            safem.close()
        except AttributeError:
            pass
        
 #       if cvar1_tempm == 1:
 #           tk.Tk.wm_attributes("-topmost", 1)
 #       else:
 #           pass
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        
        for F in (MainWindow, SetupWindow):
        
            frame = F(container, self)
        
            self.frames[F] = frame
        
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(MainWindow)
        
    def show_frame(self, cont):
        
        frame = self.frames[cont]
        frame.tkraise()
                     
class MainWindow(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        e1_var = "6:00"
        e2_var = "8:00"
        e3_var = "30"
        
        ev1 = tk.StringVar()
        ev2 = tk.StringVar()
        ev3 = tk.StringVar()
        
        ev1.set(e1_var)
        ev2.set(e2_var)
        ev3.set(e3_var)
        
        def Set_Enum_1(self):
            global enum
            enum = 1
    
        def Set_Enum_2(self):
            global enum
            enum = 2
            
        def export1(self):
            global eexp
            if enum == 1:
                eexp = str(ev1.get())
            else:
                eexp = str(ev2.get())
                
        def AddTime1(self):
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
                ev1.set(time_add)
    
            else:
                ev2.set(time_add)
    
        def AddTime15(self):
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
                ev1.set(time_add)
    
            else:
                ev2.set(time_add)
    
        def SubTime1(self):
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
                ev1.set(time_add)
    
            else:
                ev2.set(time_add)
    
        def SubTime15(self):
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
                ev1.set(time_add)
    
            else:
                ev2.set(time_add)
    
        def AddTime1m(self):
            v1 = str(e3.get())
            v1_m1 = int(v1) + 1
    
            if v1_m1 < 59:
                v2_m = v1_m1
            else:
                v2_m = 59
  
            time_add = (str(dt.timedelta(minutes=v2_m)))[2:-3]
            ev3.set(time_add)
    
        def AddTime15m(self):
            v1 =str(e3.get())
            v1_m1 = int(v1) + 15
    
            if v1_m1 < 59:
                v2_m = v1_m1
            else:
                v2_m = 59
        
            time_add = (str(dt.timedelta(minutes=v2_m)))[2:-3]
            ev3.set(time_add)
    
        def SubTime1m(self):
            v1 =str(e3.get())
            v1_m1 = int(v1) - 1
    
            if v1_m1 < 30:
                v2_m = 30
            else:
                v2_m = v1_m1
        
            time_add = (str(dt.timedelta(minutes=v2_m)))[2:-3]
            ev3.set(time_add)
    
        def SubTime15m(self):
            v1 =str(e3.get())
            v1_m1 = int(v1) - 15
    
            if v1_m1 < 30:
                v2_m = 30
            else:
                v2_m = v1_m1
        
            time_add = (str(dt.timedelta(minutes=v2_m)))[2:-3]
            ev3.set(time_add)
                
        def AddTime1c(self):
            export1(self)
            AddTime1(self)
    
        def AddTime15c(self):
            export1(self)
            AddTime15(self)
    
        def SubTime1c(self):
            export1(self)
            SubTime1(self)
    
        def SubTime15c(self):
            export1(self)
            SubTime15(self)
            
        def show_buttons():
            button1.grid_forget() 
            button2.grid(row=0, column=6)  
            button3.grid(row=0, column=7)
            button4.grid(row=1, column=7)  
            button5.grid(row=2, column=7)
            button6.grid(row=3, column=7)
              
        def hide_buttons():
            button1.grid(row=0, column=6)  
            button2.grid_forget()   
            button3.grid_forget()
            button4.grid_forget()  
            button5.grid_forget()
            button6.grid_forget()
            
        def savetime():
            safetime = shelve.open("config")
            safetime["1e"] = ev1.get()
            safetime["2e"] = ev2.get()
            safetime["3e"] = ev3.get()
            safetime.close()
        
        l1 = tk.Label(self, text="You have arrived at: ")
        l1.grid(row=0, column=0)
        
        e1 = tk.Entry(self)
        e1["width"] = 5
        e1.bind("<Enter>", Set_Enum_1 )
        e1.bind("<Button-1>", AddTime1c )
        e1.bind("<Shift-1>", AddTime15c )
        e1.bind("<Button-3>", SubTime1c )
        e1.bind("<Shift-3>", SubTime15c )
        e1.grid(row=0, column=1, pady=4)
        e1.config(bg="white", state="readonly", textvariable = ev1)
        
        button1 = tk.Button(self, text=">", fg="red", command=show_buttons)
        button1.grid(row=0, column=6)
        button1.lower()
        
        button2 = tk.Button(self, text="<", fg="red", command=hide_buttons)
        button2.grid(row=0, column=6)

        button3 = tk.Button(self, text="Setup", fg="red", command=lambda: controller.show_frame(SetupWindow))
        button3.grid(row=0, column=7)
        
        button4 = tk.Button(self, text="Save", fg="red", command=savetime)
        button4.grid(row=1, column=7)
        
        button5 = tk.Button(self, text="Login", fg="red", command=popupmsg)
        button5.grid(row=2, column=7)
        
        button6 = tk.Button(self, text="About", fg="red", command=popupabout)
        button6.grid(row=3, column=7)
        
    #Create a Label in textFrame
        l2 = tk.Label(self)
        l2["text"] = "How long will you work?:"
        l2.grid(row=1, column=0)
    
    # Create an Entry Widget in textFrame
        e2 = tk.Entry(self)
        e2["width"] = 5
        e2.bind("<Enter>", Set_Enum_2 )
        e2.bind("<Button-1>", AddTime15c )
        e2.bind("<Button-3>", SubTime15c )
        e2.grid(row=1, column=1, pady=4)
        e2.config(bg="white", state="readonly", textvariable = ev2)

        l3 = tk.Label(self)
        l3["text"] = "And lunch? :"
        l3.grid(row=1, column=4)

        e3 = tk.Entry(self)
        e3["width"] = 2
        e3.bind("<Button-1>", AddTime1m )
        e3.bind("<Shift-1>", AddTime15m )
        e3.bind("<Button-3>", SubTime1m )
        e3.bind("<Shift-3>", SubTime15m )
        e3.grid(row=1, column=5)
        e3.config(bg="white", state="readonly", textvariable = ev3)
    
        l4= tk.Label(self)
        l4["text"] = "minutes"
        l4.grid(row=1, column=6, padx=2)
        
        timeathome = tk.Label(self)
        timeathome.configure(text="Sample", bg="green", font=("Font",20))
        timeathome.grid(row=2, columnspan=7, sticky="nsew")        
        
        timeleft = tk.Label(self)
        timeleft.configure(text="Sample", bg="yellow", font=("Font",20))
        timeleft.grid(row=3, columnspan=7, sticky="nsew")
        
        try:
            safetime = shelve.open("config")
            ev1_time = safetime["1e"]
            ev2_time = safetime["2e"]
            ev3_time = safetime["3e"]
            ev1.set(ev1_time)
            ev2.set(ev2_time)
            ev3.set(ev3_time)
            safetime.close()
        except AttributeError:
            pass
        except KeyError:
            pass
        
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
    
            timeleft.config(text=str(time_print))
    
            if print_finished != timeleft:["text"]
            timeleft["text"] = print_finished
            timeleft.after(200, tick1)
            
            timeathome.config(text=str(time_print))
    
            if print_finished != timeathome:["text"]
            timeathome["text"] = time_print

        tick1()
                
class SetupWindow(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global cvar1
        cvar1 = tk.IntVar()
                
        def save():
            safe = shelve.open("config")
            safe["1s"] = cvar1.get()
            safe.close()
            
        label = tk.Label(self, text="Here I will add configuration options")
        label.grid(row=0, column=0)
        
        cbutton1 = tk.Checkbutton(self, text="Stay on top", variable=cvar1)
        cbutton1.grid(row=1, column=0)        
        
        buttons = tk.Button(self, text="Save", command=save)
        buttons.grid(row=2, column=1)
        
        button = tk.Button(self, text="Go back", command=lambda: controller.show_frame(MainWindow))
        button.grid(row=2, column=2)
        
        try:
            safe = shelve.open("config")
            cvar1_temp = safe["1s"]
            cvar1.set(cvar1_temp)
            safe.close()
        except AttributeError:
            pass
        
app = TimeWindow()
app.resizable(0,0)
app.mainloop()
