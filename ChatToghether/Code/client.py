from tkinter import *
from network import Network
from user import User
<<<<<<< HEAD:ChatToghether/Code/client.py
<<<<<<< HEAD:ChatTogether/Code/client.py
=======
import time

def sendMessage(user, network):
    message = ""
    while message == "":
        message = input("Insert the message you want to send: ")
    chatId = ""
    while chatId == "" or len(chatId) != 11:
        chatId = input("Insert the id of the chat: ")
    return network.send([user, "add", chatId, message])
def joinChat(user, network):
    chatCode = ""
    while chatCode == "":
        chatCode = input("Insert the chat's code: ")
    chatId = ""
    while chatId == "" or len(chatId) != 11:
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
    while chatId == "" or len(chatId) != 11:
        chatId = input("Insert the chat's ID: ")
    return network.send([user, "get", chatId])

def quitChat(user, network):
    chatId = ""
    while chatId == "" or len(chatId) != 11:
        chatId = input("Insert the id of the chat you want to delete: ")
    return network.send([user, "quit", chatId])
def login(user, network):
    return network.send([user,"signin", -1])

# Client's main
def main():
    username = ""
    while username == "":
        username = input("Insert your username: ")
    password = input("Insert your password: ")
>>>>>>> parent of 720826a (Updated):ChatTogetherProject/ChatTogether/client.py

    user = User(username, password, {})
    network = Network()
<<<<<<< HEAD:ChatToghether/Code/client.py
<<<<<<< HEAD:ChatTogetherProject/ChatTogether/client.py
    if user.username != "" and len(user.username) <= 8 and len(user.password) >= 8:
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
            backgroundFrame.pack(fill=BOTH, side=LEFT, expand=True)
    else:
        messagebox.showerror("Error", "Username must not be empty and its length must be less than 9, Password lenght must be almost 8")

def joinChat():
    global addChatType
    addChatType = "join"
    sendButton.pack(fill = X, side=BOTTOM)
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
    sendButton.pack(fill = X, side=BOTTOM)
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
        if chatIdName != "" and len(chatIdName) <= 10  and chatCode != "":
            data = user.createChat(chatIdName, chatCode, network)
            messages = data[0]
            user = data[1]
            users = data[2]
            printMessages(messages)
            updateChats()
            printUsers(users)
        else:
            messagebox.showerror("Adding chat error", "None of the fields must be empty and the lenght of the name of the chat must be less than 11")
    elif addChatType == "join":
        if chatIdName != "" and chatCode != "":
            data = user.joinChat(chatIdName, chatCode, network)
            if data[0] == "Id or code is wrong" or data[0] == "You typed wrong data":
                messagebox.showerror("Joining error", data[0])
            else:
                messages = data[0]
                user = data[1]
                users = data[2]
                printMessages(messages)
                updateChats()
                printUsers(users)
        
    sendButton.pack_forget()
    codeEntered.delete(0,END)
    IdNameEnter.delete(0,END)
    codeEntered.pack_forget()
    IdNameEnter.pack_forget()

def updateChats():
    global chats
    for widget in listboxChats.winfo_children():
        widget.destroy()
    chats = []
    for chatId in user.chats:
        chats.append(user.chats[chatId])
    for chat in chats:
        chatCreated = Radiobutton(listboxChats,relief=FLAT,bg="#A4ACFF",text= chat,variable=r, value=chat, command=lambda: updateChat(r.get()))
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
            if chat != "":
                data = user.sendMessage(message,chatId,network)
                messages = data[0]
                user = data[1]
                users = data[2]
                messageEntered.delete(0, END)
                messageSender.pack(side=RIGHT)
                printMessages(messages)
                break

def updateChat(value):
    global chatNameLabel
    global chat
    chat = value
    ChatsId = ""
    for chatId in user.chats:
        if user.chats[chatId] == chat:
            ChatsId = chatId
    getChat()
    chatNameLabel.destroy()
    chatNameLabel = Label(chatNameFrame,text=("Chat Name: " + chat + " Chat Id: " + ChatsId),bg="#CBC9EB",relief=FLAT)
    chatNameLabel.pack()
    printUsers(users)

def getChat():
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

def quitChat():
    global user
    global users
    global chat
    global chatNameLabel
    global listboxChat
    for chatId in user.chats:
        if user.chats[chatId] == chat:
            data = user.quitChat(chatId, network)
            messagebox.showinfo("Quit Chat",data[0])
            user = data[1]
            users = []
            chatNameLabel.destroy()
            chatNameLabel = Label(chatNameFrame,text= '',bg="#CBC9EB",relief=FLAT)
            chatNameLabel.pack()
            for widget in listboxChat.winfo_children():
                widget.destroy()
            updateChats()
            break

def printUsers(users):
    global listboxUsers
    for widget in listboxUsers.winfo_children():
        widget.destroy()
    listboxUsers.delete(0, END)
    for username in users:
        listboxUsers.insert(END, username)

