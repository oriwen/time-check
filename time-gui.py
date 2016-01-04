# -*- coding: cp1250 -*-

import tkinter as tk
import time
import sys
import datetime as dt
from datetime import timedelta
import os.path, os
import configparser
from tkinter import colorchooser, messagebox, filedialog
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from PIL import ImageTk, Image
import subprocess
import shutil
import zipfile

#Global variables
    #Entry widget number
enum = 0
    #Entry widget value export
eexp = 0
    #Path to data directory
global base_path
base_path = ""

funame = "updater.exe"
root_dir1 = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]+"/data/"
root_dir2 = os.getcwd()+"/data/"
ulocation1 = os.path.exists(root_dir1+"/"+funame)
ulocation2 = os.path.exists(root_dir2+funame)
        
if ulocation1 == True:
    base_path = root_dir1
elif ulocation2 == True:
    base_path = root_dir2
else:
    messagebox.showerror("Error","update.exe not present in data folder, reinstall program")    

ABOUT_TEXT ="""
                Go Home! v2.0 
            created by Adam Slivka
          
    For information about licence, philosophy,
and all parts of program see GoHome!_User_manual.pdf.
     """

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
        
        checkconfig = os.path.exists(base_path+"config.ini")
        
        if checkconfig == True:
            pass
        else:
            config = configparser.ConfigParser()
            config["preset"] = {"arrival_time":"6:00", "work_time":"8:00","lunch_break":"0:30"}
            config['setup'] = {"stay_on_top":"0"}
            config['visual'] = {"color1":"green","color2":"yellow" }
            config['login'] = {"username":"", "url":"http://czbrq-s-apl0007.cz.abb.com:8080/reports/login.jsp", "remember":"1"}
            config['system'] = {"version":"2.0", "version_updater":"1", "autocheck":"0", "update_dir":"S:/adam.slivka/All/GoHome!/update"}
            with open(base_path+'config.ini', 'w') as configfile:
                config.write(configfile)
        
        config = configparser.ConfigParser()
        config.read(base_path+"config.ini")
        cvar1 = int(config["setup"]["stay_on_top"])
        cvar2 = int(config["system"]["autocheck"])
        ver_actual = config["system"]["version"]
        ver_upd = config["system"]["version_updater"]
        path_upd = config["system"]["update_dir"]
        
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

        def versioncheck():
        #Version checking
            update_proc = 1
            config = configparser.ConfigParser()
            config.read(base_path+"config.ini")
            path_upd = config["system"]["update_dir"]
            path = path_upd+"/updater.zip"
            try:
                with open(path_upd+"/update.txt","r") as ver_p:
                    version = ver_p.read()
            except FileNotFoundError:
                path_upd = "S:/adam.slivka/All/GoHome!/update"
                with open(path_upd+"/update.txt","r") as ver_p:
                    version = ver_p.read()
            try:
                with open(path_upd+"/updater.txt","r") as ver:
                    version_updater = ver.read()
            except FileNotFoundError:
                messagebox.showerror("Error","Update folder not found, set correct path in config.ini")
                
            d_1,d_2 = version.split('.')
            a_1,a_2 = ver_actual.split('.')
            if int(version_updater) > int(ver_upd):
                result = messagebox.askquestion("New version","New version available, update?")
                if result == "yes":
                    os.mkdir("tmp")
                    root_dir = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
                    shutil.copy2(path_upd+"/updater.zip", os.getcwd()+"/tmp")
                    file = os.getcwd()+"/tmp/updater.zip"
                    zip_ref = zipfile.ZipFile(file,"r")
                    zip_ref.extractall(os.getcwd()+"/tmp")
                    zip_ref.close()
                    shutil.copyfile("tmp/updater.exe",base_path+"updater.exe")
                    shutil.rmtree("tmp")
                    config = configparser.ConfigParser()
                    config.read(base_path+"config.ini")
                    config.set("system", "version_updater", version_updater)
                    with open(base_path+"config.ini", "w") as configfile:
                        config.write(configfile)
                    if int(d_2) > int(a_2):
                        subprocess.Popen(base_path+"updater.exe")
                        os._exit(-1)
                    else:
                        pass
                else:
                    update_proc = 0      
            else:
                pass    
            if int(d_1) >= int(a_1) and int(d_2) > int(a_2) and update_proc == 1:
                result = messagebox.askquestion("New version","New version available, update?")
                if result == "yes":
                    subprocess.Popen(base_path+"updater.exe")
                    os._exit(-1)
                else:
                    pass       
            else:
                pass

        if cvar2 == 1:
            versioncheck()
        else:
            pass

        
    def show_frame(self, cont):
        
        frame = self.frames[cont]
        frame.tkraise()
                     
