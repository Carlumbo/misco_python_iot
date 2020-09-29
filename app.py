import tkinter as tk
from tkinter import *
import os, re, platform, socket, uuid, json, requests

root = tk.Tk()
root.title('Misco Login')
root.geometry("500x350")
root.configure(bg="grey")

#create login values
login_user = StringVar()
login_password = StringVar()
#creat user info values
reg_user = StringVar()
reg_password = StringVar()
reg_pass_confirm = StringVar()
reg_auth = StringVar()

#Sign_in window

def send_Data(): 
    dataType2 = dataType.get()
    dataPoint2 = dataPoint.get()
    x = {
        "type": dataType2,
        "dataPoint": dataPoint2, 
        "Uploader": currentUser, 
        "PC orgin": macUUID, 
        "Email": currentUser
    }

    requests.post("http://localhost:3000/index/new", x)

def add_data():
    global currentUser
    global dataType
    global dataPoint

    dataType =  StringVar()
    dataPoint = DoubleVar()
    
    currentUser = email1.get()
    passEnter = passW.get()
    data_window = Toplevel()
    data_window.title('Data Entry')
    data_window.geometry('500x350')
    data_window.configure(bg="grey")

    loginReq =  {
        "email": currentUser,
        "password": passEnter
    }
    requests.post("http://localhost:3000/user/login", loginReq)

    login_window.destroy()
    
    label1 = tk.Label(data_window, text="Type", relief=GROOVE)
    label1.place(relx=0.2,  rely=0.3, anchor=S )

    
    dataType =  tk.Entry(data_window, textvariable=dataType, relief=GROOVE)
    dataType.place(relx=0.6, rely=0.3, anchor=CENTER , width=300)
     
    label2 = tk.Label(data_window, text="Datapoint", relief=GROOVE)
    label2.place(relx=0.2, rely=0.5, anchor=S)

    dataEntry =  tk.Entry(data_window, textvariable=dataPoint, relief=GROOVE)
    dataEntry.place(relx=0.6, rely=0.5, anchor=CENTER , width=300)

    label3 = tk.Label(data_window, text="User", relief=GROOVE)
    label3.place(relx=0.2, rely=0.7, anchor=S)

    #label4 = tk.Label(data_window, text=currentUser, relief=GROOVE)
    #label4.place(relx=0.4, rely=0.7, anchor=S)

    
    pcOrigin1 = tk.Label(data_window, text="Pc Origin", relief=GROOVE)
    pcOrigin1.place(relx=0.2, rely=0.7, anchor=S)

    pcOrigin = tk.Label(data_window, text=macUUID, relief=GROOVE)
    pcOrigin.place(relx=0.4, rely=0.7, anchor=S)


    sendButton = tk.Button(data_window, text="Send", width=20, command=send_Data, bg="blue", activebackground="red", fg="White", relief=GROOVE)
    sendButton.place(relx=0.6, rely=1, anchor=SE)

   # exitButton = tk.Button(data_window, text="EXIT", width=20, command=data_window.destroy(), bg="red", activebackground="red", fg="White", relief=GROOVE)
    #exitButton.place(relx=0.3, rely=1, anchor=SE)
def sign_in():
    global login_window
    login_window =  Toplevel()
    login_window.title('Login')
    login_window.geometry('500x350')
    login_window.configure(bg="grey")

    global email1
    global passW
    email1 = StringVar()
    passW = StringVar()

    EmailL  = tk.Label(login_window, text="email", relief=GROOVE)
    EmailL .place(relx=0.2,  rely=0.3, anchor=S )

    passwordL = tk.Label(login_window, text="Password", relief=GROOVE)
    passwordL.place(relx=0.2, rely=0.5, anchor=S)

    emailE = tk.Entry(login_window, textvariable=email1, relief=GROOVE)
    emailE.place(relx=0.6, rely=0.3, anchor=CENTER , width=300)

    passwordE = Entry(login_window, show="*", textvariable=passW, relief=GROOVE)
    passwordE.place(relx=0.6, rely=0.5, anchor=S , width=300)

    signInButton = tk.Button(login_window, text="Sign In", width=20, height=2, command=add_data, activebackground="grey", activeforeground="red")
    signInButton.place(relx= 0.8, rely=0.8, anchor=SE)



    exitButton = tk.Button(login_window, text="EXIT", width=20, command=login_window.destroy, bg="red", activebackground="red", fg="White", relief=GROOVE)
    exitButton.place(relx=0.3, rely=1, anchor=SE)

#Sign up with Auth funcitonality

def sign_up():

    reg_win = Toplevel()
    reg_win.title("Create Account")
    reg_win.geometry("550x300")
    reg_win.configure(bg="grey")

    global reg_user
    global reg_password
    global reg_pass_confirm
    global reg_auth

    label1 = tk.Label(reg_win, text="email", relief=GROOVE)
    label1.place(relx=0.2,rely=0.2, anchor=CENTER)

    label2= tk.Label(reg_win, text="Password", relief=GROOVE)
    label2.place(relx=0.2,rely=0.3, anchor=CENTER)

    label3= tk.Label(reg_win, text="Password Confirmation", relief=GROOVE)
    label3.place(relx=0.2,rely=0.4, anchor=CENTER)

    email = Entry(reg_win, relief=GROOVE, textvariable=reg_user)
    email.place(relx=0.6, rely=0.2, anchor=CENTER, width=300)
    

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
   # setting up variables for get requsts
    logUserGet = login_user.get()
    logPassGet = login_password.get()

def create_user():
    global reg_user
    global reg_pass
    global reg_pass_confirm
    global reg_auth

    email = reg_user.get()
    password = reg_pass.get()
    password_confrimation = reg_pass_confirm.get()
 
def download_api():
    x = requests.get('http://localhost:3000/user/all')
    ##y = json.dumps(x)
    print(x.json())
    ##print(y)z
     
    """if macInfo.get():
        text_response = macInfo.get()
    else:
        text_response = "Text was empty!"s

    textWidget = tk.Text()
    textWidget.insert(tk.END, text_response)
    textWidget.grid(row=3, column=0, sticky="WE")
"""
# intial form signin set up

#grabbing PC name
global platId
pcLabel =tk.Label(root, text="Current System Name:",relief=GROOVE)
pcLabel.place(relx=0.2,rely=0.3, anchor=CENTER)
platId = platform.uname().system + "-" + platform.uname().node

pcInfo = tk.Label(root, text=platId)
pcInfo.place(relx= 0.5, rely=0.3, anchor=CENTER)


#get mac address
macLabel =tk.Label(root, text="Unique Mac Address:",relief=GROOVE)
macLabel.place(relx=0.2,rely=0.4, anchor=CENTER)

global macUUID
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