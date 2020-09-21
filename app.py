import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps= []

if os.path.isfile('save.txt'): 
    with open('save.txt', 'r') as f: 
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]
      #  apps = tempApps

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename= filedialog.askopenfilename(initialdir="/", title="Select File",
                                        filetypes=(("CSVs", "*.csv"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps: 
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()
    
def runApps():
    for app in apps:
        os.startfile(app)

""" 
def resetApp():
    apps.destroy()
"""
canvas =  tk.Canvas(root, height=700, width=500, bg="#265172")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


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


for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()


root.mainloop()


with open('save.txt', 'w') as f: 
    for app in apps:
        f.write(app + ',')

