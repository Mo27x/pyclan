from tkinter import *
from tkinter import messagebox
from tkinter.font import Font

from PIL import ImageTk, Image

from network import Network
from user import User


def connectUser(type):
    global user
    global network
    global logged
    global logUser
    username = usernameEnter.get()
    password = passwordEnter.get()
    user = User(username, password, {})
    network = Network()
    if user.username != "" and len(user.username) <= 8 <= len(user.password):
        data = []
        if type == "login":
            data = user.login(network)
        elif type == "signin":
            data = user.signin(network)
        logged = data[2]
        user = data[1]
        updateChats()
        if not logged:
            messagebox.showerror("Connection error", data[0])
        else:
            logUser.destroy()
            backgroundFrame.pack(fill=BOTH, side=LEFT, expand=True)
            Label(userFrame, text=user.username, bg="#CBC9EB", relief=FLAT, font=test).pack(side=LEFT)
    else:
        messagebox.showerror("Error",
                             "Username must not be empty and its length must be less than 9, Password lenght must be almost 8")


def joinChat():
    global addChatType
    addChatType = "join"
    sendButton.pack(fill=X, side=BOTTOM)
    codeEntered.pack(side=BOTTOM)
    IdNameEnter.pack(side=BOTTOM)
    codeEntered.delete(0, END)
    IdNameEnter.delete(0, END)
    IdNameEnter.selection_range(0, END)
    codeEntered.selection_range(0, END)
    codeEntered.insert(0, "Enter chat code here: ")
    IdNameEnter.insert(0, "Enter chat ID here: ")


def createChat():
    global addChatType
    addChatType = "create"
    sendButton.pack(fill=X, side=BOTTOM)
    codeEntered.pack(side=BOTTOM)
    IdNameEnter.pack(side=BOTTOM)
    codeEntered.delete(0, END)
    IdNameEnter.delete(0, END)
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
        if chatIdName != "" and len(chatIdName) <= 16 and chatCode != "":
            data = user.createChat(chatIdName, chatCode, network)
            messages = data[0]
            user = data[1]
            users = data[2]
            updateChats()
        else:
            messagebox.showerror("Adding chat error",
                                 "None of the fields must be empty and the lenght of the name of the chat can be almost 16")
    elif addChatType == "join":
        if chatIdName != "" and chatCode != "":
            data = user.joinChat(chatIdName, chatCode, network)
            if data[0] == "Id or code is wrong" or data[0] == "You typed wrong data":
                messagebox.showerror("Joining error", data[0])
            else:
                messages = data[0]
                user = data[1]
                users = data[2]
                updateChats()

    sendButton.pack_forget()
    codeEntered.delete(0, END)
    IdNameEnter.delete(0, END)
    codeEntered.pack_forget()
    IdNameEnter.pack_forget()


def updateChats():
    global chats
    for widget in scrollableChats_frame.winfo_children():
        widget.destroy()
    chats = []
    for chatId in user.chats:
        chats.append(user.chats[chatId])
    for chat in chats:
        Radiobutton(scrollableChats_frame, relief=FLAT, bg="#A4ACFF", text=chat, variable=r, value=chat,
                    command=lambda: updateChat(r.get()), font=test).pack()
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
                data = user.sendMessage(message, chatId, network)
                messages = data[0]
                user = data[1]
                users = data[2]
                messageEntered.delete(0, END)
                messageSender.pack(side=RIGHT)
                printMessages(messages)
                break


def updateChat(value: str):
    global chatNameLabel
    global chat
    chat = value
    ChatsId = ""
    for chatId in user.chats:
        if user.chats[chatId] == chat:
            ChatsId = chatId
    getChat()
    chatNameLabel.destroy()
    chatNameLabel = Label(chatNameFrame, text=("Chat Name: " + chat + " Chat Id: " + ChatsId), bg="#CBC9EB",
                          relief=FLAT, font=test)
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
    global scrollableChat_frame
    for chatId in user.chats:
        if user.chats[chatId] == chat:
            data = user.quitChat(chatId, network)
            messagebox.showinfo("Quit Chat", data[0])
            user = data[1]
            users = []
            chatNameLabel.destroy()
            chatNameLabel = Label(chatNameFrame, text='', bg="#CBC9EB", relief=FLAT, font=test)
            chatNameLabel.pack()
            for widget in scrollableChat_frame.winfo_children():
                widget.destroy()
            updateChats()
            break


