import subprocess
import time
import sys
import pyautogui as pag
from threading import Thread

passed_variable = sys.argv[1]
URL = 'https://drexel.qualtrics.com/jfe/form/SV_bClOWafnNkwIPrw'

def survey():
    subprocess.Popen(["surveybrowser.exe", URL], creationflags=subprocess.CREATE_NEW_CONSOLE)

time.sleep(1)
Thread(target=survey).start()
time.sleep(25)

#CHANGE COORDINATES
pag.moveTo(750,400) #Gototextfield
pag.mouseUp()
pag.mouseDown()
pag.mouseUp()
time.sleep(1)
pag.write(passed_variable)
time.sleep(1)
pag.moveTo(1295,534) #Pressnext
pag.mouseUp()
pag.mouseDown()
pag.mouseUp()