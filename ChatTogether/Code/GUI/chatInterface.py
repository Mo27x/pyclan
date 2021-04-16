from tkinter import *
from PIL import ImageTk,Image
import tkinter as tk

root = tk.Tk()
root.title("ChatTogether")
root.iconbitmap('./Images/ChatTogether.ico')

chats = [ #array of chats
    "chat1",
    "chat2",
    "chat3"
]

def printMessage():
    if message.get() != "":
        Message = tk.Label(scrollable_frame,text="Utente: " + message.get(),bg="light blue",fg="black",relief=tk.FLAT)
        Message.pack()

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

#images
img_messageSender= ImageTk.PhotoImage(Image.open("./Images/sendMessage.png"))

#Frames
BackGroundFrame = tk.Frame(root, bg="light blue")
BackGroundFrame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

UserFrame = tk.LabelFrame(BackGroundFrame,bg = "light blue")#create a frame for the chat
UserFrame.grid(row=0,column=0, sticky="nsew")

ChatSelectionFrame = tk.LabelFrame(BackGroundFrame,bg="light blue")#create a frame for the selection of a chat
ChatSelectionFrame.grid(row=1,column=0,sticky="nsew")

ChatNameFrame = tk.LabelFrame(BackGroundFrame,bg = "light blue")#create a frame for the chat name
ChatNameFrame.grid(row=0,column=1, sticky="nsew")

ChatFrame = tk.LabelFrame(BackGroundFrame,bg="light blue")#create a frame for the chat
ChatFrame.grid(row=1,column=1,sticky="nsew")

UserFunctionFrame1 = tk.LabelFrame(BackGroundFrame,bg="light blue",padx=20,pady=20)#create a frame for the send messages
UserFunctionFrame1.grid(row=2,column=0,sticky="nsew")

SendMessageFrame = tk.LabelFrame(BackGroundFrame,bg="light blue")#create a frame for the send messages
SendMessageFrame.grid(row=2,column=1,sticky="nsew")


#DropMenu
clicked = tk.StringVar()#create a string
clicked.set("Select a Chat")#set text in dropBox
dropMenu = tk.OptionMenu(ChatSelectionFrame,clicked,*chats)#add options in dropBox
dropMenu.pack(side=TOP)

#textBox
message = tk.StringVar()#create message string
messageEntered = tk.Entry(SendMessageFrame,textvariable = message,width=60)#create textBox
messageEntered.pack(side=LEFT)

code = tk.StringVar()#create message string
codeEntered = tk.Entry(UserFunctionFrame1,textvariable = code,width=20)
codeEntered.pack(side=BOTTOM)

Id = tk.StringVar()#create message string
IdEntered = tk.Entry(UserFunctionFrame1,textvariable = Id,width=20)
IdEntered.pack(side=BOTTOM)

#button
MessageSender = tk.Button(SendMessageFrame,width=20,relief=tk.FLAT,bg="light blue",command=printMessage, image = img_messageSender)#size 20 x 20
MessageSender.pack(side=LEFT)

CreateChatButton = tk.Button(UserFunctionFrame1,relief=tk.FLAT,bg="light blue", text = "Create Chat",command=create)#makes you create a new chat
CreateChatButton.pack(fill = tk.X, side=LEFT)

LeaveChatButton = tk.Button(UserFunctionFrame1,relief=tk.FLAT,bg="light blue",text = "Leave Chat",command=leave)#makes you leave a new chat
LeaveChatButton.pack(fill = tk.X, side=LEFT)

JoinChatButton = tk.Button(UserFunctionFrame1,relief=tk.FLAT,bg="light blue",text = "Join Chat",command=join)#makes you join a new chat
JoinChatButton.pack(fill = tk.X, side=LEFT)

SendButton = tk.Button(UserFunctionFrame1,relief=tk.FLAT,bg="light blue",text = "Send Info",command=sent)#makes you send what you put 
SendButton.pack(fill = tk.X, side=BOTTOM)

#Labels
UserLabel = tk.Label(UserFrame,text="Username",bg="light blue",fg="white",relief=tk.FLAT)#puts the username in the frame
UserLabel.pack()

ChatNameLabel = tk.Label(ChatNameFrame,text="ChatName",bg="light blue",fg="white",relief=tk.FLAT)#puts the chatname in the frame
ChatNameLabel.pack()

UserOptionsMessage1 = tk.Label(UserFunctionFrame1,bg="light blue",fg="white",relief=tk.FLAT)
UserOptionsMessage1.place(relx = 0.0,rely = 0.4,anchor = NW)

UserOptionsMessage2 = tk.Label(UserFunctionFrame1,bg="light blue",fg="white",relief=tk.FLAT)
UserOptionsMessage2.place(relx = 0.0,rely = 0.7,anchor = NW)


#scrollbar
canvas = tk.Canvas(ChatFrame,bg="light blue")

scrollbar = tk.Scrollbar(ChatFrame, orient="vertical",bg="light blue", command=canvas.yview)

scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both")

scrollbar.pack(side="left", fill="both")


root.mainloop()#dinno variables