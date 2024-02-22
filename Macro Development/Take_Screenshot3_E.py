import pyautogui
import os
import time

time.sleep(1)
folder_path = 'path/to/your/folder'
os.makedirs(folder_path, exist_ok=True)

ss_filename = 'Mission 3 Screenshot.png'

screenshot = pyautogui.screenshot()

screenshot.save( os.path.join(folder_path, ss_filename) )
time.sleep(1)