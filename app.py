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

#Sign_in window
def sign_in()
    login_window =  Toplevel()
    login_window.title('Login')
    login_window.geometry('500x350')
    login_window.configure(bg="light blue")
global login_user
global login_password

label1 = tk.Label(login_window, text="Username", relief=GROOVE)
label1.place(relx=0.2,  rely=0.5, anchor=S )

label2 = tk.Label(login_window, text="Password", relief=GROOVE)
label2.place(relx=0.2, relyy=0.5, anchor=S)

username = Entry(login_window, textvariable=login_userm relief=GROOVE)
username.place(relx=0.6, rely=0.3, achor=CENTER , width=300)

userPassword = Entry(login_window, show="*" textvariable=login_pass relief=GROOVE)
userPassword.place(relx=0.6, rely=0.3, achor=S , width=300)

signInButton = tk.Button(login_window, text="Sign_In", width=20. height=2, command=check, activebackground="grey", activeforeground="red")

exitButton = tk.Button(login_window, text="EXIT", wdith=20, command=login_window.destroy, bg="red", activebackground="red", fg="White", relief=GROOVE)
exitButton.place(relx=0.3, rely=1, anchor=SE)

#Sign up with Auth funcitonality

def sign_up:

    reg_win = Toplevel()
    reg_win.title("Create Accountt")
    reg_win.geomtry("350x200")
    reg_win.configure(bg="blue")

global reg_user
global reg_password
global reg_pass_confirm
global reg_auth

label1 = tk.Label(reg_win, text="Username", relief=GROOVE)
label1.place(relx=0.2,rely=0.2, anchor=CENTER)

label2= tk.Label(reg_win, text="Password", relief=GROOVE)
label2.place(relx=0.2,rely=0.4, anchor=CENTER)

label3= tk.Label(reg_win, text="Password Confirmation-", relief=GROOVE)
label3.place(relx=0.2,rely=0.6, anchor=CENTER)

label4= tk.Label(reg_win, text="Authorization", relief=GROOVE)
label4.place(relx=0.2,rely=0.6, anchor=CENTER)

username = Entry(reg_win, relief=GROOVE, textvariable=reg_user)
username.place(relx=0.6, rely=0.2, anchor=Center, width=300)


password = Entry(reg_win, relief=GROOVE, textvariable=reg_password)
password.place(relx=0.6, rely=0.4, anchor=Center, width=300)


password_confirmation = Entry(reg_win, relief=GROOVE, textvariable=reg_pass_confirm)
password_confirmation.place(relx=0.6, rely=0.6, anchor=Center, width=300)

authoriazation = Entry(reg_win, relief=GROOVE, textvariable=reg_auth)
authorization.place(relx=0.6, rely=0.6, anchor=Center, width=300)

signUpButton = tk.Button(reg_win, text="Sign up", width=20 height=2
, command=create_user,
                        activebackground="grey", activeforeground="red"
, relief=GROOVE)
    singnUpButton.place(relx=0.5, rely=0.8, anchor=CENTER)
    exitButton = tk.Button(reg_win, text='EXIT' )