def printUsers(usernames: list):
    global scrollableUsers_frame
    for widget in scrollableUsers_frame.winfo_children():
        widget.destroy()
    for username in usernames:
        Label(scrollableUsers_frame, text=username, bg="#A4ACFF", font=test).pack()


def printMessages(messages: str):
    global scrollableChat_frame
    for widget in scrollableChat_frame.winfo_children():
        widget.destroy()
    for message in messages:
        Label(scrollableChat_frame, text=message, bg="#A4ACFF", font=test).pack(side=TOP, anchor=NW)


root = Tk()
root.title("Howdy")
root.iconbitmap('./Images/howdy.ico')
root.configure(bg="#A4ACFF")
root.resizable(False, False)
logUser = Toplevel(bg="#A4ACFF")
logUser.iconbitmap('./Images/howdy.ico')
logUser.geometry("400x200")
logUser.resizable(False, False)
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

# font size
test = Font(family="Quicksand", size=11)
# images
img_messageSender = ImageTk.PhotoImage(Image.open("./Images/sendMessage.png"))
# frame
backgroundFrame = LabelFrame(root, bg="#A4ACFF")
usersFrame = LabelFrame(backgroundFrame, bg="#CBC9EB")
usersChatFrame = LabelFrame(backgroundFrame, bg="#A4ACFF")
userFunctionFrame = LabelFrame(backgroundFrame, bg="#A4ACFF")
addChatFrame = LabelFrame(backgroundFrame, bg="#A4ACFF")
ChatFrame = LabelFrame(backgroundFrame)
chatNameFrame = LabelFrame(backgroundFrame, bg="#CBC9EB")
sendMessageFrame = LabelFrame(backgroundFrame, bg="#A4ACFF")
userFrame = LabelFrame(backgroundFrame, bg="#CBC9EB")
chatSelectionFrame = LabelFrame(backgroundFrame, bg="#A4ACFF")
# label
welcome = Label(logUser, text="Welcome to Howdy", bg="#A4ACFF", font=test)
usernameLabel = Label(logUser, text="Username", bg="#A4ACFF", font=test)
passwordLabel = Label(logUser, text="Password", bg="#A4ACFF", font=test)
UsersLabel = Label(usersFrame, text="Users", bg="#CBC9EB", relief=FLAT, font=test)
chatNameLabel = Label(chatNameFrame, text="ChatName", bg="#CBC9EB", relief=FLAT, font=test)
# button
messageSender = Button(sendMessageFrame, width=20, relief=FLAT, bg="#A4ACFF", command=sendMessage,
                       image=img_messageSender)
createChatButton = Button(userFunctionFrame, relief=RAISED, bg="#8EB5F0", text="Create Chat", command=createChat,
                          font=test)
leaveChatButton = Button(chatNameFrame, relief=RAISED, bg="#8EB5F0", text="Leave Chat", command=quitChat, font=test)
joinChatButton = Button(userFunctionFrame, relief=RAISED, bg="#8EB5F0", text="Join Chat", command=joinChat, font=test)
sendButton = Button(addChatFrame, relief=RAISED, bg="#8EB5F0", text="Submit", command=addChat, font=test)
signin = Button(logUser, text="SignUp", command=lambda: connectUser("signin"), bg="#8EB5F0", font=test)
login = Button(logUser, text="LogIn", command=lambda: connectUser("login"), bg="#8EB5F0", relief=FLAT, font=test)
# enter
usernameEnter = Entry(logUser, width=20, font=test)
passwordEnter = Entry(logUser, show='*', width=20, font=test)
codeEntered = Entry(addChatFrame, width=20, font=test)
IdNameEnter = Entry(addChatFrame, width=20, font=test)
messageEntered = Entry(sendMessageFrame, width=60, font=test)

