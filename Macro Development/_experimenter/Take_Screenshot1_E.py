import pyautogui
import os
import time
import sys

passed_variable = sys.argv[1]

time.sleep(1)
folder_path = 'C:\\ARTEMIS\\' + passed_variable + '\\Screenshots'
os.makedirs(folder_path, exist_ok=True)

ss_filename = 'Mission 1 Screenshot.png'

screenshot = pyautogui.screenshot()

screenshot.save( os.path.join(folder_path, ss_filename) )
time.sleep(1)