from xmlrpc.server import SimpleXMLRPCServer
import socket
import subprocess
import tkinter as tk
from tkinter import messagebox
from threading import Thread

coordinates = "200x100+400+400"

IP = socket.gethostbyname(socket.gethostname()) #auto grabbing IP
# party = SimpleXMLRPCServer((IP, 4001), allow_none=True)
party = SimpleXMLRPCServer(('localhost', 4000), allow_none=True)

def check():
    pass

def start_training(teamID):
    global party_teamID
    party_teamID = teamID

    subprocess.run(['python', 'Start_Training_P.py', party_teamID])

def start_recording():
    subprocess.run(['python', 'Start_Recording_P.py'])

def start_artemis_m1():
    subprocess.run(['python', 'Start_Artemis_M1_P.py'])

def start_survey1():
    subprocess.run(['python', 'Start_Survey1_P.py', party_teamID])

def start_m2():
    subprocess.run(['python', 'Start_M2_P.py'])

def start_survey2():
    subprocess.run(['python', 'Start_Survey2_P.py'])

def start_m3():
    subprocess.run(['python', 'Start_M3_P.py'])

def start_survey3():
    subprocess.run(['python', 'Start_Survey3_P.py'])

def stop_recording():
    subprocess.run(['python', 'Stop_Recording_P.py'])

def idShare(ID):
    print("Printing ID on server: "+ ID)

def stopMacro():
    if( messagebox.askyesno(title="WARNING!!!", message="Are you sure?") ):
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
party.register_function(idShare)

print("Server Starting...\n")
Thread(target=party.serve_forever).start()
print("Server Started.\n")

panel = tk.Tk()
panel.geometry(coordinates)
panel.resizable(False, False)
panel.title("Helm")

label = tk.Label(panel, text="Macro is running\n Please do not touch anything")
label.pack(pady=5)

submit_button = tk.Button(panel, text="STOP Macro", command= stopMacro)
submit_button.pack(pady=5)

panel.mainloop()


