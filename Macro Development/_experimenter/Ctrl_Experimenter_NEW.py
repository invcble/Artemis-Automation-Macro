import tkinter as tk
from tkinter import messagebox
import xmlrpc.client
import time
import subprocess
from threading import Thread
import sys


coordinates = "300x300+400+400"
IP_list = []

try:
    with open("C:\\ARTEMIS\\IP_LIST.txt") as file:
        for line in file:
            IP_list.append( line.strip().split(": ")[1] )
except:
    messagebox.showerror(title="Error", message="Could not find IP_LIST.txt")
    sys.exit()

Helm = xmlrpc.client.ServerProxy('http://'+ IP_list[0] +':4001')
Wpns = xmlrpc.client.ServerProxy('http://'+ IP_list[1] +':4002')
Engr = xmlrpc.client.ServerProxy('http://'+ IP_list[2] +':4003')

print("Console Starting...")



##-------------------BUTTON FUNCTIONS-------------------##

def submission():
    global teamID
    if len(type_field.get())==0 or type_field.get().isspace():
        messagebox.showinfo(title="Error", message="Please enter a Team ID")
    else:
        teamID = str( type_field.get() )
        panel.destroy()
        show_sub_window()

def checkConnection():
    try:
        Helm.check()
        Wpns.check()
        Engr.check()
        messagebox.showinfo(title="Connection OK", message="All are connected")
    except:
        messagebox.showerror(title="Connection Error", message="Please make sure macro controllers are running on all participants. If they are, please update IP_LIST.txt")

def startTraining():
    Thread(target = Helm.start_training).start()
    Thread(target = Wpns.start_training).start()
    Thread(target = Engr.start_training).start()
    time.sleep(5)

def startRecording():
    Thread(target = Helm.start_recording).start()
    Thread(target = Wpns.start_recording).start()
    Thread(target = Engr.start_recording).start()
    time.sleep(5)

def startArtemisM1():
    subprocess.run(['python', 'Start_Artemis_M1_E.py'])
    Thread(target = Helm.start_artemis_m1).start()
    Thread(target = Wpns.start_artemis_m1).start()
    Thread(target = Engr.start_artemis_m1).start()
    time.sleep(5)

def startSurvey1():
    Thread(target = Helm.start_survey1, args = (teamID,)).start()
    Thread(target = Wpns.start_survey1, args = (teamID,)).start()
    Thread(target = Engr.start_survey1, args = (teamID,)).start()
    subprocess.run(['python', 'Take_Screenshot1_E.py', teamID])
    time.sleep(5)

def startM2():
    Thread(target = Helm.start_m2).start()
    Thread(target = Wpns.start_m2).start()
    Thread(target = Engr.start_m2).start()
    subprocess.run(['python', 'Start_M2_E.py'])
    time.sleep(5)

def startSurvey2():
    Thread(target = Helm.start_survey2, args = (teamID,)).start()
    Thread(target = Wpns.start_survey2, args = (teamID,)).start()
    Thread(target = Engr.start_survey2, args = (teamID,)).start()
    subprocess.run(['python', 'Take_Screenshot2_E.py', teamID])
    time.sleep(5)

def startM3():
    Thread(target = Helm.start_m3).start()
    Thread(target = Wpns.start_m3).start()
    Thread(target = Engr.start_m3).start()
    subprocess.run(['python', 'Start_M3_E.py'])
    time.sleep(5)

def startSurvey3():
    Thread(target = Helm.start_survey3, args = (teamID,)).start()
    Thread(target = Wpns.start_survey3, args = (teamID,)).start()
    Thread(target = Engr.start_survey3, args = (teamID,)).start()
    subprocess.run(['python', 'Take_Screenshot3_E.py', teamID])
    time.sleep(5)

def stopRecording():
    Thread(target = Helm.stop_recording).start()
    Thread(target = Wpns.stop_recording).start()
    Thread(target = Engr.stop_recording).start()
    subprocess.run(['python', 'Stop_Artemis_E.py'])
    time.sleep(5)

#not implemented yet
def logVideo():
    Thread(target = Helm.move_video, args = (teamID,)).start()
    Thread(target = Wpns.move_video, args = (teamID,)).start()
    Thread(target = Engr.move_video, args = (teamID,)).start()
    subprocess.run(['python', 'move_log_E.py', teamID])
    time.sleep(5)



##-------------------TKINTER WINDOW-------------------##

def show_sub_window():

    sub_window = tk.Tk()
    sub_window.title("Macro Center")
    sub_window.geometry(coordinates)
    sub_window.attributes('-topmost', True)
    sub_window.resizable(False, False)
    
    team_label = tk.Label(sub_window, text="Team ID: " + teamID)
    team_label.pack(pady=10)

    check_button = tk.Button(sub_window, text="Check Connection", command=checkConnection)
    check_button.pack(pady=3, padx=5)

    buttonframe = tk.Frame(sub_window)
    buttonframe.pack(padx=5, pady=5)

    button = tk.Button(buttonframe, text="1. Start Training", width=15, command=startTraining)
    button.grid(row=0, column=0, padx=5, pady=5)

    button = tk.Button(buttonframe, text="2. Start Recording", width=15, command=startRecording)
    button.grid(row=0, column=1, padx=5, pady=5)

    button = tk.Button(buttonframe, text="3. Start Mission 1", width=15, command=startArtemisM1)
    button.grid(row=1, column=0, padx=5, pady=5)

    button = tk.Button(buttonframe, text="4. SS & Survey 1", width=15, command=startSurvey1)
    button.grid(row=1, column=1, padx=5, pady=5)

    button = tk.Button(buttonframe, text="5. Start Mission 2", width=15, command=startM2)
    button.grid(row=2, column=0, padx=5, pady=5)

    button = tk.Button(buttonframe, text="6. SS & Survey 2", width=15, command=startSurvey2)
    button.grid(row=2, column=1, padx=5, pady=5)

    button = tk.Button(buttonframe, text="7. Start Mission 3", width=15, command=startM3)
    button.grid(row=3, column=0, padx=5, pady=5)

    button = tk.Button(buttonframe, text="8. SS & Survey 3", width=15, command=startSurvey3)
    button.grid(row=3, column=1, padx=5, pady=5)

    button = tk.Button(buttonframe, text="9. Stop Recording", width=15, command=stopRecording)
    button.grid(row=4, column=0, padx=5, pady=5)

    button = tk.Button(buttonframe, text="10. Log & Video", width=15, command=logVideo)
    button.grid(row=4, column=1, padx=5, pady=5)


panel = tk.Tk()
panel.geometry(coordinates)
panel.resizable(False, False)
panel.title("Control Panel")

label = tk.Label(panel, text="Welcome to Artemis Macro Control Panel\n Please enter the Team ID")
label.pack(pady=20)

type_field = tk.Entry(panel)
type_field.pack()

submit_button = tk.Button(panel, text="Submit", command= submission)
submit_button.pack(pady=20)

panel.attributes('-topmost', True)
panel.mainloop()

