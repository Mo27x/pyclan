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

#images
img_messageSender= ImageTk.PhotoImage(Image.open("./Images/sendMessage.png"))

#Frames
BackGroundFrame = tk.Frame(root, width=200, height=100, bg="light blue")
BackGroundFrame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

UserFrame = tk.LabelFrame(BackGroundFrame,bg = "light blue",padx = 100 , pady = 5)#create a frame for the chat
UserFrame.grid(row=0,column=0, sticky="nsew")

ChatSelectionFrame = tk.LabelFrame(BackGroundFrame,bg="light blue",padx = 100 , pady = 300)#create a frame for the selection of a chat
ChatSelectionFrame.grid(row=1,column=0,sticky="nsew")

ChatNameFrame = tk.LabelFrame(BackGroundFrame,bg = "light blue",padx = 100 , pady = 5)#create a frame for the chat name
ChatNameFrame.grid(row=0,column=1, sticky="nsew")

ChatFrame = tk.LabelFrame(BackGroundFrame,bg="light blue",padx = 200 , pady = 300)#create a frame for the chat
ChatFrame.grid(row=1,column=1,sticky="nsew")

#DropMenu
clicked = tk.StringVar()#create a string
clicked.set("Select a Chat")#set text in dropBox
dropMenu = tk.OptionMenu(ChatSelectionFrame,clicked,*chats)#add options in dropBox
dropMenu.pack()

#textBox
message = tk.StringVar()
messageEntered = tk.Entry(ChatFrame,textvariable = message)
messageEntered.pack(fill = tk.X,side=LEFT)

#button
MessageSender = tk.Button(ChatFrame,width = 60,relief=tk.FLAT,bg="light blue",image=img_messageSender)
MessageSender.pack(side=LEFT)

#Labels
UserLabel = tk.Label(UserFrame,text="Username",bg="light blue",fg="white",relief=tk.FLAT)#puts the username in the frame
UserLabel.pack()

ChatNameLabel = tk.Label(ChatNameFrame,text="ChatName",bg="light blue",fg="white",relief=tk.FLAT)#puts the chatname in the frame
ChatNameLabel.pack()

Message =tk.Label(ChatFrame,text="message",bg="light blue",fg="white",relief=tk.FLAT)
Message.pack(side=TOP)

#scrollbar
canvas = tk.Canvas(ChatFrame,bg="light blue")
scrollbar = tk.Scrollbar(ChatFrame, orient="vertical",bg="light blue", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

for i in range(50):
    tk.Label(scrollable_frame,bg="light blue", text="message").pack()

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


root.mainloop()