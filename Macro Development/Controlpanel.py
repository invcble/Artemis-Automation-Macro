import tkinter as tk
from tkinter import messagebox
import time

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
    time.sleep(10)
    print( teamID )

def show_sub_window():
    sub_window = tk.Tk()
    sub_window.title("Macro Center")
    sub_window.geometry(coordinates)
    sub_window.attributes('-topmost', True)
    sub_window.resizable(False, False)
    
    team_label = tk.Label(sub_window, text="Team ID: " + teamID)
    team_label.pack(pady=10)

    buttonframe = tk.Frame(sub_window)
    buttonframe.pack(padx=5, pady=5)

    button = tk.Button(buttonframe, text="1. Start Training", width=15, command=printing)
    button.grid(row=0, column=0, padx=5, pady=5)

    button = tk.Button(buttonframe, text="2. Start Recording", width=15, command=sub_window.destroy)
    button.grid(row=0, column=1, padx=5, pady=5)

    button = tk.Button(buttonframe, text="3. Start M1", width=15, command=printing)
    button.grid(row=1, column=0, padx=5, pady=5)

    button = tk.Button(buttonframe, text="4. Start Survey 1", width=15, command=sub_window.destroy)
    button.grid(row=1, column=1, padx=5, pady=5)

    button = tk.Button(buttonframe, text="5. Start M2", width=15, command=printing)
    button.grid(row=2, column=0, padx=5, pady=5)

    button = tk.Button(buttonframe, text="6. Start Survey 2", width=15, command=sub_window.destroy)
    button.grid(row=2, column=1, padx=5, pady=5)

    button = tk.Button(buttonframe, text="7. Start M3", width=15, command=printing)
    button.grid(row=3, column=0, padx=5, pady=5)

    button = tk.Button(buttonframe, text="8. Start Survey 3", width=15, command=sub_window.destroy)
    button.grid(row=3, column=1, padx=5, pady=5)

    button = tk.Button(buttonframe, text="9. Stop Recording", width=15, command=printing)
    button.grid(row=4, column=0, padx=5, pady=5)

    button = tk.Button(buttonframe, text="placeholder", width=15, command=sub_window.destroy)
    button.grid(row=4, column=1, padx=5, pady=5)

    close_button = tk.Button(sub_window, text="EXIT", command=sub_window.destroy)
    close_button.pack(pady=5, padx=5)



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

# print_button = tk.Button(panel, text="print", command= printing)
# print_button.pack(pady=20)

panel.attributes('-topmost', True)
panel.mainloop()