# scrollbar
containerChat = Frame(ChatFrame, bg="#A4ACFF")
canvasChat = Canvas(containerChat, width=500, bg="#A4ACFF")
scrollbarChatY = Scrollbar(containerChat, orient="vertical", command=canvasChat.yview, bg="#A4ACFF")
scrollbarChatX = Scrollbar(ChatFrame, orient="horizontal", command=canvasChat.xview, bg="#A4ACFF")
scrollableChat_frame = Frame(canvasChat, bg="#A4ACFF")
scrollableChat_frame.bind("<Configure>", lambda e: canvasChat.configure(scrollregion=canvasChat.bbox("all")))
canvasChat.create_window((0, 0), window=scrollableChat_frame, anchor="nw")
canvasChat.configure(yscrollcommand=scrollbarChatY.set, xscrollcommand=scrollbarChatX.set)

containerChat.pack()
canvasChat.pack(side="left", fill="both", expand=True)
scrollbarChatY.pack(side="right", fill="y")
scrollbarChatX.pack(side="bottom", fill="x")
# chats
containerChats = Frame(chatSelectionFrame, bg="#A4ACFF")
canvasChats = Canvas(containerChats, width=150, bg="#A4ACFF")
scrollbarChatsY = Scrollbar(containerChats, orient="vertical", command=canvasChats.yview, bg="#A4ACFF")
scrollableChats_frame = Frame(canvasChats, bg="#A4ACFF")
scrollableChats_frame.bind("<Configure>", lambda e: canvasChats.configure(scrollregion=canvasChats.bbox("all")))
canvasChats.create_window((0, 0), window=scrollableChats_frame, anchor="nw")
canvasChats.configure(yscrollcommand=scrollbarChatsY.set)

containerChats.pack()
canvasChats.pack(side="left", fill="both", expand=True)
scrollbarChatsY.pack(side="right", fill="y")
# users
containerUsers = Frame(usersChatFrame, bg="#A4ACFF")
canvasUsers = Canvas(containerUsers, width=150, bg="#A4ACFF")
scrollbarUsersY = Scrollbar(containerUsers, orient="vertical", command=canvasUsers.yview, bg="#A4ACFF")
scrollableUsers_frame = Frame(canvasUsers, bg="#A4ACFF")
scrollableUsers_frame.bind("<Configure>", lambda e: canvasUsers.configure(scrollregion=canvasUsers.bbox("all")))
canvasUsers.create_window((0, 0), window=scrollableUsers_frame, anchor="nw")
canvasUsers.configure(yscrollcommand=scrollbarUsersY.set)

containerUsers.pack()
canvasUsers.pack(side="left", fill="both", expand=True)
scrollbarUsersY.pack(side="right", fill="y")


def main():
    welcome.place(x=120, y=10)
    signin.place(x=183, y=120)
    login.place(x=120, y=120)
    usernameEnter.place(x=120, y=50)
    usernameLabel.place(x=30, y=50)
    passwordLabel.place(x=30, y=90)
    passwordEnter.place(x=120, y=90)

    userFrame.grid(row=0, column=0, sticky="nsew")
    chatSelectionFrame.grid(row=1, column=0, sticky="nsew")
    chatNameFrame.grid(row=0, column=1, sticky="nsew")
    ChatFrame.grid(row=1, column=1, sticky="nsew")
    userFunctionFrame.grid(row=2, column=0, sticky="nsew")
    addChatFrame.grid(row=2, column=2, sticky="nsew")
    sendMessageFrame.grid(row=2, column=1, sticky="nsew")
    usersChatFrame.grid(row=1, column=2, sticky="nsew")
    usersFrame.grid(row=0, column=2, sticky="nsew")

    UsersLabel.pack()

    messageSender.pack(side=RIGHT)
    createChatButton.pack(fill=X, side=LEFT)
    leaveChatButton.pack(fill=X, side=RIGHT)
    joinChatButton.pack(fill=X, side=LEFT)
    sendButton.pack_forget()
    messageEntered.pack(fill=X, side=LEFT, expand=True)
    codeEntered.pack_forget()
    IdNameEnter.pack_forget()


if __name__ == "__main__":
    main()

while True:
    root.update()
    if chat != "":
        getChat()
    root.update_idletasks()