def printMessages(messages):
    global listboxChat
    for widget in listboxChat.winfo_children():
        widget.destroy()
    for message in messages:
        Label(listboxChat, text= message, bg="#A4ACFF").pack(side=TOP, anchor=NW)

root = Tk()
root.title("Howdy")
root.iconbitmap('./Images/ChatTogether.ico')
root.geometry("688x270")
root.configure(bg="#A4ACFF")
root.resizable(False,False)
logUser = Toplevel(bg="#A4ACFF")
logUser.iconbitmap('./Images/ChatTogether.ico')
logUser.geometry("400x200")
logUser.resizable(False,False)
network = None
logged = False
isLogin = False
user = None
addChatType = ""
chat = ""
r = StringVar()

users = []
chats = []
messages = []

#images
img_messageSender= ImageTk.PhotoImage(Image.open("./Images/sendMessage.png"))
#frame
backgroundFrame = LabelFrame(root, bg="#A4ACFF")
usersFrame = LabelFrame(backgroundFrame,bg="#CBC9EB")
usersChatFrame = LabelFrame(backgroundFrame,bg="#A4ACFF") 
userFunctionFrame = LabelFrame(backgroundFrame,bg="#A4ACFF")
addChatFrame = LabelFrame(backgroundFrame,bg="#A4ACFF")
ChatFrame = LabelFrame(backgroundFrame)
chatNameFrame = LabelFrame(backgroundFrame,bg = "#CBC9EB")
sendMessageFrame = LabelFrame(backgroundFrame,bg="#A4ACFF")
userFrame = LabelFrame(backgroundFrame,bg = "#CBC9EB")
chatSelectionFrame = LabelFrame(backgroundFrame,bg="#A4ACFF")
#label
welcome = Label(logUser, text="Welcome to Howdy", bg="#A4ACFF")
usernameLabel = Label(logUser, text = "Username", bg="#A4ACFF")
passwordLabel = Label(logUser, text = "Password", bg="#A4ACFF")
UsersLabel = Label(usersFrame,text="Users",bg="#CBC9EB",relief=FLAT)
chatNameLabel = Label(chatNameFrame,text="ChatName",bg="#CBC9EB",relief=FLAT)
#button
messageSender = Button(sendMessageFrame,width=20,relief=FLAT,bg="#A4ACFF",command=sendMessage, image = img_messageSender)
createChatButton = Button(userFunctionFrame,relief=RAISED,bg="#8EB5F0", text = "Create Chat",command=createChat)
leaveChatButton = Button(chatNameFrame,relief=RAISED,bg="#8EB5F0",text = "Leave Chat",command=quitChat)
joinChatButton = Button(userFunctionFrame,relief=RAISED,bg="#8EB5F0",text = "Join Chat",command=joinChat)
sendButton = Button(addChatFrame,relief=RAISED,bg="#8EB5F0",text = "Submit",command=addChat)
signin = Button(logUser, text = "Sign In",command= lambda: connectUser("signin"), bg="#8EB5F0")
login = Button(logUser, text = "Log In",command= lambda: connectUser("login"), bg="#8EB5F0")
#enter
usernameEnter = Entry(logUser,width = 20)
passwordEnter = Entry(logUser, show='*', width = 20)
codeEntered = Entry(addChatFrame, width=20)
IdNameEnter = Entry(addChatFrame,width=20)
messageEntered = Entry(sendMessageFrame,width=60)
#scrollbar
listboxChat = Listbox(ChatFrame, bg="#A4ACFF")
scrollbarChatY = Scrollbar(ChatFrame, orient=VERTICAL)
scrollbarChatX = Scrollbar(listboxChat, orient=HORIZONTAL)
canvasChat = Canvas(ChatFrame,bg="#A4ACFF")

listboxUsers = Listbox(usersChatFrame, bg="#A4ACFF")
scrollbarUsers = Scrollbar(usersChatFrame)
canvasUsers = Canvas(usersChatFrame, bg="#A4ACFF")

listboxChats = Listbox(chatSelectionFrame, bg="#A4ACFF")
scrollbarChats = Scrollbar(chatSelectionFrame)
canvasChats = Canvas(chatSelectionFrame, bg="#A4ACFF")

listboxChat.config(yscrollcommand=scrollbarChatY.set, xscrollcommand=scrollbarChatX.set)
scrollbarChatY.config(command= listboxChat.yview)
scrollbarChatX.config(command= listboxChat.xview)

listboxUsers.config(yscrollcommand = scrollbarUsers.set)
scrollbarUsers.config(command = listboxUsers.yview)

listboxChats.config(yscrollcommand = scrollbarChats.set)
scrollbarChats.config(command = listboxChats.yview)

