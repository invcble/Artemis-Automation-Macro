import tkinter as tk
from tkinter import messagebox

coordinates = "300x400+100+100"

def submission():
    global teamID
    if len(type_field.get())==0 or type_field.get().isspace():
        messagebox.showinfo(title="Error", message="Please enter a Team ID")
    else:
        teamID = type_field.get()
        panel.destroy()
        show_sub_window()

def printing():
    print( teamID )

def show_sub_window():
    sub_window = tk.Tk()
    sub_window.title("Macro Center")
    sub_window.geometry(coordinates)
    sub_window.attributes('-topmost', True)
    
    team_label = tk.Label(sub_window, text="Team ID: " + teamID)
    team_label.pack(pady=10)

    close_button = tk.Button(sub_window, text="Start Training", command=sub_window.destroy)
    close_button.pack(pady=5, padx=5)

    close_button = tk.Button(sub_window, text="Start Recording", command=sub_window.destroy)
    close_button.pack(pady=5)

    close_button = tk.Button(sub_window, text="Start Artemis M1", command=sub_window.destroy)
    close_button.pack(pady=5)

    close_button = tk.Button(sub_window, text="Start Survey 1", command=sub_window.destroy)
    close_button.pack(pady=5)

    close_button = tk.Button(sub_window, text="Start M2", command=sub_window.destroy)
    close_button.pack(pady=5)

panel = tk.Tk()
panel.geometry(coordinates)
panel.title("Control Panel")

label = tk.Label(panel, text="Welcome to Artemis Macro Control Panel\n Please enter the Team ID")
label.pack(pady=20)

type_field = tk.Entry(panel)
type_field.pack()

submit_button = tk.Button(panel, text="Submit", command= submission)
submit_button.pack(pady=20)

# print_button = tk.Button(panel, text="print", command= printing)
# print_button.pack(pady=20)

panel.attributes('-topmost', True)
panel.mainloop()