class MainWindow(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        e1_var = "6:00"
        e2_var = "8:00"
        e3_var = "0:30"
        e5_var = "0:00"
        
        ev1 = tk.StringVar()
        ev2 = tk.StringVar()
        ev3 = tk.StringVar()
        ev5 = tk.StringVar()
        
        ev1.set(e1_var)
        ev2.set(e2_var)
        ev3.set(e3_var)
        ev5.set(e5_var)

        def Set_Enum_1(self):
            global enum
            enum = 1
    
        def Set_Enum_2(self):
            global enum
            enum = 2

        def Set_Enum_3(self):
            global enum
            enum = 3

        def Set_Enum_5(self):
            global enum
            enum = 5
            
        def export1(self):
            global eexp
            if enum == 1:
                eexp = str(ev1.get())
            elif enum == 2:
                eexp = str(ev2.get())
            elif enum == 3:
                eexp = str(ev3.get())
            else:
                eexp = str(ev5.get())
                
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

        def AddTime1m(self):
            v1 = eexp
            v1_h, v1_m = v1.split(':') 
            v1_h1 = int(v1_h)
            v1_m1 = int(v1_m) + 1

            if v1_m1 > 59:
                v2_h = int(v1_h1 + (v1_m1 // 60))
                v2_m = int(v1_m1 - 60)
            else:
                v2_h = v1_h1
                v2_m = v1_m1
                
            time_add = str((str(dt.timedelta(hours=v2_h, minutes=v2_m)))[:-3])

            if enum == 3:
                ev3.set(time_add)
            else:
                ev5.set(time_add)
    
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

        def AddTime15m(self):
            v1 = eexp
            v1_h, v1_m = v1.split(':') 
            v1_h1 = int(v1_h)
            v1_m1 = int(v1_m) + 15
    
            if v1_m1 > 59:
                v2_h = int(v1_h1 + (v1_m1 // 60))
                v2_m = int(v1_m1 - 60)
            else:
                v2_h = v1_h1
                v2_m = v1_m1
        
            time_add = str((str(dt.timedelta(hours=v2_h, minutes=v2_m)))[:-3])

            if enum == 3:
                ev3.set(time_add)
            else:
                ev5.set(time_add)
    
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

        def SubTime1m(self):
            v1 = eexp
            v1_h, v1_m = v1.split(':') 
            v1_h1 = int(v1_h)
            v1_m1 = int(v1_m) - 1
    
            if v1_m1 < 0:
                v1_m1 = 59
                v2_h = int(v1_h1 - 1)
                v2_m = int(v1_m1)
            else:
                v2_h = v1_h1
                v2_m = v1_m1

            if enum == 3:
                if v1_h1 == 0:
                    if v1_m1 < 30:
                        v2_m = 30
                        v2_h = 0
                    else:
                        v2_h = v1_h1
                        v2_m = v1_m1
        
            time_add = str((str(dt.timedelta(hours=v2_h, minutes=v2_m)))[:-3])

            if enum == 3:
                ev3.set(time_add)
            else:
                ev5.set(time_add)
    
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

        def SubTime15m(self):
            v1 = eexp
            v1_h, v1_m = v1.split(':') 
            v1_h1 = int(v1_h)
            v1_m1 = int(v1_m) - 15
    
            if v1_m1 < 0:
                v1_m1 = 59
                v2_h = int(v1_h1 - 1)
                v2_m = int(v1_m1)
            else:
                v2_h = v1_h1
                v2_m = v1_m1

            if enum == 3:
                if v1_h1 == 0:
                    if v1_m1 < 30:
                        v2_m = 30
                        v2_h = 0
                    else:
                        v2_h = v1_h1
                        v2_m = v1_m1
        
            time_add = str((str(dt.timedelta(hours=v2_h, minutes=v2_m)))[:-3])

            if enum == 3:
                ev3.set(time_add)
            else:
                ev5.set(time_add)
            
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

        def AddTime1cm(self):
            export1(self)
            AddTime1m(self)
    
        def AddTime15cm(self):
            export1(self)
            AddTime15m(self)
    
        def SubTime1cm(self):
            export1(self)
            SubTime1m(self)
    
        def SubTime15cm(self):
            export1(self)
            SubTime15m(self)
            
        def savetime():
            config = configparser.ConfigParser()
            config.read(base_path+"config.ini")
            config.set("preset", "arrival_time", e1.get())
            config.set("preset", "work_time", e2.get())
            config.set("preset", "lunch_break", e3.get())
            with open(base_path+"config.ini", "w") as configfile:
                config.write(configfile)
        
        l1 = tk.Label(self, text="Arrived at: ")
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
        
        image3 = ImageTk.PhotoImage(file = base_path+"setup_r.png")
        button3 = tk.Button(self, image=image3, fg="red", command=lambda: controller.show_frame(SetupWindow))
        button3.image = image3
        button3.grid(row=0, column=7)
        
        image4 = ImageTk.PhotoImage(file = base_path+"save_r.png")
        button4 = tk.Button(self, fg="red", command=savetime, image=image4)
        button4.image = image4
        button4.grid(row=1, column=7)
        
        image5 = ImageTk.PhotoImage(file = base_path+"login_r.png")
        button5 = tk.Button(self, fg="red", image=image5, command=lambda: controller.show_frame(LoginWindow))
        button5.image = image5
        button5.grid(row=2, column=7)
        
        image6 = ImageTk.PhotoImage(file = base_path+"about_r.png")
        button6 = tk.Button(self, fg="red", image=image6, command=popupabout)
        button6.image = image6
        button6.grid(row=3, column=7)

        l2 = tk.Label(self)
        l2["text"] = ",will work for:"
        l2.grid(row=0, column=2)

        e2 = tk.Entry(self)
        e2["width"] = 5
        e2.bind("<Enter>", Set_Enum_2 )
        e2.bind("<Button-1>", AddTime15c )
        e2.bind("<Button-3>", SubTime15c )
        e2.grid(row=0, column=3, pady=4)
        e2.config(bg="white", state="readonly", textvariable = ev2)

        l5 = tk.Label(self)
        l5["text"] = "Left work for:"
        l5.grid(row=1, column=0)

        e5 = tk.Entry(self)
        e5["width"] = 5
        e5.bind("<Enter>", Set_Enum_5 )
        e5.bind("<Button-1>", AddTime1cm )
        e5.bind("<Shift-1>", AddTime15cm )
        e5.bind("<Button-3>", SubTime1cm )
        e5.bind("<Shift-3>", SubTime15cm )
        e5.grid(row=1, column=1, pady=4)
        e5.config(bg="white", state="readonly", textvariable = ev5)

        l3 = tk.Label(self)
        l3["text"] = "And lunch? :"
        l3.grid(row=1, column=2)

        e3 = tk.Entry(self)
        e3["width"] = 5
        e3.bind("<Enter>", Set_Enum_3 )
        e3.bind("<Button-1>", AddTime1cm )
        e3.bind("<Shift-1>", AddTime15cm )
        e3.bind("<Button-3>", SubTime1cm )
        e3.bind("<Shift-3>", SubTime15cm )
        e3.grid(row=1, column=3)
        e3.config(bg="white", state="readonly", textvariable = ev3)
    
        l4= tk.Label(self)
        l4["text"] = "minutes"
        l4.grid(row=1, column=4, padx=2)
        
        timeathome = tk.Label(self)
        timeathome.configure(text="Sample", bg="green", font=("Font",20))
        timeathome.grid(row=2, columnspan=7, sticky="nsew")        
        
        timeleft = tk.Label(self)
        timeleft.configure(text="Sample", bg="yellow", font=("Font",20))
        timeleft.grid(row=3, columnspan=7, sticky="nsew")
        
        config = configparser.ConfigParser()
        config.read(base_path+"config.ini")
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
                    break
                except (ValueError):
                    t_work_h = "08"
                    t_work_m = "00"
                break
    
# lunch break
            while True:
                try:
                    t_lunch = e3.get()
                    t_lunch_h, t_lunch_m = t_lunch.split(':')
                    break
                except (ValueError):
                    t_lunch_h = "00"
                    t_lunch_m = "30"
                break
            
# work break
            while True:
                try:
                    t_break = e5.get()
                    t_break_h, t_break_m = t_break.split(':')
                    break
                except (ValueError):
                    pass
                break
#variables preparation
            t_now = h1 + ":" + m1 + ":" + s1
            t_ar= t_in_h + ":" + t_in_m + ":00"
            t_m = dt.timedelta(minutes=int(t_work_m)) + dt.timedelta(minutes=int(t_lunch_m))
            t_m1 = t_m + dt.timedelta(minutes=int(t_break_m))
            t_w_h, t_w_m, t_w_s = str(t_m1).split(':')
            time_working = str(int(t_work_h) + int(t_w_h) + int(t_lunch_h) + int(t_break_h)) + ":" + str(t_w_m) + ":00"
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
        cvar2 = tk.IntVar()
        color1 = tk.StringVar()
        color2 = tk.StringVar()
        dir_update = "S:/adam.slivka/All/GoHome!/update"

        def set_path():
            dir_update = tk.filedialog.askdirectory()
            config = configparser.ConfigParser()
            config.read(base_path+"config.ini")
            config.set("system", "update_dir", str(dir_update))
            with open(base_path+"config.ini", "w") as configfile:
                config.write(configfile)
            print(dir_update)
                
        def save():
            config = configparser.ConfigParser()
            config.read(base_path+"config.ini")
            config.set("setup", "stay_on_top", str(cvar1.get()))
            config.set("system", "autocheck", str(cvar2.get()))
            config.set("visual", "color1", str(color1.get()))
            config.set("visual", "color2", str(color2.get()))
            with open(base_path+"config.ini", "w") as configfile:
                config.write(configfile)
                
        def reset():
            python = sys.executable
            os.execl(python, python, * sys.argv)
            
        def save_reset():
            save()
            reset()
        
        def showsystem():
            cbutton1.grid(row=2, columnspan=4, sticky="w")
            cbutton2.grid_forget()
            buttonpath.grid_forget()
            buttons.grid(row=4, column=1, sticky="w")
            buttonsr.grid(row=4, column=2, sticky="w")
            button.grid(row=4, column=0, sticky="w")
            label.configure(text="Note that configuration will take effect after restart")
            label.grid(row=3, columnspan=7)
            buttonc1.grid_forget()
            buttonc2.grid_forget()
            labelc1.grid_forget()
            labelc2.grid_forget()

        def showupdates():
            cbutton1.grid_forget()
            cbutton2.grid(row=2, columnspan=4, sticky="w")
            buttonpath.grid(row=3, columnspan=4, sticky="w")
            buttons.grid(row=5, column=1, sticky="w")
            buttonsr.grid(row=5, column=2, sticky="w")
            button.grid(row=5, column=0, sticky="w")
            label.configure(text="Note that configuration will take effect after restart")
            label.grid(row=4, columnspan=7)
            buttonc1.grid_forget()
            buttonc2.grid_forget()
            labelc1.grid_forget()
            labelc2.grid_forget()
            
        def showvisual():
            label.configure(text="Note that configuration will take effect after restart")
            cbutton1.grid_forget()
            cbutton2.grid_forget()
            buttonpath.grid_forget()
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

        def goback():
            login_OK_temp = login_OK.get()
            if login_OK_temp == 1:
                controller.show_frame(LoginWindow)
            else:
                controller.show_frame(MainWindow)
                
        selectbutton1 = tk.Button(self, text="System", command=showsystem)
        selectbutton1.grid(row=1, column=0, sticky="w")
        
        selectbutton2 = tk.Button(self, text="Visual", command=showvisual)
        selectbutton2.grid(row=1, column=1, sticky="w")

        selectbutton3 = tk.Button(self, text="Updates", command=showupdates)
        selectbutton3.grid(row=1, column=2, sticky="w")
            
        label = tk.Label(self, text="Select category")
        label.grid(row=3, columnspan=7)
        
        cbutton1 = tk.Checkbutton(self, text="Stay on top", variable=cvar1)        
        cbutton2 = tk.Checkbutton(self, text="Auto-Update", variable=cvar2)
        
        buttons = tk.Button(self, text="Save", command=save)
        buttonsr = tk.Button(self, text="Save&Reset", command=save_reset)
        buttonpath = tk.Button(self, text="Path to updates", command=set_path)
        
        button = tk.Button(self, text="Go back", command=goback)
        button.grid(row=4, column=0, sticky="w")
        
        buttonc1 = tk.Button(self, text="Color1", command=color1_choose)
        buttonc2 = tk.Button(self, text="Color2", command=color2_choose)
        
        labelc1 = tk.Label(self, text="14:30")
        labelc2 = tk.Label(self, text="3:45:56")
        
        config = configparser.ConfigParser()
        config.read(base_path+"config.ini")
        cvar1_temp = (config["setup"]["stay_on_top"])
        cvar1.set(cvar1_temp)
        cvar2_temp = (config["system"]["autocheck"])
        cvar2.set(cvar2_temp)
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
        e3_var = "0:30"
        e5_var = "0:00"
        
        ev1 = tk.StringVar()
        ev2 = tk.StringVar()
        ev3 = tk.StringVar()
        ev5 = tk.StringVar()
        watt_start = "06:00" 
        
        ev1.set(e1_var)
        ev2.set(e2_var)
        ev3.set(e3_var)
        ev5.set(e5_var)
        
        rem_var = tk.IntVar()
        rem_temp = 0
        global login_OK
        login_OK = tk.IntVar()
        login_OK.set(0)
        login_temp = ""
        savedpath = tk.StringVar()

        lunch_load = 0
        t_out_time = "0:00:00"

        time_string = tk.StringVar()
        time_string.set("0:00:00")
        
        def Set_Enum_1(self):
            global enum
            enum = 1
    
        def Set_Enum_2(self):
            global enum
            enum = 2

        def Set_Enum_3(self):
            global enum
            enum = 3

        def Set_Enum_5(self):
            global enum
            enum = 5
            
        def export1(self):
            global eexp
            if enum == 1:
                eexp = str(ev1.get())
            elif enum == 2:
                eexp = str(ev2.get())
            elif enum == 3:
                eexp = str(ev3.get())
            else:
                eexp = str(ev5.get())
                
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
            v1 = eexp
            v1_h, v1_m = v1.split(':') 
            v1_h1 = int(v1_h)
            v1_m1 = int(v1_m) + 1

            if v1_m1 > 59:
                v2_h = int(v1_h1 + (v1_m1 // 60))
                v2_m = int(v1_m1 - 60)
            else:
                v2_h = v1_h1
                v2_m = v1_m1
                
            time_add = str((str(dt.timedelta(hours=v2_h, minutes=v2_m)))[:-3])

            if enum == 3:
                ev3.set(time_add)
            elif enum == 5:
                ev5.set(time_add)
            else:
                pass
                
        def AddTime15m(self):
            v1 = eexp
            v1_h, v1_m = v1.split(':') 
            v1_h1 = int(v1_h)
            v1_m1 = int(v1_m) + 15
    
            if v1_m1 > 59:
                v2_h = int(v1_h1 + (v1_m1 // 60))
                v2_m = int(v1_m1 - 60)
            else:
                v2_h = v1_h1
                v2_m = v1_m1
        
            time_add = str((str(dt.timedelta(hours=v2_h, minutes=v2_m)))[:-3])

            if enum == 3:
                ev3.set(time_add)
            elif enum == 5:
                ev5.set(time_add)
            else:
                pass
    
        def SubTime1m(self):
            v1 = eexp
            v1_h, v1_m = v1.split(':') 
            v1_h1 = int(v1_h)
            v1_m1 = int(v1_m) - 1
    
            if v1_m1 < 0:
                v1_m1 = 59
                v2_h = int(v1_h1 - 1)
                v2_m = int(v1_m1)
            else:
                v2_h = v1_h1
                v2_m = v1_m1

            if enum == 3:
                if v1_h1 == 0:
                    if v1_m1 < 30:
                        v2_m = 30
                        v2_h = 0
                    else:
                        v2_h = v1_h1
                        v2_m = v1_m1
        
            time_add = str((str(dt.timedelta(hours=v2_h, minutes=v2_m)))[:-3])

            if enum == 3:
                ev3.set(time_add)
            elif enum == 5:
                ev5.set(time_add)
            else:
                pass
    
        def SubTime15m(self):
            v1 = eexp
            v1_h, v1_m = v1.split(':') 
            v1_h1 = int(v1_h)
            v1_m1 = int(v1_m) - 15
    
            if v1_m1 < 0:
                v1_m1 = 59
                v2_h = int(v1_h1 - 1)
                v2_m = int(v1_m1)
            else:
                v2_h = v1_h1
                v2_m = v1_m1

            if enum == 3:
                if v1_h1 == 0:
                    if v1_m1 < 30:
                        v2_m = 30
                        v2_h = 0
                    else:
                        v2_h = v1_h1
                        v2_m = v1_m1
        
            time_add = str((str(dt.timedelta(hours=v2_h, minutes=v2_m)))[:-3])

            if enum == 3:
                ev3.set(time_add)
            elif enum == 5:
                ev5.set(time_add)
            else:
                pass
                
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

        def AddTime1cm(self):
            export1(self)
            AddTime1m(self)
    
        def AddTime15cm(self):
            export1(self)
            AddTime15m(self)
    
        def SubTime1cm(self):
            export1(self)
            SubTime1m(self)
    
        def SubTime15cm(self):
            export1(self)
            SubTime15m(self)
            
        def savetime():
            config = configparser.ConfigParser()
            config.read(base_path+"config.ini")
            config.set("preset", "arrival_time", e1.get())
            config.set("preset", "work_time", e2.get())
            config.set("preset", "lunch_break", e3.get())
            with open(base_path+"config.ini", "w") as configfile:
                config.write(configfile)

        def loginattempt():
            username = loginentry.get()
            password = passentry.get()
            phantom_driver = base_path+"phantomjs.exe"
            browser = webdriver.PhantomJS(phantom_driver, service_args=['--ignore-ssl-errors=true'])
            url = "http://czbrq-s-apl0007.cz.abb.com:8080/reports/login.jsp"
            try:
                browser.get(url)
                browser.find_element_by_id("uname").clear()
                browser.find_element_by_id("uname").send_keys(username)
                browser.find_element_by_id("pass").clear()
                browser.find_element_by_id("pass").send_keys(password)
                browser.find_element_by_css_selector('input[type=\"submit\"]').click()
                if browser.current_url == url:
                    messagebox.showerror("Error","Wrong Password")
                    browser.quit()
                    return
                else:
                    pass
                browser.switch_to.frame(browser.find_element_by_name("toolbar"))
                browser.find_element_by_css_selector("select#repId > option[value='1']").click()
                browser.switch_to.default_content()
                browser.switch_to.frame(browser.find_element_by_name("report"))
                content = browser.page_source
                browser.switch_to.default_content()
                browser.switch_to.frame(browser.find_element_by_name("toolbar"))
                browser.find_element_by_css_selector("select#repId > option[value='19']").click()
                browser.switch_to.default_content()
                browser.switch_to.frame(browser.find_element_by_name("report"))
                content_2 = browser.page_source
                browser.quit()
            except NoSuchElementException:
                messagebox.showerror("Error","WATT not accessible")
            soup=BeautifulSoup(content, "lxml")
            soup_2=BeautifulSoup(content_2, "lxml")
            #get correct class
            now = dt.date.today()
            day = int(now.strftime("%d"))
            day_string = str(day)+"."
            #get times from table
            variables = {}

            try:
                for row in range (0,100):
                    for td in soup.find("td", text=day_string).parent.findAll('td')[row]:
                        x = str(td)
                        x1 = x.strip()
                        variables [row] = x1
            except IndexError:
                pass

            #Lunch check
            lunch_var = "0:30:00"
            try:        
                for y in range (0,100):
                    if variables[y] == "Od Ob":
                        ob1 = dt.datetime.strptime(variables[int(y+1)],"%H:%M")
                        ob2 = dt.datetime.strptime(variables[int(y-2)],"%H:%M")
                        lunch_var = ob1 - ob2
                        lunch_load = 1
                    elif variables[y] == "Př Ob":
                        ob1 = dt.datetime.strptime(variables[int(y-2)],"%H:%M")
                        ob2 = dt.datetime.strptime(variables[int(y-5)],"%H:%M")
                        lunch_var = ob1 - ob2
                        lunch_load = 1
            except KeyError:
                pass
                    
            l_h, l_m, l_s  = str(lunch_var).split(':') 
            lunch_set = str(l_h+":"+l_m)
            ev3.set(lunch_set)
                    
            #Arrival set and check for medical
            if variables[4] == "Př Lé":
                ev1.set("8:00")
            else:
                ev1.set(variables[2])

            #Work-breaks check
            variables_leave = {}
            variables_enter = {}
            x = 0
            try:
                for z in range (0,100):
                    if variables[z] == "Od":
                        if variables[z+3] == "Př":
                            z1 = variables[z-2]
                            z2 = variables[z+1]
                            variables_leave[x]=z1
                            variables_enter[x]=z2
                            x=x+1
                        else:
                            pass
                    else:
                        pass
            except KeyError:
                pass
            #Time spent off-work
            t_out_h = 0
            t_out_m = 0

            try:
                for t in range (0,100):
                    t_out = str(dt.datetime.strptime(variables_enter[t],"%H:%M")-dt.datetime.strptime(variables_leave[t],"%H:%M"))
                    t_temp_h, t_temp_m, t_temp_s = t_out.split()
                    t_out_h = t_out_h + int(t_temp_h)
                    t_out_m = t_out_m + int(t_temp_m)
            except KeyError:
                pass
            
            time_out_h = str(t_out_h)
            time_out_m = str(t_out_m)
            t_out_fin = dt.datetime.strptime(time_out_h,"%H") + dt.timedelta(minutes=int(time_out_m))
            t_out_time = str(t_out_fin.time())[:-3]
            ev5.set(t_out_time)

            variables_today = {}
            
            try:
                for row in range (0,100):
                    for td in soup_2.find("td", text=day_string).parent.findAll('td')[row]:
                        x = str(td)
                        x1 = x.strip()
                        variables_today [row] = x1
            except IndexError:
                pass

            try:
                work_today = variables_today [10]
            except KeyError:
                work_today = "0:00"

            w1h, w1m = work_today.split(':')
        
            variables_sums = {}

            try:
                for row in range (0,100):
                    for td in soup_2.find("tr", {"class":"sums"}).findAll('td')[row]:
                        x = str(td)
                        x1 = x.strip()
                        variables_sums [row] = x1
            except IndexError:
                pass
            try:
                w2h, w2m = variables_sums[3].split(':')
            except KeyError:
                w2h = "0"
                w2m = "00"
            try:
                w3h, w3m = variables_sums[11].split(':')
            except KeyError:
                w3h = "0"
                w3m = "00"
            try:
                w4h, w4m = variables_sums[17].split(':')
            except KeyError:
                w4h = "0"
                w4m = "00"
            days_watt = variables_sums[2][:-3]
            hours_normal = 8 * (int(days_watt) - 1)
            #Datetime will not accept times over 24h....now add rest....
            hours_watt = int(w2h)-int(w1h)+int(w3h)+int(w4h)
            minutes_watt = int(w2m)-int(w1m)+int(w3m)+int(w4m)
            hours_dis = hours_watt - hours_normal

            try:
                if hours_dis == minutes_watt == 0:
                    time_temp = "0:00"
                elif minutes_watt < 0:
                    hours_f = hours_dis - 1
                    minutes_f = 60 - minutes_watt
                    if minutes_f == 0:
                        minutes_f = "00"
                    else:
                        pass
                    time_prep = str(hours_f)+":"+str(minutes_f)+":00"
                    if hours_dis < 0 :
                        time_temp = "minus "+str(time_prep)
                    else:
                        time_temp = "plus "+str(time_prep)
                elif minutes_watt >= 0 and hours_dis >= 0 :
                    hours_f = hours_dis
                    minutes_f = minutes_watt
                    if minutes_f == 0:
                        minutes_f = "00"
                    else:
                        pass
                    time_prep = str(hours_f)+":"+str(minutes_f)+":00"
                    time_temp = "plus "+str(time_prep)
                elif minutes_watt > 0 and hours_dis < 0 :
                    hours_f = hours_dis + 1
                    minutes_f = 60 - minutes_watt
                    if minutes_f == 0:
                        minutes_f = "00"
                    else:
                        pass
                    time_prep = str(hours_f)+":"+str(minutes_f)+":00"
                    time_temp = "minus "+str(time_prep)
                elif minutes_watt >= 0 and hours_dis < 0 :
                    hours_f = abs(hours_dis)
                    minutes_f = minutes_watt
                    if minutes_f == 0:
                        minutes_f = "00"
                    else:
                        pass
                    time_prep = str(hours_f)+":"+str(minutes_f)+":00"
                    time_temp = "minus "+str(time_prep)
                else:
                    pass
            except KeyError:
                pass

            time_string.set(time_temp)
            
            config = configparser.ConfigParser()
            config.read(base_path+"config.ini")
            if rem_var.get() == 1:
                config.set("login", "username", loginentry.get())
            else:
                config.set("login", "username", "")
            with open(base_path+"config.ini", "w") as configfile:
                config.write(configfile)
  
            login_OK.set(1)
            
        def loginaction():
            l1.grid(row=0, column=0)
            e1.grid(row=0, column=1, pady=4)
            l2.grid(row=0, column=2)
            e2.grid(row=0, column=3, pady=4)
            l3.grid(row=1, column=2)
            if lunch_load == 1:
                e4.grid(row=1, column=3)
            else:
                e3.grid(row=1, column=3)
            l4.grid(row=1, column=4, padx=2)
            l5.grid(row=1, column=0)
            e5.grid(row=1, column=1, pady=4)
            button3.grid(row=0, column=7)
            button4.grid(row=1, column=7)
            button5.grid(row=2, column=7)
            button6.grid(row=3, column=7)
            button_monthly.grid(row=0, column=4)
            timeathome.grid(row=2, columnspan=7, sticky="nsew")
            timeleft.grid(row=3, columnspan=7, sticky="nsew")
            loginlabel.grid_forget()
            loginentry.grid_forget()
            passlabel.grid_forget()
            passentry.grid_forget()
            loginbutton.grid_forget()
            remember.grid_forget()
            back_button.grid_forget()
            
        def loginaction_final():
            loginattempt()
            login_OK_temp = login_OK.get()
            if login_OK_temp == 1:
                loginaction()
            else:
                pass

        def monthly_overview():
            balance = "Your time balance is "+time_string.get()
            messagebox.showinfo("Month overview", balance)


        l1 = tk.Label(self, text="Arrived at: ")
        
        e1 = tk.Entry(self)
        e1["width"] = 5
        e1.config(bg="white", state="readonly", textvariable = ev1)

        image3 = ImageTk.PhotoImage(file = base_path+"undo_r.png")
        button3 = tk.Button(self, image=image3, fg="red", command=lambda: controller.show_frame(MainWindow))
        button3.image = image3
        
        image4 = ImageTk.PhotoImage(file = base_path+"setup_r.png")
        button4 = tk.Button(self, image=image4, fg="red", command=lambda: controller.show_frame(SetupWindow))
        button4.image = image4
        
        image5 = ImageTk.PhotoImage(file = base_path+"login_r.png")
        button5 = tk.Button(self, image=image5, fg="red", command=loginaction_final)
        button5.image = image5
        
        image6 = ImageTk.PhotoImage(file = base_path+"about_r.png")
        button6 = tk.Button(self, image=image6, fg="red", command=popupabout)
        button6.image = image6

        image_monthly = ImageTk.PhotoImage(file = base_path+"monthly_r.png")
        button_monthly = tk.Button(self, image=image_monthly, command=monthly_overview)
        button_monthly.image = image_monthly
        
        l2 = tk.Label(self)
        l2["text"] = ",will work for:"
    
        e2 = tk.Entry(self)
        e2["width"] = 5
        e2.bind("<Enter>", Set_Enum_2 )
        e2.bind("<Button-1>", AddTime15c )
        e2.bind("<Button-3>", SubTime15c )
        e2.config(bg="white", state="readonly", textvariable = ev2)

        l3 = tk.Label(self)
        l3["text"] = "And lunch? :"

        e3 = tk.Entry(self)
        e3["width"] = 5
        e3.bind("<Button-1>", AddTime1cm )
        e3.bind("<Shift-1>", AddTime15cm )
        e3.bind("<Button-3>", SubTime1cm )
        e3.bind("<Shift-3>", SubTime15cm )
        e3.config(bg="white", state="readonly", textvariable = ev3)
        
        e4 = tk.Entry(self)
        e4["width"] = 4
        e4.config(bg="white", state="readonly", textvariable = ev3)
    
        l4= tk.Label(self)
        l4["text"] = "minutes"

        l5 = tk.Label(self)
        l5["text"] = "Left work for:"

        e5 = tk.Entry(self)
        e5["width"] = 5
        e5.config(bg="white", state="readonly", textvariable = ev5)
        
        timeathome = tk.Label(self)
        timeathome.configure(text="Sample", bg="green", font=("Font",20))
        
        timeleft = tk.Label(self)
        timeleft.configure(text="Sample", bg="yellow", font=("Font",20))
        
        loginlabel = tk.Label(self, text="Osobní číslo")
        loginlabel.grid(row=0, column=1)
        
        loginentry = tk.Entry(self)
        loginentry["width"] = 10
        loginentry.grid(row=0, column=2, pady=4)
        loginentry.focus_set()
        
        remember = tk.Checkbutton(self, text="Remember me", variable=rem_var)
        remember.grid(row=0, column=3)
        
        passlabel = tk.Label(self, text="Heslo")
        passlabel.grid(row=1, column=1)
        
        passentry = tk.Entry(self, show="*" )
        passentry["width"] = 15
        passentry.grid(row=1, column=2)
        passentry.bind("<Return>", lambda event: loginaction_final())
        
        loginbutton = tk.Button(self, text = "Login", command=loginaction_final)
        loginbutton.grid(row=2, column=0, columnspan=2)
        loginbutton.bind("<Return>", lambda event: loginaction_final())
        
        back_button = tk.Button(self, text = "Back", command=lambda: controller.show_frame(MainWindow))
        back_button.grid(row=2, column=2, columnspan=2)
        back_button.bind("<Return>", lambda event: controller.show_frame(MainWindow))
        
        config = configparser.ConfigParser()
        config.read(base_path+"config.ini")
        ev2_time = (config["preset"]["work_time"])
        ev2.set(ev2_time)
        color1_temp = str((config["visual"]["color1"]))
        color2_temp = str((config["visual"]["color2"]))
        timeathome.configure(bg=color1_temp)
        timeleft.configure(bg=color2_temp)
        savedpath_temp = (config["login"]["url"])
        savedpath.set(savedpath_temp)
        rem_temp = (config ["login"]["remember"])
        rem_var.set(rem_temp)
        if rem_var.get() == 1:
            login_temp = (config ["login"]["username"])
            loginentry.insert(0, login_temp)
        else:
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
                    if int(t_in_h) < 6:
                        t_in_h = "06"
                        t_in_m = "00"
                    else:
                        pass
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
                    break
                except (ValueError):
                    t_work_h = "08"
                    t_work_m = "00"
                break
    
# lunch break
            while True:
                try:
                    if lunch_load == 1:
                        t_lunch = e4.get()
                    else:
                        t_lunch = e3.get()
                    t_lunch_h, t_lunch_m = t_lunch.split(':')

                    if int(t_lunch_h) == 0:
                        if int(t_lunch_m) < 30:
                            t_lunch_m = str(30)
                        else:
                            pass
                    else:
                        pass
                    break
                except (ValueError):
                    t_lunch_m = "30"
                    t_lunch_h = "0"
                break

# non-paid pause
            t_out_time_h, t_out_time_m, t_out_time_s = t_out_time.split(":")

#variables preparation
            t_now = h1 + ":" + m1 + ":" + s1
            t_ar= t_in_h + ":" + t_in_m + ":00"
            t_m = dt.timedelta(minutes=int(t_work_m)) + dt.timedelta(minutes=int(t_lunch_m))
            t_m1 = t_m + dt.timedelta(minutes=int(t_out_time_m))
            t_w_h, t_w_m, t_w_s = str(t_m1).split(':')
            time_working = str(int(t_work_h) + int(t_w_h) + int(t_lunch_h) + int(t_out_time_h)) + ":" + str(t_w_m) + ":00"
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
