# import pyautogui as pag
# import pydirectinput
# pag.FAILSAFE = False
# import time


# # win = pyautogui.getWindowsWithTitle("WhatsApp")
# # if win:
# #     kaltura = win[1] if len(win) > 1 else win[0]
# #     if kaltura.isMinimized:
# #         pyautogui.click(kaltura.left + 10, kaltura.top + 10) 
# #     pyautogui.click(kaltura.left + 10, kaltura.top + 10)

# while True:
#     pag.moveTo(2511,1200)
#     time.sleep(2)
#     Kaltura_windows = pag.getWindowsWithTitle('Kaltura')

#     # kaltura = next((win for win in Kaltura_windows), None)

#     Kaltura_windows[1].restore()
#     while True:
#         try:
#             Kaltura_windows[1].activate()
#             break
#         except:
#             print("retrying")
#             time.sleep(0.3)
#             print(".")
#             time.sleep(0.3)
#             print(".")
#             time.sleep(0.3)
#             print(".")

#     time.sleep(3)
#     # pydirectinput.click(2511,1333)
#     pydirectinput.moveTo(2511,1333)
#     time.sleep(0.5)
#     pydirectinput.click()
#     # pag.moveTo(2511,1333)
#     # time.sleep(2)
#     # # pag.mouseUp()
#     # # pag.mouseDown()
#     # pag.click()
#     # print(Kaltura_windows)


import pyautogui as pag

print(pag.mouseInfo())