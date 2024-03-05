import os
import time
import pygetwindow as gw
import pyautogui as pag

time.sleep(1)
os.system("taskkill /im surveybrowser.exe /f") #Closebrowser
time.sleep(2)
os.system("taskkill /im Artemis.exe /f")
time.sleep(2)

kaltura = gw.getWindowsWithTitle("Kaltura Capture")[1]
time.sleep(2)

if kaltura:
    if kaltura.isMinimized:
        kaltura.restore()
    kaltura.activate()
time.sleep(3)

pag.moveTo(1455,1033) #Stoprecord
time.sleep(1)
pag.mouseUp()
pag.mouseDown()
pag.mouseUp()
pag.moveTo(1510,923) #Stopconfirmation
time.sleep(1)
pag.mouseUp()
pag.mouseDown()
pag.mouseUp()
time.sleep(5)
pag.moveTo(1260,1029) #Save&upload
pag.mouseUp()
pag.mouseDown()
pag.mouseUp()
time.sleep(1)
pag.moveTo(1133,755) #Confirmupload
pag.mouseUp()
pag.mouseDown()
pag.mouseUp()