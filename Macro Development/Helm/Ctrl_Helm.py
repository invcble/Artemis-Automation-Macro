from xmlrpc.server import SimpleXMLRPCServer
import socket
import subprocess
import tkinter as tk
from tkinter import messagebox
from threading import Thread

coordinates = "200x100+550+400"

IP = socket.gethostbyname(socket.gethostname()) #auto grabbing IP
# party = SimpleXMLRPCServer((IP, 4001), allow_none=True)
party = SimpleXMLRPCServer(('localhost', 4000), allow_none=True)

def check():
    pass

def start_training():
    subprocess.run(['python', 'Start_Training_P.py'])

def start_recording():
    subprocess.run(['python', 'Start_Recording_P.py'])

def start_artemis_m1():
    subprocess.run(['python', 'Start_Artemis_M1_P.py'])

def start_survey1(party_teamID):
    subprocess.run(['python', 'Start_Survey1_P.py', party_teamID])

def start_m2():
    subprocess.run(['python', 'Start_M2_P.py'])

def start_survey2(party_teamID):
    subprocess.run(['python', 'Start_Survey2_P.py', party_teamID])

def start_m3():
    subprocess.run(['python', 'Start_M3_P.py'])

def start_survey3(party_teamID):
    subprocess.run(['python', 'Start_Survey3_P.py', party_teamID])

def stop_recording():
    subprocess.run(['python', 'Stop_Recording_P.py'])

def move_video(party_teamID):
    subprocess.run(['python', 'move_video_P.py', party_teamID])

def stopMacro():
    if( messagebox.askyesno(title="!!! WARNING !!!", message="Are you sure?") ):
        global pwd_panel, pwd_field

        pwd_panel = tk.Toplevel(panel)
        pwd_panel.geometry(coordinates)
        pwd_panel.resizable(False, False)
        pwd_panel.title("Exit")
        tk.Label(pwd_panel, text="Please enter the password").pack(pady=5)

        pwd_field = tk.Entry(pwd_panel, show="*")
        pwd_field.pack(pady=5)

        tk.Button(pwd_panel, text="Submit", command= checkPWD).pack(pady=5)

def checkPWD():
    if pwd_field.get() == "artemis":
        party.shutdown()
        party.server_close()
        panel.destroy()

party.register_function(check)
party.register_function(start_training)
party.register_function(start_recording)
party.register_function(start_artemis_m1)
party.register_function(start_survey1)
party.register_function(start_m2)
party.register_function(start_survey2)
party.register_function(start_m3)
party.register_function(start_survey3)
party.register_function(stop_recording)
party.register_function(move_video)

print("Server Starting...\n")
Thread(target=party.serve_forever).start()
print("Server Started.\n")

panel = tk.Tk()
panel.geometry(coordinates)
panel.resizable(False, False)
panel.title("Helm")
panel.protocol("WM_DELETE_WINDOW", lambda: None)

label = tk.Label(panel, text="Macro is running\n Please do not touch anything")
label.pack(pady=5)

submit_button = tk.Button(panel, text="STOP Macro", command= stopMacro)
submit_button.pack(pady=5)

panel.mainloop()


