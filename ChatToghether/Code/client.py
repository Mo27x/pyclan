from network import Network
from user import User
import os
import time

def sendMessage(user):
    message = ""
    while message == "":
        message = input("Insert your username: ")
    chatId = ""
    verify = False
    while not verify:
        try:
            verify = True
            chatId = int(input("Insert the id of the chat: ")) # for the tests put 1
        except:
            verify = False
    user.sendMessage(chatId, message)
def joinChat(user):
    chatName = ""
    chatId = ""
    while chatName != "" and chatCode != "":
        chatName = input("Insert the chat's name: ")
        chatCode = input("Insert the chat's code: ")
    user.joinChat(chatId, chatName)

def createChat(user):
    chatName = ""
    chatCode = ""
    while chatName == "":
        chatName = input("Insert the name of the chat you want to create: ")
    while chatCode == "":
        chatCode = input("Insert the code of the chat you want to create: ")
    user.createChat(chatName, chatCode)    

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
    print("You are user: ", user.id)
    createChat(user)
    while True:
        function = input("What you want to do: ")
        if function == 1:
            createChat(user)
        elif function == 2:
            joinChat(user)
        elif function == 3:
            sendMessage(user)
        chatData = user.getChat(1)
        user.addChat(chatData[1], chatData[2])
        print(chatData[0])
        time.sleep(1)
        os.system('cls')
main()