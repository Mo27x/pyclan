from tkinter import *

root = Tk()
root.title("ChatTogether")
root.iconbitmap('./Images/ChatTogether.ico')
dimentions = root.geometry("800x800")

chats = [ #array of chats
    "chat1",
    "chat2",
    "chat3"
]

UserFrame = LabelFrame(root, bg = "blue",padx = 100 , pady = 10)#create a frame for the chat
UserFrame.grid(row=0,column =0,padx = 1 , pady = 1)

ChatNameFrame = LabelFrame(root, bg = "blue",padx = 100 , pady = 10)#create a frame for the chat name
ChatNameFrame.grid(row=0,column =1,padx = 1 , pady = 1)

ChatSelectionFrame = LabelFrame(root, bg = "blue",padx = 100 , pady = 300)#create a frame for the selection of a chat
ChatSelectionFrame.grid(row=1,column =0,padx = 0 , pady = 0)

ChatFrame = LabelFrame(root, bg = "blue",padx = 200 , pady = 300)#create a frame for the chat
ChatFrame.grid(row=1,column =1,padx = 0 , pady = 0)


UserLabel = Label(UserFrame,text="Username",bg="blue",fg="white")#puts the username in the frame
UserLabel.pack()

ChatNameLabel = Label(ChatNameFrame,text="ChatName",bg ="blue",fg="white")#puts the chatname in the frame
ChatNameLabel.pack()

Chat = Label(ChatFrame,text="ChatHere",bg ="blue",fg="white")#puts the chatname in the frame
Chat.pack()


clicked = StringVar()#create a string
clicked.set("Select a Chat")#set text in dropBox
drop = OptionMenu(ChatSelectionFrame,clicked,*chats)#add options in dropBox
drop.pack()


root.mainloop()