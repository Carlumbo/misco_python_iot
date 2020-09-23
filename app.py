import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk() # creates base file window
root.title("Misc Login") #Attachs name to file winoow
apps= []
global root

if os.path.isfile('save.txt'):  
    with open('save.txt', 'r') as f: 
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

 #creates a concatinated file log

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
    # allows for the previous data to be removed before its updated
    filename= filedialog.askopenfilename(initialdir="/", title="Select File",
                                        filetypes=(("CSVs", "*.csv"), ("all files", "*.*")))
    # sets a filter for only csv files, can be changed to other file types 
    apps.append(filename)
    print(filename)
    for app in apps: 
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()
   # creates a loop to display items saved in an array


def runApps():
    for app in apps:
        os.startfile(app)


canvas =  tk.Canvas(root, height=150, width=300, bg="#265172")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

Button = tk.Button(root, text="Login", height="2", width="30").pack()

Button = tk.Button(root, text="Register", height="2", width="30").pack()

"""
openFile = tk.Button(root, text="Open File", padx=10, 
                     pady=5, fg="white", bg="#22bb22", command=addApp)
openFile.pack()

inputBox = tk.Frame(frame, bg="blue")
inputBox.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

inputField = tk.Entry(inputBox, text="Data Point", bg="white" ,fg="black" ,bd="3")
inputField.pack() 

runApps = tk.Button(root, text="Run Apps", padx=10, 
                    pady=5, fg="white", bg="#263d42", command=runApps)
runApps.pack()

reset = tk.Button(root, text="Reset", padx=10,  
    pady=5, fg="white", bg="#bb2222")
reset.pack()
"""

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()


root.mainloop()


with open('save.txt', 'w') as f: 
    for app in apps:
        f.write(app + ',')

##########################################
def register():
    #creates registration window for user name and password
    registration_screen = Toplevel(root)
    registration_screen.title("Register")
    registration_screen.geometry("300x250")

    username = StringVar()
    password = StringVar() 

    Label(registration_screen, text="Please enter credentials below", bg="blue").pack()
    Label(registration_screen, text).pack()

    username_label = tk.Label(register_screen, text="Username *")
    username_label.pack()
    
    # password input field
    username_entry = tk.Entry(registration_screen, textvariable=username)
    username_entry.pack()

    #password labels
    password_label = tk.Label(registration_screen, textvariable)
    password_label.pack()

    #password entry 
    password_entry = tk.Entry(registration_screen, textvariable=password, show= '*')
    password_entry.pack()

    #Post button
    register_button = tk.Button(registration_screen, text="Register", width=10, height=1, bg="blue").pack()

    


