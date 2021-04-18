from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from network import Network
from user import User
from _thread import *

def printMessages(messages):
    global listboxChat
    for widget in listboxChat.winfo_children():
        widget.destroy()
    for message in messages:
        Label(listboxChat, text= message, bg="light blue").pack(side=TOP, anchor=NW)

def updateChat(value):
    global ChatNameLabel
    global chat
    chat = value
    ChatsId = ""
    for chatId in user.chats:
        if user.chats[chatId] == chat:
            ChatsId = chatId
    getChat()
    ChatNameLabel.destroy()
    ChatNameLabel = Label(ChatNameFrame,text=("Chat Name: " + chat + " Chat Id: " + ChatsId),bg="light blue",fg="white",relief=FLAT)
    ChatNameLabel.pack()
    printUsers(users)

def printUsers(users):
    global listboxUsers
    for widget in listboxUsers.winfo_children():
        widget.destroy()
    for username in users:
        listboxUsers.insert(END, username)

def updateChats():
    global chats
    for widget in listboxChats.winfo_children():
        widget.destroy()
    chats = []
    for chatId in user.chats:
        chats.append(user.chats[chatId])
    for chat in chats:
        chatCreated = Radiobutton(listboxChats,relief=FLAT,bg="light blue",text = chat,variable=r, value=chat, command=lambda: updateChat(r.get()))
        listboxChats.insert(END,chatCreated.pack())
    printUsers(users)

def sendMessage():
    global messageEntered
    global messages
    global user
    global users
    global chat
    users = []
    message = messageEntered.get()
    for chatId in user.chats:
        if user.chats[chatId] == chat:
            data = user.sendMessage(message,chatId,network)
            messages = data[0]
            user = data[1]
            users = data[2]
            messageEntered.delete(0, END)
            MessageSender.pack(side=RIGHT)
            printMessages(messages)
            break

def joinChat():
    global addChatType
    addChatType = "join"
    SendButton.pack(fill = X, side=BOTTOM)
    codeEntered.pack(side=BOTTOM)
    IdNameEnter.pack(side=BOTTOM)
    codeEntered.delete(0,END)
    IdNameEnter.delete(0,END)
    IdNameEnter.selection_range(0, END)
    codeEntered.selection_range(0, END)
    codeEntered.insert(0, "Enter chat code here: ")
    IdNameEnter.insert(0, "Enter chat ID here: ")

def createChat():
    global addChatType
    addChatType = "create"
    SendButton.pack(fill = X, side=BOTTOM)
    codeEntered.pack(side=BOTTOM)
    IdNameEnter.pack(side=BOTTOM)
    codeEntered.delete(0,END)
    IdNameEnter.delete(0,END)
    codeEntered.insert(0, "Enter chat code here: ")
    IdNameEnter.insert(0, "Enter chat name here: ")

def addChat():
    global user
    global network
    global users
    global messages
    global chats
    global addChatType
    users = []
    chatIdName = IdNameEnter.get()
    chatCode = codeEntered.get()
    if addChatType == "create":
        if chatIdName != "" and chatCode != "":
            data = user.createChat(chatIdName, chatCode, network)
            messages = data[0]
            user = data[1]
            users = data[2]
            printMessages(messages)
            updateChats()
            printUsers(users)
    elif addChatType == "join":
        if chatIdName != "" and chatCode != "":
            data = user.joinChat(chatIdName, chatCode, network)
            if data[0] != "Id or code is wrong":
                messages = data[0]
            else:
                messagebox.showerror("Joining error", data[0])
            user = data[1]
            users = data[2]
            printMessages(messages)
            updateChats()
            printUsers(users)
    SendButton.pack_forget()
    codeEntered.delete(0,END)
    IdNameEnter.delete(0,END)
    codeEntered.pack_forget()
    IdNameEnter.pack_forget()

def requestChat():
    global user
    global network
    global messages
    global users
    global chat
    users = []
    for chatId in user.chats:
        if user.chats[chatId] == chat:
            data = user.getChat(chatId, network)
            messages = data[0]
            user = data[1]
            users = data[2]
            printMessages(messages)
            printUsers(users)
            break

