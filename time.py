import time
import sys
import datetime as dt
from datetime import timedelta

now = dt.datetime.now()
h1 = str(now.hour)
m1 = str(now.minute)
s1 = str(now.second)

print("User manual: Enter time in correct format! Program will use standard values otherwise. \n")

# arrival time
while True:
    try:
        t_in =str(input("Please enter time of arrival in format h:mm, thanks: "))
        t_in_h, t_in_m = t_in.split(':') 
        val1 = int(t_in_h)
        val2 = int(t_in_m)
        break
    except (ValueError):
        t_in_h = "06"
        t_in_m = "00"
        print("No or wrong input - using standard time - 6:00")
    break

# work time    
while True:
    try:
        t_work = str(input("Please enter expected work time in format h:mm: "))
        t_work_h, t_work_m = t_work.split(':') 
        val3 = int(t_work_h)
        val4 = int(t_work_m)
    except (ValueError):
        t_work_h = "08"
        t_work_m = "00"
        print("No or wrong input - using standard time - 8:00")
    break
    
# lunch break
while True:
    t_lunch = str(input("Do you have standard lunch break? y(enter)/n: "))
    if t_lunch == "n":
        t_lunch1 = int(input("How long was your lunch break? Minutes:"))
    else:
        print ("Using standard lunch time - 30 minutes")
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
check = int(str(time_lost1.days))

if check < 0:
    print ("What are you doing here? GO HOME!")
else:
    print ("You can leave in:", time_lost1, "that will be at", time_print)
exit()
