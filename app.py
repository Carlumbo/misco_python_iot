import tkinter as tk
from tkinter import *
from datetime import *
import os, re, platform, socket, uuid, json, requests
#os allows access to operating sysyem through the module
#re and platform were used for testing different approaches to grabbing pc info
#socket allows access to the pcs network info (could be down with os module, but this was more straight forward)
#allows for unique strings of data, was going to use for giving each data block it's own unique id , but this was already done natively on the DB side
#json allows for me to manipulate data for api calls
#requests gives me access to CRUD functionality with api requests


#creating a varible for the tk window
root = tk.Tk()
#Adding title  to the login window
root.title('Misco Login')
#creating the dimensions of  the root window
root.geometry("400x350")
# sets color of root window
root.configure(bg="grey")


#Sign_in window
#Send data to mongoDB database
def send_Data():
    print("Hello")
    dataType2 = dataType.get()
    dataPoint2 = dataPoint.get()
    x = {
        "type": dataType2,
        "Uploader": currentUser,
        #Mac Id  to tell device orgin
        "PCorigin": macUUID,
        #data point, can be any number
        "dataPoint": dataPoint2,
        #sending the timestamp of when the JSON object was created
        "createdAt": datetime.now().strftime('%m-%d-%Y %H:%M:%S')
    }
    #print the json object to the console for verification
    print(x)
    #posting the json object to the databhase
    requests.post('https://misc-express-mongo.herokuapp.com/index/new', x)

def add_data():
    #defining global varibles ot be shared with other methods
    global currentUser
    global passEnter
    global dataType
    global dataPoint
    #creatiing two different data types
    #One is a string for easy data identification
    dataType =  StringVar()
    #the use of a doublevar  you can have floating numbers stored
    dataPoint = DoubleVar()
    #saves the login for the variable field
    currentUser = email_verify.get()
    #saves the password entered at the login
    passEnter = password_verify.get()

    #allows for the pop up of a new data_window
    data_window = Toplevel()
    #names the window
    data_window.title('Data Entry')
    #sets dimensions for the data window
    data_window.geometry('500x350')
    #gives background color of window
    data_window.configure(bg="grey")
    #creates login request to be compared to current database info
    loginReq =  {
        "email": currentUser,
        "password": passEnter
    }
    requests.post("https://misc-express-mongo.herokuapp.com/user/login", loginReq)
    #destorys login in window once the req is fulfilled
    login_window.destroy()
    #editable greeting menu, would be updatable from the website profile page, set intillay to just displaying your email address
    greetingLabel = tk.Label(data_window, text=greeting, relief=GROOVE)
    greetingLabel.place(relx=0.6,  rely=0.1, anchor=S )
    #asks for type (such as humidity, pressure, tempature)
    label1 = tk.Label(data_window, text="Type", relief=GROOVE)
    label1.place(relx=0.2,  rely=0.3, anchor=S )

    dataType =  tk.Entry(data_window, textvariable=dataType, relief=GROOVE)
    dataType.place(relx=0.6, rely=0.3, anchor=CENTER , width=300)
    #asks for the actual floating data point to be sent for the DB
    label2 = tk.Label(data_window, text="Datapoint", relief=GROOVE)
    label2.place(relx=0.2, rely=0.5, anchor=S)

    dataEntry =  tk.Entry(data_window, textvariable=dataPoint, relief=GROOVE)
    dataEntry.place(relx=0.6, rely=0.5, anchor=CENTER , width=300)

    label3 = tk.Label(data_window, text="User", relief=GROOVE)
    label3.place(relx=0.2, rely=0.7, anchor=S)

    #label4 = tk.Label(data_window, text=currentUser, relief=GROOVE)
    #label4.place(relx=0.4, rely=0.7, anchor=S)

    #displays pc origin as macUUID
    pcOrigin1 = tk.Label(data_window, text="Pc Origin", relief=GROOVE)
    pcOrigin1.place(relx=0.2, rely=0.7, anchor=S)

    pcOrigin = tk.Label(data_window, text=macUUID, relief=GROOVE)
    pcOrigin.place(relx=0.4, rely=0.7, anchor=S)


    sendButton = tk.Button(data_window, text="Send", width=20, command=send_Data, bg="blue", activebackground="red", fg="White", relief=GROOVE)
    sendButton.place(relx=0.6, rely=1, anchor=SE)

   # exitButton = tk.Button(data_window, text="EXIT", width=20, command=data_window.destroy(), bg="red", activebackground="red", fg="White", relief=GROOVE)
    #exitButton.place(relx=0.3, rely=1, anchor=SE)

