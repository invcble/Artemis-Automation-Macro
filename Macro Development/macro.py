import pyautogui as pag
import time
import subprocess
import webbrowser

time.sleep(2)
training = subprocess.Popen("C:\Program Files\Windows Classics\mspaint.exe") #replace training.exe

time.sleep(2)

while True:
    time.sleep(3)
    if training.poll() is None:
        True
    else:
        print("Starting next sequence")
        break

#PLACEHOLDER OPEN GUD
#PLACEHOLDER OPEN File_org
time.sleep(2)

pag.write(['win'])
time.sleep(1)
pag.write("Kaltura Capture")
time.sleep(1)
pag.write(['enter'])
time.sleep(3)

try:
    pag.click(pag.locateCenterOnScreen("new_recording.png", confidence=0.8))
except pag.ImageNotFoundException:
    print("Couldn't find New Recording button, proceeding to record")
time.sleep(2)
pag.click(pag.locateCenterOnScreen("round_recordbutton.png", confidence=0.8))
time.sleep(4)

# pag.write(['win'])
# time.sleep(1)
# pag.write("Play Artemis")
# time.sleep(1)
# pag.write(['enter'])
# time.sleep(3)

time.sleep(5)
# # print(pag.position())
# pag.click(340,197)
# time.sleep(1)
# pag.click(36,238)
# time.sleep(1)
# pag.click(253,552)

# time.sleep(10)
# # pag.moveRel(100,100,5)
# # print(pag.position())

pag.moveTo(pag.locateCenterOnScreen("pause.png", confidence=0.8))
pag.moveRel(-100,0)
pag.mouseDown()
time.sleep(1)
pag.mouseUp()
time.sleep(1)
pag.leftClick()
time.sleep(2)
pag.click(pag.locateCenterOnScreen("confirm.png", confidence=0.8))
time.sleep(2)
pag.click(pag.locateCenterOnScreen("save_button.png", confidence=0.8))
time.sleep(2)
pag.click(pag.locateCenterOnScreen("close_kaltura.png", confidence=0.9))
time.sleep(1)
pag.click(pag.locateCenterOnScreen("close_kaltura.png", confidence=0.9))


#PLACEHOLDER CLOSE GUD
#PLACEHOLDER CLOSE File_org

webbrowser.open('https://drexel.qualtrics.com/jfe/form/SV_2gbBTwyemTFj46W')