import os
import time
import pyautogui as pag
import pydirectinput as pd

time.sleep(1)
os.system("taskkill /im surveybrowser.exe /f") #Closebrowser
time.sleep(2)
os.system("taskkill /im Artemis.exe /f")
time.sleep(5)

print('\nStopping Kaltura Recording and Uploading...')
kaltura = pag.getWindowsWithTitle("Kaltura Capture")
time.sleep(2)

try:
    kaltura[1].restore()
except:
    print("Issue restoring kaltura\nContinuing...")

time.sleep(2)
while True:
    try:
        kaltura[1].activate()
        break
    except:
        print("retrying")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")

time.sleep(4)
pd.moveTo(1455,1033) #Stoprecord
time.sleep(2)
pd.click()
pd.moveTo(1510,923) #Stopconfirmation
time.sleep(2)
pd.click()
time.sleep(5)
pd.moveTo(1260,1029) #Save&upload
time.sleep(2)
pd.click()
time.sleep(3)
pd.moveTo(1133,755) #Confirmupload
time.sleep(2)
pd.click()
        
# time.sleep(3)
# pd.moveTo(2530,1277)
# time.sleep(0.5)
# pd.click()
# pd.moveTo(2133,188)
# time.sleep(0.5)
# pd.click()