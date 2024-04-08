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
pag.moveTo(1749,854) #Startserver
pag.mouseDown()
pag.mouseUp()
time.sleep(3)
pag.moveTo(1536,335) #Modeswitch
pag.mouseDown()
pag.mouseUp()
time.sleep(2)
pag.moveTo(1535,383) #Layoutswitch
pag.mouseDown()
pag.mouseUp()
time.sleep(1)
#WAIT FOR MANUAL START