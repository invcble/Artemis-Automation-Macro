import subprocess
import time
import sys
import pyautogui as pag

passed_variable = sys.argv[1]

time.sleep(1)
subprocess.Popen(['start', 'https://drexel.qualtrics.com/jfe/form/SV_2gbBTwyemTFj46W'], shell = True)
time.sleep(3)

#CHANGE COORDINATES
pag.moveTo(638,338) #Gototextfield
pag.mouseUp()
pag.mouseDown()
pag.mouseUp()
time.sleep(1)
pag.write(passed_variable)