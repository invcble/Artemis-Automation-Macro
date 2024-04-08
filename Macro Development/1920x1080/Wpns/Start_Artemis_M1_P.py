import pyautogui as pag
import time


time.sleep(1)
pag.write(['win'])
time.sleep(1)
pag.write("Play Artemis")
time.sleep(1)
pag.write(['enter'])
time.sleep(3)

pag.moveTo(264,540) #Startgame
pag.mouseDown()
pag.mouseUp()
time.sleep(5)
pag.moveTo(1702,924) #Startclient
pag.mouseDown()
pag.mouseUp()
time.sleep(2)
pag.moveTo(1667,918) #Connectserver
pag.mouseDown()
pag.mouseUp()
time.sleep(5)
pag.moveTo(775,420) #Ship1
pag.mouseDown()
pag.mouseUp()
time.sleep(1)
pag.moveTo(1089,491) #Weapons
pag.mouseDown()
pag.mouseUp()
time.sleep(1)
pag.moveTo(1732,961) #Ready
pag.mouseDown()
pag.mouseUp()
time.sleep(3)
#READY FOR MANUAL START