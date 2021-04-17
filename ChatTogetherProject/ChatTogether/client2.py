from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from network import Network
from user import User
import time

def printMessage(messages):
    global scrollable_frame
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    for message in messages:
        Message = Label(scrollable_frame,text= message,bg="light blue",fg="black",relief= FLAT)
        Message.pack()

def sendMessage():
    global messageEntered
    global messages
    global user
    global users
    message = messageEntered.get()
    chat = clicked.get()
    for chatId in user.chats:
        if chatId == chat:
            data =  network.send([user, "add", chatId, message])
            messages = data[0]
            user = data[1]
            users = data[2]

def joinChat():
    global addChatType
    UserOptionsMessage1.config(text="Id")
    UserOptionsMessage2.config(text="Code")
    addChatType = "join"

def createChat():
    global user
    global network
    UserOptionsMessage1.config(text="Name")
    UserOptionsMessage2.config(text="Code")

def addChat():
    global user
    global network
    global users
    global messages
    global chats
    chatIdName = IdNameEnter.get()
    chatCode = codeEntered.get()
    if addChatType == "create":
        if chatIdName != "" and len(chatCode) >= 8:
            data = network.send([user, addChatType, -1, chatIdName, chatCode])
            messages = data[0]
            user = data[1]
            users = data[2]
            chats = []
            for chat in user.chats:
                chats.append(user.chats[chat])
    elif addChatType == "join":
        if chatIdName != "" and len(chatCode) >= 8:
            data = network.send([user, addChatType, chatIdName, chatCode])
            user = data[1]
            users = data[2]
            chats = []
            for chat in user.chats:
                chats.append(user.chats[chat])

        

def getChat(user: User, network):
    global messages
    global users
    chat = clicked.get()
    for chatId in user.chats:
        if chatId == chat:
            data = network.send([user, "get", chatId])
            messages = data[0]
            user = data[1]
            users = data[2]
            break

def quitChat(user, network):
    chatId = ""
    while chatId == "" or len(chatId) != 6:
        chatId = input("Insert the id of the chat you want to delete: ")
    return network.send([user, "quit", chatId])

def show():
    p = passwordEnter.get()

def InfoChatUsers():
    for widget in UsersChatFrame.winfo_children():
        widget.destroy()
    for i,name in enumerate(users):
        user = Label(UsersChatFrame,text=name,bg="light blue",fg="white",relief=FLAT)
        user.pack(side = TOP)

def connectUser(type: str):
    global user
    global network
    global logged
    global logUser
    username = usernameEnter.get()
    password = passwordEnter.get()
    if username != "" and len(password) >= 8:
        user = User(username, password, {})
        network = Network()
        logged = network.send([user, type, -1])[2]

    if logged == True:
        logUser.destroy()
        BackGroundFrame.pack(fill=BOTH, side=LEFT, expand=True)

root = Tk()
root.title("Chat Together")
root.iconbitmap('./Images/ChatTogether.ico')
root.geometry("778x393")
root.configure(bg="light blue")
root.resizable(False,False)
logUser = Toplevel(bg="light blue")
logUser.iconbitmap('./Images/ChatTogether.ico')
logUser.geometry("400x200")
logUser.resizable(False,False)
user = User("", "", {})
network = None
logged = False
isLogin = False
addChatType = ""

Open = False
users = []
chats = [""]
messages = []

