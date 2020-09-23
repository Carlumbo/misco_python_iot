import tkinter as tk
from tkinter import *
import os, re, platform, socket, uuid, json, requests

root = tk.Tk()
root.title('Misco Login')
root.geometry("500x350")
root.configure(bg="blue")

#create login values
login_user = StringVar()
login_password = StringVar()
#creat user info values
reg_user = StringVar()
reg_password = StringVar()
reg_pass_confirm = StringVar()
reg_auth = StringVar()

#Sign_in window
def sign_in():
    login_window =  Toplevel()
    login_window.title('Login')
    login_window.geometry('500x350')
    login_window.configure(bg="blue")

    global login_user
    global login_password

    label1 = tk.Label(login_window, text="Username", relief=GROOVE)
    label1.place(relx=0.2,  rely=0.3, anchor=S )

    label2 = tk.Label(login_window, text="Password", relief=GROOVE)
    label2.place(relx=0.2, rely=0.5, anchor=S)

    username = tk.Entry(login_window, textvariable=login_user, relief=GROOVE)
    username.place(relx=0.6, rely=0.3, anchor=CENTER , width=300)

    userPassword = Entry(login_window, show="*", textvariable=login_password, relief=GROOVE)
    userPassword.place(relx=0.6, rely=0.5, anchor=S , width=300)

    signInButton = tk.Button(login_window, text="Sign_In", width=20, height=2, command=check, activebackground="grey", activeforeground="red")

    exitButton = tk.Button(login_window, text="EXIT", width=20, command=login_window.destroy, bg="red", activebackground="red", fg="White", relief=GROOVE)
    exitButton.place(relx=0.3, rely=1, anchor=SE)

#Sign up with Auth funcitonality

def sign_up():

    reg_win = Toplevel()
    reg_win.title("Create Account")
    reg_win.geometry("550x300")
    reg_win.configure(bg="blue")

    global reg_user
    global reg_password
    global reg_pass_confirm
    global reg_auth

    label1 = tk.Label(reg_win, text="Username", relief=GROOVE)
    label1.place(relx=0.2,rely=0.2, anchor=CENTER)

    label2= tk.Label(reg_win, text="Password", relief=GROOVE)
    label2.place(relx=0.2,rely=0.3, anchor=CENTER)

    label3= tk.Label(reg_win, text="Password Confirmation", relief=GROOVE)
    label3.place(relx=0.2,rely=0.4, anchor=CENTER)

    label4= tk.Label(reg_win, text="Authorization", relief=GROOVE)
    label4.place(relx=0.2,rely=0.5, anchor=CENTER)

    username = Entry(reg_win, relief=GROOVE, textvariable=reg_user)
    username.place(relx=0.6, rely=0.2, anchor=CENTER, width=300)


    password = Entry(reg_win, relief=GROOVE, textvariable=reg_password)
    password.place(relx=0.6, rely=0.3, anchor=CENTER, width=300)


    password_confirmation = Entry(reg_win, relief=GROOVE, textvariable=reg_pass_confirm)
    password_confirmation.place(relx=0.6, rely=0.4, anchor=CENTER, width=300)

    authorization = Entry(reg_win, relief=GROOVE, textvariable=reg_auth)
    authorization.place(relx=0.6, rely=0.5, anchor=CENTER, width=300)

    signUpButton = tk.Button(reg_win, text="Sign up", width=20, height=2
    , command=create_user,
    activebackground="grey", activeforeground="red"
    , relief=GROOVE)

    signUpButton.place(relx=0.5, rely=1, anchor=SW)
    exitButton = tk.Button(reg_win, text='EXIT', width=20
    , command=reg_win.destroy,
    bg='red', activebackground="red", relief=GROOVE )
    exitButton.place(relx=0.3, rely=1, anchor=SE)

#request handlers

def check():
    global login_user
    global login_password
    #setting up variables for get requsts
    logUserGet = login_user.get()
    logPassGet = login_password.get()

def create_user():
    global reg_user
    global reg_pass
    global reg_pass_confirm
    global reg_auth

    username = reg_user.get()
    password = reg_pass.get()
    password_confrimation = reg_pass_confirm.get()
    authoriazation = reg_auth.get()

def download_api():
    x = requests.get('http://localhost:3001/api/v1/products')
    ##y = json.dumps(x)
    print(x.json()[2]['title'])
    ##print(y)

    """if macInfo.get():
        text_response = macInfo.get()
    else:
        text_response = "Text was empty!"

    textWidget = tk.Text()
    textWidget.insert(tk.END, text_response)
    textWidget.grid(row=3, column=0, sticky="WE")
"""
# intial form signin set up

#grabbing PC name
pcLabel =tk.Label(root, text="Current System Name:",relief=GROOVE)
pcLabel.place(relx=0.2,rely=0.3, anchor=CENTER)
platId = platform.uname().system + "-" + platform.uname().node


pcInfo = tk.Label(root, text=platId)
pcInfo.place(relx= 0.5, rely=0.3, anchor=CENTER)


#get mac address
macLabel =tk.Label(root, text="Unique Mac Address:",relief=GROOVE)
macLabel.place(relx=0.2,rely=0.4, anchor=CENTER)

# changing mac into stander format
macUUID =  (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
for ele in range(0,8*6,8)][::-1]))

macInfo = tk.Label(root, text=macUUID)
macInfo.place(relx= 0.5, rely=0.4, anchor=CENTER)


#grabbing IP address of origin pc
ipLabel =tk.Label(root, text="ip Address:",relief=GROOVE)
ipLabel.place(relx=0.2,rely=0.5, anchor=CENTER)

hostName =  socket.gethostname()
ipAddress = socket.gethostbyname(hostName)

ipInfo = tk.Label(root, text=ipAddress)
ipInfo.place(relx= 0.5, rely=0.5, anchor=CENTER)

#Login buttons
loginButton =tk.Button (root, text="Login", width=20, height=3, command=sign_in,
                  activebackground="grey", activeforeground="red"
, relief=GROOVE)
loginButton.place(relx=0.3, rely=0.75, anchor=CENTER)

signUpButton = tk.Button(root, text="Sign Up", width=20,height=3, command=sign_up,
                         activebackgroun="grey", activeforeground="red"
, relief=GROOVE)
signUpButton.place(relx=0.7, rely=0.75, anchor=CENTER)

#add button for api tests
requestButton = tk.Button(root, text="Request API", width=20, command=download_api )
requestButton.place(relx=0.7, rely=1 , anchor=S)


exitButton = tk.Button(root, text='EXIT', width=20, command=root.destroy,
                        bg="red", activebackground="red", relief=GROOVE)
exitButton.place(relx=0.3, rely=1, anchor=SE)

root.mainloop()