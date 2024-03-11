import subprocess
import time
import sys
import pyautogui as pag
from threading import Thread

passed_variable = sys.argv[1]
URL = 'https://drexel.qualtrics.com/jfe/form/SV_bClOWafnNkwIPrw'

def survey():
    subprocess.Popen(["C:\\ARTEMIS\\surveybrowser.exe", URL], creationflags=subprocess.CREATE_NEW_CONSOLE)

time.sleep(1)
Thread(target=survey).start()
time.sleep(40)

#CHANGE COORDINATES
pag.moveTo(750,440) #Gototextfield
pag.mouseUp()
pag.mouseDown()
pag.mouseUp()
time.sleep(1)
pag.write(passed_variable)
time.sleep(2)
pag.moveTo(1295,574) #Pressnext
pag.mouseUp()
pag.mouseDown()
pag.mouseUp()