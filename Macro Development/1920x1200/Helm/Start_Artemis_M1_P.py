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
pag.moveTo(1741,1029) #Startclient
pag.mouseDown()
pag.mouseUp()
time.sleep(2)
pag.moveTo(1741,1029) #Connectserver
pag.mouseDown()
pag.mouseUp()
time.sleep(5)
pag.moveTo(787,479) #Ship1
pag.mouseDown()
pag.mouseUp()
time.sleep(1)
pag.moveTo(1050,515) #Helm
pag.mouseDown()
pag.mouseUp()
time.sleep(1)
pag.moveTo(1722,1065) #Ready
pag.mouseDown()
pag.mouseUp()
time.sleep(3)
#READY FOR MANUAL START