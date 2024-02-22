import pyautogui
import os
import time

time.sleep(1)
folder_path = 'path/to/your/folder'
os.makedirs(folder_path, exist_ok=True)
screenshot_filename = 'screenshot.png'

# Full path for the screenshot
full_path = os.path.join(folder_path, screenshot_filename)

# Take a screenshot
screenshot = pyautogui.screenshot()

# Save the screenshot to the specified folder
screenshot.save(full_path)

print(f'Screenshot saved to {full_path}')
