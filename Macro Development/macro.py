import pyautogui as pag
import pygetwindow as gw
import os
import time
import subprocess
import webbrowser


# time.sleep(2)
# training = subprocess.Popen("C:\Program Files\Windows Classics\mspaint.exe") #replace training.exe
# time.sleep(2)

# while True:
#     time.sleep(3)
#     if training.poll() is None:
#         True
#     else:
#         print("Starting next sequence")
#         break
# time.sleep(2)

#PLACEHOLDER OPEN GUD
#PLACEHOLDER OPEN File_org

#KALTURA START
time.sleep(2)
os.system("taskkill /im KalturaCapture.exe /f")
time.sleep(3)
pag.write(['win'])
time.sleep(1)
pag.write("Kaltura Capture")
time.sleep(1)
pag.write(['enter'])
time.sleep(15)

pag.moveTo(638,338) #Startrecord
pag.mouseDown()
pag.mouseUp()
time.sleep(7)
pag.moveTo(1883,994) #Minimizerecord
time.sleep(1)
pag.mouseUp()
pag.mouseDown()
pag.mouseUp()

time.sleep(15) #testrecord

#KALTURA STOP
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


# ############ SERVER ARTEMIS ############
# pag.write(['win'])
# time.sleep(1)
# pag.write("Play Artemis")
# time.sleep(1)
# pag.write(['enter'])
# time.sleep(3)

# pag.moveTo(264,540) #Startgame
# pag.mouseDown()
# pag.mouseUp()
# time.sleep(5)
# pag.moveTo(1728,959) #Startserver
# pag.mouseDown()
# pag.mouseUp()
# time.sleep(3)
# pag.moveTo(1537,342) #Modeswitch
# pag.mouseDown()
# pag.mouseUp()
# time.sleep(2)
# pag.moveTo(1537,394) #Layoutswitch
# pag.mouseDown()
# pag.mouseUp()
# time.sleep(3)
# #WAIT FOR MANUAL START
# #######################################


# ############ CLIENT ARTEMIS - Helm ############
# pag.write(['win'])
# time.sleep(1)
# pag.write("Play Artemis")
# time.sleep(1)
# pag.write(['enter'])
# time.sleep(3)

# pag.moveTo(264,540) #Startgame
# pag.mouseDown()
# pag.mouseUp()
# time.sleep(5)
# pag.moveTo(1741,1029) #Startclient
# pag.mouseDown()
# pag.mouseUp()
# time.sleep(2)
# pag.moveTo(1741,1029) #Connectserver
# pag.mouseDown()
# pag.mouseUp()
# time.sleep(2)
# pag.moveTo(787,479) #Ship1
# pag.mouseDown()
# pag.mouseUp()
# time.sleep(1)
# pag.moveTo(1050,515) #Helm
# pag.mouseDown()
# pag.mouseUp()
# time.sleep(1)
# pag.moveTo(1722,1065) #Ready
# pag.mouseDown()
# pag.mouseUp()
# time.sleep(3)
# #READY FOR MANUAL START
# #######################################

## implement M1 to M2 to M3

############ CLIENT ARTEMIS - Weapons ############
# pag.click(1050,547) #Weapons
#READY FOR MANUAL START
#######################################

############ CLIENT ARTEMIS - Engineer ############
# pag.click(1050,583) #Engineer
#READY FOR MANUAL START
#######################################


# # time.sleep(10)
# # # pag.moveRel(100,100,5)
# # # print(pag.position())


# #PLACEHOLDER CLOSE GUD
# #PLACEHOLDER CLOSE File_org
# time.sleep(5)

# webbrowser.open('https://drexel.qualtrics.com/jfe/form/SV_2gbBTwyemTFj46W')