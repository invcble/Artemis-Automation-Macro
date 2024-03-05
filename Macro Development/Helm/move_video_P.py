import sys
import os
import shutil
import time

os.system("taskkill /im KalturaCapture.exe /f") #Killkaltura
time.sleep(1)
passed_variable = sys.argv[1]

source = "C:\\Kaltura\\"
destination = "C:\\ARTEMIS\\" + passed_variable + "\\Helm Recordings\\"

os.makedirs(destination , exist_ok=True)
files = os.listdir(source)

mp4_files = [file for file in files if file.endswith(".mp4")]
    
for mp4_file in mp4_files:
    shutil.move( source + mp4_file, destination + mp4_file )

time.sleep(5)
files = os.listdir(source) #Update files

del_files = [file for file in files]

try:
    for del_file in del_files:
        os.remove( source + del_file )
except:
    pass