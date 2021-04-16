from tkinter import *
from network import Network
from user import User
import time

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

# Client's main
def main():
    username = ""
    while username == "":
        username = input("Insert your username: ")
    userId = input("Insert your id if you have one, else press enter: ")

    user = User(username, userId, {})
    network = Network()
    if userId == "":
        user.id = network.getId()
        print("You are user: ", user.id)
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
        else:
            chatData = getChat(user, network)
        user = chatData[1]
        print(chatData[0])
        print(chatData[2])
main()