def getChat():
    global user
    global network
    global messages
    global users
    global chat
    while True:
        users = []
        for chatId in user.chats:
            if user.chats[chatId] == chat:
                data = user.getChat(chatId, network)
                messages = data[0]
                user = data[1]
                users = data[2]
                printMessages(messages)
                printUsers(users)

def quitChat():
    global user
    global users
    global chat
    for chatId in user.chats:
        if user.chats[chatId] == chat:
            data = user.quitChat(chatId, network)
            messagebox.showinfo(data[0])
            user = data[1]
            users = []
            updateChats()
            break

def connectUser(type: str):
    global user
    global network
    global logged
    global logUser
    global UserLabel
    username = usernameEnter.get()
    password = passwordEnter.get()
    if username != "" and len(password) >= 8:
        user = User(username, password, {})
        network = Network()
        UserLabel.pack()
        if user == None:
            messagebox.showerror("Error", "Username must not be empty, Password lenght must be almost 8")
        data = []
        if type == "login":
            data = user.login(network)
        elif type == "signin":
            data = user.signin(network)
        logged = data[2]
        user = data[1]
        updateChats()
        if logged == False:
            messagebox.showerror("Connection error", data[0])
        else:
            logUser.destroy()
            BackGroundFrame.pack(fill=BOTH, side=LEFT, expand=True)
        UserLabel.destroy()
        UserLabel = Label(UserFrame,text=user.username,bg="light blue",fg="white",relief=FLAT)
        UserLabel.pack()


root = Tk()
root.title("Chat Together")
root.iconbitmap('./Images/ChatTogether.ico')
root.geometry("688x270")
root.configure(bg="light blue")
root.resizable(False,False)
logUser = Toplevel(bg="light blue")
logUser.iconbitmap('./Images/ChatTogether.ico')
logUser.geometry("400x200")
logUser.resizable(False,False)
user = User("Username", "Password", {})
network = None
logged = False
isLogin = False
addChatType = ""
chat = ""
r =StringVar()

Open = False
users = []
chats = []
messages = []

#images
img_messageSender= ImageTk.PhotoImage(Image.open("./Images/sendMessage.png"))
#frame
BackGroundFrame = LabelFrame(root, bg="light blue")
UsersFrame = LabelFrame(BackGroundFrame,bg="light blue") 
UsersChatFrame = LabelFrame(BackGroundFrame,bg="light blue") 
UserFunctionFrame1 = LabelFrame(BackGroundFrame,bg="light blue")
UserFunctionFrame2 = LabelFrame(BackGroundFrame,bg="light blue")
ChatFrame = LabelFrame(BackGroundFrame,bg="light blue")
ChatNameFrame = LabelFrame(BackGroundFrame,bg = "light blue")
SendMessageFrame = LabelFrame(BackGroundFrame,bg="light blue")
UserFrame = LabelFrame(BackGroundFrame,bg = "light blue")
ChatSelectionFrame = LabelFrame(BackGroundFrame,bg="light blue")
#label
welcome = Label(logUser, text="Welcome to Chat Together")
usernameLabel = Label(logUser, text = "Username")
passwordLabel = Label(logUser, text = "Password")
UserLabel = Label(UserFrame,text=user.username,bg="light blue",fg="white",relief=FLAT)
ChatNameLabel = Label(ChatNameFrame,text="ChatName",bg="light blue",fg="white",relief=FLAT)

