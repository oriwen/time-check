import tkinter as tk
import time
import sys
import datetime as dt
from datetime import timedelta
import os.path, os
import configparser
from tkinter import colorchooser, messagebox
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver

#Global variables
    #Entry widget number
enum = 0
    #Entry widget value export
eexp = 0

ABOUT_TEXT ="""
            Go Home! v2.0Beta2 
          created by Adam Slivka
          
    For licence see LICENCE.TXT 
    For detailed info about program, 
    controls and all its parts see README.TXT 
    and GoHome!_User_manual.pdf"""

def popupmsg():
    popup = tk.Tk()
    popup.wm_title("!")
    label = tk.Label(popup, text="Not yet implemented")
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()
    
def popupabout():
    popup = tk.Tk()
    popup.wm_title("About")
    label = tk.Label(popup, text=ABOUT_TEXT)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

class TimeWindow(tk.Tk):
        
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        tk.Tk.wm_title(self, "Go Home! Testing version")
 
        cvar1 = 0
        
        fname = "config.ini"
        checkconfig = os.path.isfile(fname)
        
        if checkconfig == True:
            pass
        else:
            config = configparser.ConfigParser()
            config["preset"] = {"arrival_time":"6:00", "work_time":"8:00","lunch_break":"30"}
            config['setup'] = {"stay_on_top":"0"}
            config['visual'] = {"color1":"green","color2":"yellow" }
            config['login'] = {"username":"user", "url":"http://czbrq-s-apl0007.cz.abb.com:8080/reports/login.jsp"}
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        
        config = configparser.ConfigParser()
        config.read("config.ini")
        cvar1 = int(config["setup"]["stay_on_top"])
        
        if cvar1 == 1:
            tk.Tk.wm_attributes(self, "-topmost", 1)
        else:
            pass
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        
        for F in (MainWindow, SetupWindow, LoginWindow):
        
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
  
            time_add = str((str(dt.timedelta(hours=v2_h, minutes=v2_m)))[:-3])
    
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
        
            time_add = str((str(dt.timedelta(hours=v2_h, minutes=v2_m)))[:-3])
        
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
        
            time_add = str((str(dt.timedelta(hours=v2_h, minutes=v2_m)))[:-3])
        
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
        
            time_add = str((str(dt.timedelta(hours=v2_h, minutes=v2_m)))[:-3])
        
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
  
            time_add = str((str(dt.timedelta(minutes=v2_m)))[2:-3])
            ev3.set(time_add)
    
        def AddTime15m(self):
            v1 =str(e3.get())
            v1_m1 = int(v1) + 15
    
            if v1_m1 < 59:
                v2_m = v1_m1
            else:
                v2_m = 59
        
            time_add = str((str(dt.timedelta(minutes=v2_m)))[2:-3])
            ev3.set(time_add)
    
        def SubTime1m(self):
            v1 =str(e3.get())
            v1_m1 = int(v1) - 1
    
            if v1_m1 < 30:
                v2_m = 30
            else:
                v2_m = v1_m1
        
            time_add = str((str(dt.timedelta(minutes=v2_m)))[2:-3])
            ev3.set(time_add)
    
        def SubTime15m(self):
            v1 =str(e3.get())
            v1_m1 = int(v1) - 15
    
            if v1_m1 < 30:
                v2_m = 30
            else:
                v2_m = v1_m1
        
            time_add = str((str(dt.timedelta(minutes=v2_m)))[2:-3])
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
            config = configparser.ConfigParser()
            config.read("config.ini")
            config.set("preset", "arrival_time", e1.get())
            config.set("preset", "work_time", e2.get())
            config.set("preset", "lunch_break", e3.get())
            with open("config.ini", "w") as configfile:
                config.write(configfile)
        
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
        
        button5 = tk.Button(self, text="Login", fg="red", command=lambda: controller.show_frame(LoginWindow))
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
        
        config = configparser.ConfigParser()
        config.read("config.ini")
        ev1_time = (config["preset"]["arrival_time"])
        ev2_time = (config["preset"]["work_time"])
        ev3_time = (config["preset"]["Lunch_break"])
        ev1.set(ev1_time)
        ev2.set(ev2_time)
        ev3.set(ev3_time)
        color1_temp = str((config["visual"]["color1"]))
        color2_temp = str((config["visual"]["color2"]))
        timeathome.configure(bg=color1_temp)
        timeleft.configure(bg=color2_temp)
        
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
            