def login_verify():
    #logic used by sign_in to check data
    #defines global varible for greeting
    global greeting
    #grabs user info at login
    currentUser = email_verify.get()
    passEnter = password_verify.get()
    #compares user info to database infor
    list_of_users =  requests.get('https://misc-express-mongo.herokuapp.com/user/all')
    x = list_of_users.json()
    count =  len(x)
    y = 0
    #goes through a series of cases to compare info to whats in the DB
    while y < count:
        #if user email and password are correct opens window for data entry
        if currentUser ==  x[y]['email'] and passEnter == x[y]['password']:
            greeting = x[y]['email']
            # print(greeting)
            # print("Login Succesful")
            add_data()
            break
        elif currentUser ==  x[y]['email'] and passEnter != x[y]['password'] :
            print("Password Incorrect")
            break
        elif y == count - 1 and currentUser !=  x[y]['email'] :
            print("User not found ")
            y+=1
        else  :
            y+=1
    #print("hello")

def sign_in():
    #actual sign in window layout
    global login_window
    # root.destroy()
    login_window =  Toplevel()
    login_window.title('Login')
    login_window.geometry('500x350')
    login_window.configure(bg="grey")

    #varibles to store input inforamtion
    global email_verify
    global password_verify
    email_verify = StringVar()
    password_verify = StringVar()
    #greeting = StringVar()

    emailLabel  = tk.Label(login_window, text="email", relief=GROOVE)
    emailLabel .place(relx=0.2,  rely=0.3, anchor=S )

    passLabel = tk.Label(login_window, text="Password", relief=GROOVE)
    passLabel.place(relx=0.2, rely=0.5, anchor=S)

    emailE = tk.Entry(login_window, textvariable=email_verify, relief=GROOVE)
    emailE.place(relx=0.6, rely=0.3, anchor=CENTER , width=300)

    passwordE = Entry(login_window, show="*", textvariable=password_verify, relief=GROOVE)
    passwordE.place(relx=0.6, rely=0.5, anchor=S , width=300)

    # signInButton = tk.Button(login_window, text="Sign In", width=20, height=2, command=add_data, activebackground="grey", activeforeground="red")
    # signInButton.place(relx= 0.8, rely=0.8, anchor=SE)

    #sign in button that calls the login_verify funciton
    signInButton = tk.Button(login_window, text="Sign In", width=20, height=2, command=login_verify, activebackground="grey", activeforeground="red")
    signInButton.place(relx= 0.8, rely=0.8, anchor=SE)


    exitButton = tk.Button(login_window, text="EXIT", width=20, command=login_window.destroy, bg="red", activebackground="red", fg="White", relief=GROOVE)
    exitButton.place(relx=0.3, rely=1, anchor=SE)

#previiously used for dispalying database information, this was for testing at the time and additonal functionality (registering a user through the app)
def download_api():
    x = requests.get('https://misc-express-mongo.herokuapp.com/user/all')
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

#grabbing PC name and storing it into a global variable
global platId
pcLabel =tk.Label(root, text="Current System Name:",relief=GROOVE)
pcLabel.place(relx=0.3,rely=0.3, anchor=CENTER)
platId = platform.uname().system + "-" + platform.uname().node

pcInfo = tk.Label(root, text=platId)
pcInfo.place(relx= 0.7, rely=0.3, anchor=CENTER)


#get mac address anbd store into global varible
macLabel =tk.Label(root, text="Unique Mac Address:",relief=GROOVE)
macLabel.place(relx=0.3,rely=0.4, anchor=CENTER)

global macUUID
# changing mac into standard format
macUUID =  (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
for ele in range(0,8*6,8)][::-1]))

macInfo = tk.Label(root, text=macUUID)
macInfo.place(relx= 0.7, rely=0.4, anchor=CENTER)


#grabbing IP address of origin pc
ipLabel =tk.Label(root, text="ip Address:",relief=GROOVE)
ipLabel.place(relx=0.3, rely=0.5, anchor=CENTER)
#grabbing the actual ip through the socket module
hostName =  socket.gethostname()
ipAddress = socket.gethostbyname(hostName)

ipInfo = tk.Label(root, text=ipAddress)
ipInfo.place(relx= 0.7, rely=0.5, anchor=CENTER)

#Login buttons
loginButton =tk.Button (root, text="Login", width=20, height=3, command=sign_in,
                  activebackground="grey", activeforeground="red"
, relief=GROOVE)
loginButton.place(relx=0.5, rely=0.75, anchor=CENTER)

# signUpButton = tk.Button(root, text="Sign Up", width=20,height=3, command=sign_up,
#                          activebackgroun="grey", activeforeground="red"
# , relief=GROOVE)
# signUpButton.place(relx=0.7, rely=0.75, anchor=CENTER)

#add button for api tests
# requestButton = tk.Button(root, text="Request API", width=20, command=download_api )
# requestButton.place(relx=0.7, rely=1 , anchor=S)


exitButton = tk.Button(root, text='EXIT', width=20, command=root.destroy,
                        bg="red", activebackground="red", relief=GROOVE)
exitButton.place(relx=0.3, rely=1, anchor=SE)
root.mainloop()