#images
img_messageSender= ImageTk.PhotoImage(Image.open("./Images/sendMessage.png"))
#frame
BackGroundFrame = LabelFrame(root, bg="light blue")
UsersFrame = LabelFrame(BackGroundFrame,bg="light blue") 
UsersChatFrame = LabelFrame(BackGroundFrame,bg="light blue") 
UserFunctionFrame1 = LabelFrame(BackGroundFrame,bg="light blue",padx=20,pady=20)
ChatFrame = LabelFrame(BackGroundFrame,bg="light blue")
ChatNameFrame = LabelFrame(BackGroundFrame,bg = "light blue")
SendMessageFrame = LabelFrame(BackGroundFrame,bg="light blue")
UserFrame = LabelFrame(BackGroundFrame,bg = "light blue")
ChatSelectionFrame = LabelFrame(BackGroundFrame,bg="light blue")
#label
welcome = Label(logUser, text="Welcome to Chat Together")
usernameLabel = Label(logUser, text = "Username")
passwordLabel = Label(logUser, text = "Password")
UserOptionsMessage1 = Label(UserFunctionFrame1,bg="light blue",fg="white",relief=FLAT)
UserOptionsMessage2 = Label(UserFunctionFrame1,bg="light blue",fg="white",relief=FLAT)
Users = Label(UsersFrame,bg="light blue",fg="white",relief=FLAT)
#drop down menu
clicked = StringVar()
clicked.set(chats[0])
dropMenu = OptionMenu(ChatSelectionFrame,clicked,*chats)
#button
MessageSender = Button(SendMessageFrame,width=20,relief=FLAT,bg="light blue",command=getChat, image = img_messageSender)
CreateChatButton = Button(UserFunctionFrame1,relief=RAISED,bg="light blue", text = "Create Chat",command=createChat)
LeaveChatButton = Button(ChatNameFrame,relief=RAISED,bg="light blue",text = "Leave Chat",command=quitChat)
JoinChatButton = Button(UserFunctionFrame1,relief=RAISED,bg="light blue",text = "Join Chat",command=joinChat)
SendButton = Button(UserFunctionFrame1,relief=RAISED,bg="cyan",text = "Submit",command=addChat)
SignIn = Button(logUser, text = "Sign In",command= lambda: connectUser("signin"),activebackground = "pink", activeforeground = "blue")
Login = Button(logUser, text = "Login",command= lambda: connectUser("login"),activebackground = "pink", activeforeground = "blue")
#enter
usernameEnter = Entry(logUser,width = 20)
passwordEnter = Entry(logUser, show='*', width = 20)
codeEntered = Entry(UserFunctionFrame1, width=20)
IdNameEnter = Entry(UserFunctionFrame1,width=20)
messageEntered = Entry(SendMessageFrame,width=60)
codeEntered = Entry(UserFunctionFrame1, width=20)
IdNameEnter = Entry(UserFunctionFrame1,width=20)
#scrollbar chat
canvasChat = Canvas(ChatFrame,bg="light blue")
scrollbarChat = Scrollbar(ChatFrame, orient="vertical",bg="light blue", command=canvasChat.yview)
scrollable_frame = Frame(canvasChat)
scrollable_frame.bind("<Configure>",lambda e: canvasChat.configure(scrollregion=canvasChat.bbox("all")))
canvasChat.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvasChat.configure(yscrollcommand=scrollbarChat.set)

scrollbar = Scrollbar(UsersChatFrame)
scrollbar.pack( side = RIGHT, fill = Y )
mylist = Listbox(UsersChatFrame, yscrollcommand = scrollbar.set, bg="light blue" )
for username in users:
    mylist.insert(END,username)


def main():
    #Start window
    welcome.place(x= 120, y= 10)
    SignIn.place(x= 120, y= 120)
    Login.place(x= 200, y= 120)
    usernameEnter.place(x = 120, y = 50)
    usernameLabel.place(x = 30, y = 50)
    passwordLabel.place(x = 30 , y = 90)
    passwordEnter.place(x = 120 , y = 90)
 
    #Chatting window

    #Labels
    UserLabel = Label(UserFrame,text=user.username,bg="light blue",fg="white",relief=FLAT)
    ChatNameLabel = Label(ChatNameFrame,text="ChatName",bg="light blue",fg="white",relief=FLAT)

    mylist.pack( side = LEFT, fill = BOTH )
    scrollbar.config( command = mylist.yview )

    UserFrame.grid(row=0,column=0, sticky="nsew")
    ChatSelectionFrame.grid(row=1,column=0,sticky="nsew")
    ChatNameFrame.grid(row=0,column=1, sticky="nsew")
    ChatFrame.grid(row=1,column=1,sticky="nsew")
    UserFunctionFrame1.grid(row=2,column=0,sticky="nsew")
    SendMessageFrame.grid(row=2,column=1,sticky="nsew")
    UsersChatFrame.grid(row=1,column=2,sticky="nsew")
    UsersFrame.grid(row=1,column=1,sticky="nsew")

    dropMenu.pack(side=TOP)

    messageEntered.pack(side=LEFT)
    codeEntered.pack(side=BOTTOM)
    IdNameEnter.pack(side=BOTTOM)

    MessageSender.pack(side=LEFT)
    CreateChatButton.pack(fill = X, side=LEFT)
    LeaveChatButton.pack(fill = X, side=RIGHT)
    JoinChatButton.pack(fill = X, side=LEFT)
    SendButton.pack(fill = X, side=BOTTOM)

    UserLabel.pack()
    ChatNameLabel.pack()
    User.pack()
    UserOptionsMessage1.place(x = 0,y = 0.4,anchor = NW)
    UserOptionsMessage2.place(x = 0,y = 0.7,anchor = NW)

    canvasChat.pack(side="left", fill="both")
    scrollbarChat.pack(side="left", fill="both")

if __name__ == "__main__":
    main()
root.mainloop()