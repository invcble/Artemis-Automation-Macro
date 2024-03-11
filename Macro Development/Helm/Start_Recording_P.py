import pyautogui as pag
import os
import time

# time.sleep(1)
# pag.moveTo(1438,236) #Stoptraining
# pag.mouseDown()
# pag.mouseUp()


time.sleep(1)
os.system("taskkill /im KalturaCapture.exe /f") #Killkaltura
time.sleep(3)
pag.write(['win'])
time.sleep(1)
pag.write("Kaltura Capture")
time.sleep(1)
pag.write(['enter'])
time.sleep(20)

pag.moveTo(638,338) #Startrecord
pag.mouseDown()
pag.mouseUp()
# time.sleep(8)
# pag.moveTo(1883,994) #Minimizerecord
# pag.mouseUp()
# time.sleep(1)
# pag.mouseUp()
# pag.mouseDown()
# pag.mouseUp()
# time.sleep(1)