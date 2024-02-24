import pyautogui
import os
import time

time.sleep(1)
folder_path = 'C:\\Users\\dal362\\Desktop\\TEMP_SS'
os.makedirs(folder_path, exist_ok=True)

ss_filename = 'Mission 2 Screenshot.png'

screenshot = pyautogui.screenshot()

screenshot.save( os.path.join(folder_path, ss_filename) )
time.sleep(1)