def main():
    welcome.place(x= 120, y= 10)
    signin.place(x= 120, y= 120)
    login.place(x= 200, y= 120)
    usernameEnter.place(x = 120, y = 50)
    usernameLabel.place(x = 30, y = 50)
    passwordLabel.place(x = 30 , y = 90)
    passwordEnter.place(x = 120 , y = 90)
 
    userFrame.grid(row=0,column=0, sticky="nsew")
    chatSelectionFrame.grid(row=1,column=0,sticky="nsew")
    chatNameFrame.grid(row=0,column=1, sticky="nsew")
    ChatFrame.grid(row=1,column=1,sticky="nsew")
    userFunctionFrame.grid(row=2,column=0,sticky="nsew")
    addChatFrame.grid(row=2,column=2,sticky="nsew")
    sendMessageFrame.grid(row=2,column=1,sticky="nsew")
    usersChatFrame.grid(row=1,column=2,sticky="nsew")
    usersFrame.grid(row=0,column=2,sticky="nsew")

    messageSender.pack(side=RIGHT)
    createChatButton.pack(fill = X, side=LEFT)
    leaveChatButton.pack(fill = X, side=RIGHT)
    joinChatButton.pack(fill = X, side=LEFT)
    sendButton.pack_forget()
    messageEntered.pack(fill = X,side=LEFT)
    codeEntered.pack_forget()
    IdNameEnter.pack_forget()

    chatNameLabel.pack()
    UsersLabel.pack()

    listboxChat.pack(side = LEFT, fill = BOTH, expand=True)
    scrollbarChatY.pack(side = RIGHT, fill = Y)
    scrollbarChatX.pack(side = BOTTOM, fill = X)

    listboxUsers.pack(side = LEFT, fill = BOTH, expand=True)
    scrollbarUsers.pack(side = RIGHT, fill = Y)

    listboxChats.pack(side = LEFT, fill = BOTH, expand=True)
    scrollbarChats.pack(side = RIGHT, fill = Y)

if __name__ == "__main__":
    main()

while True:
    try:
        root.update()
        if chat != "":
            getChat()
    except:
        pass
=======
    if userId == "":
        user.id = network.getId()
        print("You are user: ", user.id)
=======
import os
import time

def sendMessage(user, network):
    message = ""
    while message == "":
        message = input("Insert the message you want to send: ")
    chatId = ""
    verify = False
    while not verify:
        try:
            verify = True
            chatId = int(input("Insert the id of the chat: ")) # for the tests put 1
        except:
            verify = False
    return network.send([user, "add", chatId, message])
def joinChat(user, network):
    chatId = ""
    chatCode = ""
    while chatCode == "":
        chatCode = input("Insert the chat's code: ")
    verify = False
    while not verify:
        try:
            verify = True
            chatId = int(input("Insert the chat's ID: "))
        except:
            verify = False
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
    chatId = None
    while chatId == None:
        chatId = int(input("Insert the chat's ID: "))
    print(chatId)
    return network.send([user, "get", chatId])

# Client's main
def main():
    username = ""
    password = ""
    while username == "":
        username = input("Insert your username: ")
    while password == ""
        password = input("Insert your password: ")
    # create a user
    user = User(username, password)
    network = Network()
    user.id = int(network.getP())
    print("You are user: ", user.id)
>>>>>>> parent of f955452 (Ready to add GUI):ChatToghether/Code/client.py
    while True:
        function = input("What do you want to do(1: create a chat, 2: join a chat, 3: send a message, other: view messages from selected joined chat): ")
        chatData = []
        if function == "1":
            chatData = createChat(user, network)
            print("The ID of the chat you created is: ", chatData[1])
        elif function == "2":
            chatData = joinChat(user, network)
        elif function == "3":
            chatData = sendMessage(user, network)
        else:
            chatData = getChat(user, network)
        print(chatData[0])
<<<<<<< HEAD:ChatTogether/Code/client.py
main()
>>>>>>> parent of c05a3bd (Upgraded):ChatTogether/Code/client.py
=======
        user.addChat(chatData[1], chatData[2])
main()
>>>>>>> parent of f955452 (Ready to add GUI):ChatToghether/Code/client.py
=======
    while True:
        function = input("What do you want to do(1: create a chat, 2: join a chat, 3: send a message, 4: quit a chat, other: view messages): ")
        chatData = []
        if function == "1":
            chatData = createChat(user, network)
            print("The ID of the chat you created is: ", chatData[3])
        elif function == "2":
            chatData = joinChat(user, network)
        elif function == "3":
            chatData = sendMessage(user, network)
        elif function == "4":
            chatData = quitChat(user, network)
        elif function == "5":
            chatData = getChat(user, network)
        else:
            chatData = login(user, network)
        user = chatData[1]
        print(chatData[0])
        if function == "3":
            print(chatData[2])
main()
>>>>>>> parent of 720826a (Updated):ChatTogetherProject/ChatTogether/client.py
