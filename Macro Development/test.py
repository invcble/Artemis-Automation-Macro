import subprocess
import time


browser_started = False
while not browser_started:
    output = subprocess.run(["tasklist", "/fo", "csv", "/nh"], capture_output=True, text=True)
    
    if "surveybrowser.exe" in output.stdout:
        browser_started = True
    else:
        time.sleep(1)
        print("nhi mila\n")
# output = subprocess.run(["tasklist", "/fo", "csv", "/nh"], capture_output=True, text=True)
# print(output.stdout)