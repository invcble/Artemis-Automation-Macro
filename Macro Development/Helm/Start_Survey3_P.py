import subprocess
import time
import sys
import pyautogui as pag
from threading import Thread

passed_variable = sys.argv[1]
URL = 'https://drexel.qualtrics.com/jfe/form/SV_3UAxJrtri8j9au2'

def survey():
    subprocess.Popen(["surveybrowser.exe", URL])

time.sleep(1)
Thread(target=survey).start()
time.sleep(10)

#CHANGE COORDINATES
pag.moveTo(150,390) #Gototextfield
pag.mouseUp()
pag.mouseDown()
pag.mouseUp()
time.sleep(1)
pag.write(passed_variable)