import urllib.request
import os
import shutil
import zipfile
import sys
import subprocess
import configparser


funame = "GoHome!.exe"
root_dir1 = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
root_dir2 = os.getcwd()
ulocation1 = os.path.exists(root_dir1+"/"+funame)
ulocation2 = os.path.exists(root_dir2+"/"+funame)
base_path = ""
if ulocation1 == True:
    base_path = root_dir1
elif ulocation2 == True:
    base_path = root_dir2
else:
    print("error, GoHome!.exe not present, reinstall program")
    os.system("pause")
    os._exit(-1)
path = "s:/adam.slivka/All/GoHome!/update/update.zip"
version_get = open("s:/adam.slivka/All/GoHome!/update/update.txt","r")
version = version_get.read()
version_get.close()
print("Updating to version "+version+". Please wait, do not close this window!")
print("Downloading update")
os.mkdir(base_path +"/tmp")
shutil.copy2("s:/adam.slivka/All/GoHome!/update/update.zip", base_path +"/tmp")
file = base_path +"/tmp/update.zip"
print("Extracting archive")
zip_ref = zipfile.ZipFile(file,"r")
zip_ref.extractall(base_path +"/tmp")
zip_ref.close()
print("Copy files to dir")
shutil.copyfile(base_path +"/tmp/GoHome!.exe",base_path +"/GoHome!.exe")
print("Throwing out garbage")
shutil.rmtree(base_path +"/tmp")
print("Updating configuration")
config = configparser.ConfigParser()
config.read(base_path+"/data/config.ini")
config.set("system", "version", version)
with open(base_path+"/data/config.ini", "w") as configfile:
    config.write(configfile)
print("All done, please hit any key to continue...")
os.system("pause")
subprocess.Popen(base_path+ "/GoHome!.exe")
os._exit(-1)


