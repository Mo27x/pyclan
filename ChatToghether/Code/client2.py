from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from network import Network
from user import User
import time

root = Tk()
root.title("Chat Together")
"Images\ChatToghether.ico"
# root.iconbitmap('./Images/ChatTogether.ico')
root.geometry("800x500")
#open Chat interface
logUser = Toplevel()
logUser.geometry("400x250")
# logged: says if you are already Signed in
logged = False
# isLogin: determine if you are Logging in or Signing in
isLogin = False
user = None
network = None
def sendMessage(user, network):
    message = ""
    while message == "":
        message = input("Insert the message you want to send: ")
    chatId = ""
    while chatId == "" or len(chatId) != 6:
        chatId = input("Insert the id of the chat: ")
    return network.send([user, "add", chatId, message])
def joinChat(user, network):
    chatCode = ""
    while chatCode == "":
        chatCode = input("Insert the chat's code: ")
    chatId = ""
    while chatId == "" or len(chatId) != 6:
        chatId = input("Insert the chat's ID: ")
    return network.send([user, "join", chatId, chatCode])

def createChat(user, network):
    chatName = ""
    chatCode = ""
    while chatName == "":
        chatName = input("Insert the name of the chat you want to create: ")
    while chatCode == "":
        chatCode = input("Insert the code of the chat you want to create: ")
    return network.send([user, "create", -1, chatName, chatCode])

def getChat(user, network):
    chatId = ""
    while chatId == "" or len(chatId) != 6:
        chatId = input("Insert the chat's ID: ")
    return network.send([user, "get", chatId])

def quitChat(user, network):
    chatId = ""
    while chatId == "" or len(chatId) != 6:
        chatId = input("Insert the id of the chat you want to delete: ")
    return network.send([user, "quit", chatId])

def startUser():
    global idEnter
    global user
    global network
    global logged
    global logUse
    global BackGroundFrame
    username = Username.get()
    userId = ""
    if isLogin:
        userId = idEnter.get()
        if username != "" and userId != "" and len(userId) == 6:
            user = User(username, userId, {})
            network = Network()
            logged = True
            BackGroundFrame.pack(fill=BOTH, side=LEFT, expand=True)
    elif username != "" and userId == "":
        user = User(username, "", {})
        network = Network()
        user.id = network.getId()
        print(user.id)
        logged = True
        BackGroundFrame.pack(fill=BOTH, side=LEFT, expand=True)
    logUser.destroy()

def showId():
    global idLabel
    global idEnter
    global isLogin
    isLogin = True
    idLabel.place(x=30,y=140)
    idEnter.place(x = 120, y = 140)

def hideId():
    global idLabel
    global e2
    global isLogin
    isLogin = False
    idLabel.place_forget()
    idEnter.place_forget()

def join():
    UserOptionsMessage1.config(text="Id")
    UserOptionsMessage2.config(text="Code")

def create():
    UserOptionsMessage1.config(text="Name")
    UserOptionsMessage2.config(text="Code")
  
def leave():
    UserOptionsMessage1.config(text="Name")
    UserOptionsMessage2.config(text="Id")

def sent():
    UserOptionsMessage1.config(text="")
    UserOptionsMessage2.config(text="")


#dinno variables(images)
img_messageSender= ImageTk.PhotoImage(Image.open("./Images/sendMessage.png"))

#dinno variables(Frames)
BackGroundFrame = Frame(root, bg="light blue")#its the base frame
UserFrame = Frame(BackGroundFrame,bg = "light blue")#create a frame for the chat
ChatSelectionFrame = Frame(BackGroundFrame,bg="light blue")#create a frame for the selection of a chat
ChatNameFrame = Frame(BackGroundFrame,bg = "light blue")#create a frame for the chat name
ChatFrame = Frame(BackGroundFrame,bg="light blue")#create a frame for the chat
UserFunctionFrame1 = Frame(BackGroundFrame,bg="light blue",padx=20,pady=20)#create a frame for the send messages
SendMessageFrame = Frame(BackGroundFrame,bg="light blue")#create a frame for the send messages

idEnter = Entry(logUser, width = 20)
Username = StringVar()
usernaneEnter = Entry(logUser,textvariable = Username,width = 20)
#dinno variables
message = StringVar()#create message string
messageEntered = Entry(SendMessageFrame,textvariable = message,width=60)#create textBox
code = StringVar()#create message string
codeEntered = Entry(UserFunctionFrame1,textvariable = code,width=20)
Id = StringVar()#create message string
IdEntered = Entry(UserFunctionFrame1,textvariable = Id,width=20)

