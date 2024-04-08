import time
import ctypes

time.sleep(1)
#replace Training.exe
exe_path = "C:\\ARTEMIS\\Weapons Training.exe"
ctypes.windll.shell32.ShellExecuteW(None, "runas", exe_path, None, None, 5)
time.sleep(1)