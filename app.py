import tkinter as tk
from tkinter import *
import os

root = tk.Tk()
root.title('Misco Login')
root.geometry("500x350")
root.configure(bg="light blue")

#create login values
login_user = StringVar()
login_password = StringVar()
#creat user info values
registration_user = StringVar()
registration_password = StringVar()
registration_auth = StringVar()

#Sign_in windo
def sign_in()
    login_window =  Toplevel()
    login_window.title('Login')
    login_window.geometry('500x350')
    login_window.configure(bg="light blue")
global login_user
global login_password

message1 = tk.Label(login_window, text="Username", relief=GROOVE)
message1.place(relx=0.2,  rely=0.5, anchor=S )

message2 = tk.Label(login_window, text="Password", relief=GROOVE)
message2.place(relx=0.2, relyy=0.5, anchor=S)

username = Entry(login_window, textvariable=login_userm relief=GROOVE)
username.place(relx=0.6, rely=0.3, achor=CENTER , width=300)

userPassword = Entry(login_window, show="*" textvariable=login_pass relief=GROOVE)
userPassword.place(relx=0.6, rely=0.3, achor=S , width=300)

signInButton = tk.Button(login_window, text="Sign_In", width=20. height=2, command=check, activebackground="grey", activeforeground="red")

exitButton = tk.Button(login_window, text="EXIT", wdith=20, command=login_window.destroy, bg="red", activebackground="red", fg="White", relief=GROOVE)
exitButton.place(relx=0.3, rely=1, anchor=SE)