welcome = Label(logUser, text="Welcome to Chat Together")
usernameLabel = Label(logUser, text = "Username")
idLabel = Label(logUser, text = "ID")
#dinno variables(Labels)
UserLabel = Label(UserFrame,text=Username.get(),bg="light blue",fg="white",relief=FLAT)#puts the username in the frame
ChatNameLabel = Label(ChatNameFrame,text="ChatName",bg="light blue",fg="white",relief=FLAT)#puts the chatname in the frame
UserOptionsMessage1 = Label(UserFunctionFrame1,bg="light blue",fg="white",relief=FLAT)
UserOptionsMessage2 = Label(UserFunctionFrame1,bg="light blue",fg="white",relief=FLAT)

SignIn = Button(logUser, text = "Sign In",command=hideId,activebackground = "pink", activeforeground = "blue")
LogIn = Button(logUser, text = "LogIn",command=showId,activebackground = "pink", activeforeground = "blue")
Submit = Button(logUser, text="Submit",command=startUser, activebackground="pink", activeforeground="blue")
#dinno variables
MessageSender = Button(SendMessageFrame,width=20,relief=FLAT,bg="light blue", image = img_messageSender)
CreateChatButton = Button(UserFunctionFrame1,relief=FLAT,bg="light blue", text = "Create Chat",command=create)#makes you create a new chat
LeaveChatButton = Button(UserFunctionFrame1,relief=FLAT,bg="light blue",text = "Leave Chat",command=leave)#makes you leave a new chat
JoinChatButton = Button(UserFunctionFrame1,relief=FLAT,bg="light blue",text = "Join Chat",command=join)#makes you join a new chat
SendButton = Button(UserFunctionFrame1,relief=FLAT,bg="light blue",text = "Send Info",command=sent)#makes you send what you put 

#scrollbar
canvas = Canvas(ChatFrame,bg="light blue")
scrollbar = Scrollbar(ChatFrame, orient="vertical",bg="light blue", command=canvas.yview)
scrollable_frame = Frame(canvas)
chats = ["ciao"]

def main():
    welcome.place(x=120, y=10)
    usernameLabel.place(x = 30,y = 100)
    usernaneEnter.place(x = 120, y = 100)  
    SignIn.place(x = 140, y = 50)  
    LogIn.place(x = 200, y = 50)
    Submit.place(x=150, y=160)
    root.configure(bg='light blue')
    while True:
        global chats
        #Frames
        BackGroundFrame.pack(fill=BOTH, side=LEFT, expand=True)
        BackGroundFrame.pack_forget()
        UserFrame.grid(row=0,column=0, sticky="nsew")
        ChatSelectionFrame.grid(row=1,column=0,sticky="nsew")
        ChatNameFrame.grid(row=0,column=1, sticky="nsew")
        ChatFrame.grid(row=1,column=1,sticky="nsew")
        UserFunctionFrame1.grid(row=2,column=0,sticky="nsew")
        SendMessageFrame.grid(row=2,column=1,sticky="nsew")

        #DropMenu
        clicked = StringVar()#create a string
        clicked.set("Select a Chat")
        dropMenu = OptionMenu(ChatSelectionFrame,clicked,*chats)#add options in dropMenu
        dropMenu.pack(side=TOP)

        #textBox
        messageEntered.pack(side=LEFT)
        codeEntered.pack(side=BOTTOM)
        IdEntered.pack(side=BOTTOM)

        #button
        MessageSender.pack(side=LEFT)
        CreateChatButton.pack(fill = X, side=LEFT)
        LeaveChatButton.pack(fill = X, side=LEFT)
        JoinChatButton.pack(fill = X, side=LEFT)
        SendButton.pack(fill = X, side=BOTTOM)

        #Labels
        UserLabel.pack()
        ChatNameLabel.pack()
        UserOptionsMessage1.place(relx = 0.0,rely = 0.4,anchor = NW)
        UserOptionsMessage2.place(relx = 0.0,rely = 0.7,anchor = NW)

        #Scrollbar
        scrollable_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both")
        scrollbar.pack(side="left", fill="both")
        # chats = user.chats
        root.mainloop()
main()