#button
MessageSender = Button(SendMessageFrame,width=20,relief=FLAT,bg="light blue",command=sendMessage, image = img_messageSender)
CreateChatButton = Button(UserFunctionFrame1,relief=RAISED,bg="light blue", text = "Create Chat",command=createChat)
LeaveChatButton = Button(ChatNameFrame,relief=RAISED,bg="light blue",text = "Leave Chat",command=quitChat)
JoinChatButton = Button(UserFunctionFrame1,relief=RAISED,bg="light blue",text = "Join Chat",command=joinChat)
SendButton = Button(UserFunctionFrame2,relief=RAISED,bg="light blue",text = "Submit",command=addChat)
SignIn = Button(logUser, text = "Sign In",command= lambda: connectUser("signin"),activebackground = "pink", activeforeground = "blue")
Login = Button(logUser, text = "Login",command= lambda: connectUser("login"),activebackground = "pink", activeforeground = "blue")
#enter
usernameEnter = Entry(logUser,width = 20)
passwordEnter = Entry(logUser, show='*', width = 20)
codeEntered = Entry(UserFunctionFrame2, width=20)
IdNameEnter = Entry(UserFunctionFrame2,width=20)
messageEntered = Entry(SendMessageFrame,width=60)
#scrollbar
listboxChat = Listbox(ChatFrame, bg="light blue")
scrollbarChatY = Scrollbar(ChatFrame, orient=VERTICAL)
scrollbarChatX = Scrollbar(listboxChat, orient=HORIZONTAL)
canvasChat = Canvas(ChatFrame,bg="light blue")

listboxUsers = Listbox(UsersChatFrame, bg="light blue")
scrollbarUsers = Scrollbar(UsersChatFrame)
canvasUsers = Canvas(UsersChatFrame, bg="light blue")

listboxChats = Listbox(ChatSelectionFrame, bg="light blue")
scrollbarChats = Scrollbar(ChatSelectionFrame)
canvasChats = Canvas(ChatSelectionFrame, bg="light blue")

listboxChat.config(yscrollcommand=scrollbarChatY.set, xscrollcommand=scrollbarChatX.set)
scrollbarChatY.config(command= listboxChat.yview)
scrollbarChatX.config(command= listboxChat.xview)

listboxUsers.config(yscrollcommand = scrollbarUsers.set)
scrollbarUsers.config(command = listboxUsers.yview)

listboxChats.config(yscrollcommand = scrollbarChats.set)
scrollbarChats.config(command = listboxChats.yview)

def main():
    #Start window
    welcome.place(x= 120, y= 10)
    SignIn.place(x= 120, y= 120)
    Login.place(x= 200, y= 120)
    usernameEnter.place(x = 120, y = 50)
    usernameLabel.place(x = 30, y = 50)
    passwordLabel.place(x = 30 , y = 90)
    passwordEnter.place(x = 120 , y = 90)
 
    #Labels
    UsersLabel = Label(UsersFrame,text="Users",bg="light blue",fg="white",relief=FLAT)

    UserFrame.grid(row=0,column=0, sticky="nsew")
    ChatSelectionFrame.grid(row=1,column=0,sticky="nsew")
    ChatNameFrame.grid(row=0,column=1, sticky="nsew")
    ChatFrame.grid(row=1,column=1,sticky="nsew")
    UserFunctionFrame1.grid(row=2,column=0,sticky="nsew")
    UserFunctionFrame2.grid(row=2,column=2,sticky="nsew")
    SendMessageFrame.grid(row=2,column=1,sticky="nsew")
    UsersChatFrame.grid(row=1,column=2,sticky="nsew")
    UsersFrame.grid(row=0,column=2,sticky="nsew")

    MessageSender.pack(side=RIGHT)
    CreateChatButton.pack(fill = X, side=LEFT)
    LeaveChatButton.pack(fill = X, side=RIGHT)
    JoinChatButton.pack(fill = X, side=LEFT)
    SendButton.pack_forget()

    messageEntered.pack(fill = X,side=LEFT)
    codeEntered.pack_forget()
    IdNameEnter.pack_forget()

    UserLabel.pack()
    ChatNameLabel.pack()
    UsersLabel.pack()

    listboxChat.pack(side = LEFT, fill = BOTH, expand=True)
    scrollbarChatY.pack(side = RIGHT, fill = Y)
    scrollbarChatX.pack(side = BOTTOM, fill = X)

    listboxUsers.pack(side = LEFT, fill = BOTH, expand=True)
    scrollbarUsers.pack(side = RIGHT, fill = Y)

    listboxChats.pack(side = LEFT, fill = BOTH, expand=True)
    scrollbarChats.pack(side = RIGHT, fill = Y)
    start_new_thread(getChat())

if __name__ == "__main__":
    main()
root.mainloop()