# Must check under windows......
            
            if tk.Tk.wm_state(controller) == "iconic":
                tk.Tk.wm_state(controller, "icon")

        tick1()
                
class SetupWindow(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        cvar1 = tk.IntVar()
        color1 = tk.StringVar()
        color2 = tk.StringVar()
                
        def save():
            config = configparser.ConfigParser()
            config.read("config.ini")
            config.set("setup", "stay_on_top", str(cvar1.get()))
            config.set("visual", "color1", str(color1.get()))
            config.set("visual", "color2", str(color2.get()))
            with open("config.ini", "w") as configfile:
                config.write(configfile)
                
        def reset():
            python = sys.executable
            os.execl(python, python, * sys.argv)
            
        def save_reset():
            save()
            reset()
        
        def showsystem():
            cbutton1.grid(row=2, columnspan=4, sticky="w")
            buttons.grid(row=4, column=1, sticky="w")
            buttonsr.grid(row=4, column=2, sticky="w")
            button.grid(row=4, column=0, sticky="w")
            label.configure(text="Note that configuration will take effect after restart")
            label.grid(row=3, columnspan=7)
            buttonc1.grid_forget()
            buttonc2.grid_forget()
            labelc1.grid_forget()
            labelc2.grid_forget()
            
        def showvisual():
            label.configure(text="Note that configuration will take effect after restart")
            cbutton1.grid_forget()
            buttonc1.grid(row=2, column=0, sticky="w")
            buttonc2.grid(row=3, column=0, sticky="w")
            labelc1.grid(row=2, column=1, sticky="w")
            labelc2.grid(row=3, column=1, sticky="w")
            buttons.grid(row=5, column=1, sticky="w")
            buttonsr.grid(row=5, column=2, sticky="w")
            label.grid(row=4, columnspan=7)
            button.grid(row=5, column=0, sticky="w")
            
        def color1_choose():
            colorc1 = colorchooser.askcolor()
            color1_temp = colorc1[1]
            labelc1.configure(bg=color1_temp)
            color1.set(color1_temp)
            
        def color2_choose():
            colorc2 = colorchooser.askcolor()
            color2_temp = colorc2[1]
            labelc2.configure(bg=color2_temp)
            color2.set(color2_temp)
                
        selectbutton1 = tk.Button(self, text="System", command=showsystem)
        selectbutton1.grid(row=1, column=0, sticky="w")
        
        selectbutton2 = tk.Button(self, text="Visual", command=showvisual)
        selectbutton2.grid(row=1, column=1, sticky="w")
            
        label = tk.Label(self, text="Select category")
        label.grid(row=3, columnspan=7)
        
        cbutton1 = tk.Checkbutton(self, text="Stay on top", variable=cvar1)        
        
        buttons = tk.Button(self, text="Save", command=save)
        buttonsr = tk.Button(self, text="Save&Reset", command=save_reset)
        
        button = tk.Button(self, text="Go back", command=lambda: controller.show_frame(MainWindow))
        button.grid(row=4, column=0, sticky="w")
        
        buttonc1 = tk.Button(self, text="Color1", command=color1_choose)
        buttonc2 = tk.Button(self, text="Color2", command=color2_choose)
        
        labelc1 = tk.Label(self, text="14:30")
        labelc2 = tk.Label(self, text="3:45:56")
        
        config = configparser.ConfigParser()
        config.read("config.ini")
        cvar1_temp = (config["setup"]["stay_on_top"])
        cvar1.set(cvar1_temp)
        color1_temp = str((config["visual"]["color1"]))
        color2_temp = str((config["visual"]["color2"]))
        color1.set(color1_temp)
        color2.set(color2_temp)
        labelc1.configure(bg=color1_temp)
        labelc2.configure(bg=color2_temp)
        
class LoginWindow(tk.Frame):
    
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
        
        rem_login = tk.IntVar()
        rem_temp = 0
        login_OK = 1
        savedpath = tk.StringVar()
        
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
  
            time_add = str((str(dt.timedelta(hours=v2_h, minutes=v2_m)))[:-3])
    
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
        
            time_add = str((str(dt.timedelta(hours=v2_h, minutes=v2_m)))[:-3])
        
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
        
            time_add = str((str(dt.timedelta(hours=v2_h, minutes=v2_m)))[:-3])
        
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
        
            time_add = str((str(dt.timedelta(hours=v2_h, minutes=v2_m)))[:-3])
        
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
  
            time_add = str((str(dt.timedelta(minutes=v2_m)))[2:-3])
            ev3.set(time_add)
    
        def AddTime15m(self):
            v1 =str(e3.get())
            v1_m1 = int(v1) + 15
    
            if v1_m1 < 59:
                v2_m = v1_m1
            else:
                v2_m = 59
        
            time_add = str((str(dt.timedelta(minutes=v2_m)))[2:-3])
            ev3.set(time_add)
    
        def SubTime1m(self):
            v1 =str(e3.get())
            v1_m1 = int(v1) - 1
    
            if v1_m1 < 30:
                v2_m = 30
            else:
                v2_m = v1_m1
        
            time_add = str((str(dt.timedelta(minutes=v2_m)))[2:-3])
            ev3.set(time_add)
    
        def SubTime15m(self):
            v1 =str(e3.get())
            v1_m1 = int(v1) - 15
    
            if v1_m1 < 30:
                v2_m = 30
            else:
                v2_m = v1_m1
        
            time_add = str((str(dt.timedelta(minutes=v2_m)))[2:-3])
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
            config = configparser.ConfigParser()
            config.read("config.ini")
            config.set("preset", "arrival_time", e1.get())
            config.set("preset", "work_time", e2.get())
            config.set("preset", "lunch_break", e3.get())
            with open("config.ini", "w") as configfile:
                config.write(configfile)
                
        def loginaction():
            l1.grid(row=0, column=0)
            e1.grid(row=0, column=1, pady=4)
            l2.grid(row=1, column=0)
            e2.grid(row=1, column=1, pady=4)
            l3.grid(row=1, column=4)
            e3.grid(row=1, column=5)
            l4.grid(row=1, column=6, padx=2)
            timeathome.grid(row=2, columnspan=7, sticky="nsew")
            timeleft.grid(row=3, columnspan=7, sticky="nsew")
            loginlabel.grid_forget()
            loginentry.grid_forget()
            passlabel.grid_forget()
            passentry.grid_forget()
            
        def loginattempt():
            username = 1610616 #loginentry.get()
            password = 1610616 #passentry.get()
            phantom_driver = "/NonEncryptedData/python/data/phantomjs.exe"
            browser = webdriver.PhantomJS(phantom_driver, service_args=['--ignore-ssl-errors=true'])
            url = "http://czbrq-s-apl0007.cz.abb.com:8080/reports/login.jsp"
            browser.get(url)
            browser.find_element_by_id("uname").clear()
            browser.find_element_by_id("uname").send_keys(username)
            browser.find_element_by_id("pass").clear()
            browser.find_element_by_id("pass").send_keys(password)
            browser.find_element_by_css_selector('input[type=\"submit\"]').click()
            url1 = browser.current_url
            browser.switch_to.frame(browser.find_element_by_name("report"))
            content = browser.page_source
            browser.quit()
            soup=BeautifulSoup(content, "lxml")
            table = soup.find('table', {'class': 'data'})
            pretty = table.prettify()
            print(pretty)
            
            if rem_temp == 1:
                config = configparser.ConfigParser()
                config.read("config.ini")
                config.set("login", "username", loginentry.get())
                with open("config.ini", "w") as configfile:
                    config.write(configfile)
            else:
                pass
        
            
        def loginaction_final():
            loginattempt()
            if login_OK == 0:
                loginaction()
            else:
                pass
            
        def rem():
            pass
            
        l1 = tk.Label(self, text="You have arrived at: ")
        
        e1 = tk.Entry(self)
        e1["width"] = 5
        e1.bind("<Enter>", Set_Enum_1 )
        e1.bind("<Button-1>", AddTime1c )
        e1.bind("<Shift-1>", AddTime15c )
        e1.bind("<Button-3>", SubTime1c )
        e1.bind("<Shift-3>", SubTime15c )
        e1.config(bg="white", state="readonly", textvariable = ev1)
        
        button1 = tk.Button(self, text=">", fg="red", command=show_buttons)
        button1.grid(row=0, column=6)
        button1.lower()
        
        button2 = tk.Button(self, text="<", fg="red", command=hide_buttons)
        button2.grid(row=0, column=6)

        button3 = tk.Button(self, text="Main", fg="red", command=lambda: controller.show_frame(MainWindow))
        button3.grid(row=0, column=7)
        
        button4 = tk.Button(self, text="Setup", fg="red", command=lambda: controller.show_frame(SetupWindow))
        button4.grid(row=1, column=7)
        
        button5 = tk.Button(self, text="Login", fg="red", command=popupmsg)
        button5.grid(row=2, column=7)
        
        button6 = tk.Button(self, text="About", fg="red", command=popupabout)
        button6.grid(row=3, column=7)
        
        l2 = tk.Label(self)
        l2["text"] = "How long will you work?:"
    
        e2 = tk.Entry(self)
        e2["width"] = 5
        e2.bind("<Enter>", Set_Enum_2 )
        e2.bind("<Button-1>", AddTime15c )
        e2.bind("<Button-3>", SubTime15c )
        e2.config(bg="white", state="readonly", textvariable = ev2)

        l3 = tk.Label(self)
        l3["text"] = "And lunch? :"

        e3 = tk.Entry(self)
        e3["width"] = 2
        e3.bind("<Button-1>", AddTime1m )
        e3.bind("<Shift-1>", AddTime15m )
        e3.bind("<Button-3>", SubTime1m )
        e3.bind("<Shift-3>", SubTime15m )
        e3.config(bg="white", state="readonly", textvariable = ev3)
    
        l4= tk.Label(self)
        l4["text"] = "minutes"
        
        timeathome = tk.Label(self)
        timeathome.configure(text="Sample", bg="green", font=("Font",20))
        
        timeleft = tk.Label(self)
        timeleft.configure(text="Sample", bg="yellow", font=("Font",20))
        
        loginlabel = tk.Label(self, text="Osobní číslo")
        loginlabel.grid(row=0, column=1)
        
        loginentry = tk.Entry(self)
        loginentry["width"] = 10
        loginentry.grid(row=0, column=2)
        
        remember = tk.Checkbutton(self, text="Remember me", variable=rem)
        remember.grid(row=0, column=3)
        
        passlabel = tk.Label(self, text="Heslo")
        passlabel.grid(row=1, column=1)
        
        passentry = tk.Entry(self)
        passentry["width"] = 15
        passentry.grid(row=1, column=2)
        
        loginbutton = tk.Button(self, text = "Login", command=loginaction_final)
        loginbutton.grid(row=2, columnspan=2)
        
        config = configparser.ConfigParser()
        config.read("config.ini")
        ev1_time = (config["preset"]["arrival_time"])
        ev2_time = (config["preset"]["work_time"])
        ev3_time = (config["preset"]["lunch_break"])
        ev1.set(ev1_time)
        ev2.set(ev2_time)
        ev3.set(ev3_time)
        color1_temp = str((config["visual"]["color1"]))
        color2_temp = str((config["visual"]["color2"]))
        timeathome.configure(bg=color1_temp)
        timeleft.configure(bg=color2_temp)
        savedpath_temp = (config["login"]["url"])
        savedpath.set(savedpath_temp)
        
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
            
# Must check under windows......not working right...
            
            if tk.Tk.wm_state(controller) == "iconic":
                tk.Tk.iconify()

        tick1()
        
app = TimeWindow()
app.resizable(0,0)
app.mainloop()
