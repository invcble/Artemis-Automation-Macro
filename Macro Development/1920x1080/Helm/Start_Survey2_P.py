import subprocess
import time
import sys
import pyautogui as pag
from tkinter import messagebox
from threading import Thread

Survey_link = []

try:
    with open("C:\\ARTEMIS\\SURVEY_LINK.txt") as file:
        for line in file:
            Survey_link.append( line.strip().split(": ")[1] )
except:
    messagebox.showerror(title="Error", message="Could not find SURVEY_LINK.txt")
    sys.exit()

passed_variable = sys.argv[1]
URL = f"{Survey_link[1]}"

def survey():
    subprocess.Popen(["C:\\ARTEMIS\\surveybrowser.exe", URL], creationflags=subprocess.CREATE_NEW_CONSOLE)

time.sleep(1)
Thread(target=survey).start()
time.sleep(25)

#CHANGE COORDINATES
pag.moveTo(607,447) #Gototextfield
pag.mouseUp()
pag.mouseDown()
pag.mouseUp()
time.sleep(1)
pag.write(passed_variable)
time.sleep(2)
pag.moveTo(1295,594) #Pressnext
pag.mouseUp()
pag.mouseDown()
pag.mouseUp()