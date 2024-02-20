import pyautogui as pag
import time
import subprocess
import webbrowser
import os
import pygetwindow as gw


####FLOW
#Server: Start Training
#Clients: Opens Training.exe

#Server: Start Recording
#Clients: Closes Training.exe,
########  Starts Kaltura, minimize

#Server: Start Artemis M1
#Clients: Opens Artemis & Loads Mission 1,
##(( SERVER HAS CONTROL TO START ARTEMIS SERVER ))

#Server: Start Survey 1
#Clients: Closes Artemis,
########  Open Survey 1

#Server: Start Artemis M2
#Clients: Closes browser,
########  Opens Artemis & Loads Mission 2,
##(( SERVER HAS CONTROL TO START ARTEMIS SERVER ))

#Server: Start Survey 2
#Clients: Closes Artemis,
########  Open Survey 2

#Server: Start Artemis M3
#Clients: Closes browser,
########  Opens Artemis & Loads Mission 3,
##(( SERVER HAS CONTROL TO START ARTEMIS SERVER ))

#Server: Start Survey 3
#Clients: Closes Artemis,
########  Open Survey 3

#Server: Stop Recording
#Clients: Closes browser,
########  Stops Kaltura


## AT VERY END, Rename POPUP saves ID, writes log file with that ID,
## send that ID to participants, participants create a folder with name, MOVES current video files

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

time.sleep(4)
#KALTURA START
os.system("taskkill /im KalturaCapture.exe /f")
time.sleep(2)
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

# #KALTURA STOP
# pag.moveTo(pag.locateCenterOnScreen("pause.png", confidence=0.8))
# pag.moveRel(-100,0)
# pag.mouseDown()
# time.sleep(1)
# pag.mouseUp()
# time.sleep(1)
# pag.leftClick()
# time.sleep(2)
# pag.click(pag.locateCenterOnScreen("confirm.png", confidence=0.8))
# time.sleep(2)
# pag.click(pag.locateCenterOnScreen("save_button.png", confidence=0.8))
# time.sleep(2)
# pag.click(pag.locateCenterOnScreen("close_kaltura.png", confidence=0.9))
# time.sleep(1)
# pag.click(pag.locateCenterOnScreen("close_kaltura.png", confidence=0.9))


# #PLACEHOLDER CLOSE GUD
# #PLACEHOLDER CLOSE File_org
# time.sleep(5)

# webbrowser.open('https://drexel.qualtrics.com/jfe/form/SV_2gbBTwyemTFj46W')