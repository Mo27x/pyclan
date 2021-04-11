from network import Network
from user import User
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
    while password == "":
        password = input("Insert your password: ")
    # create a user
    user = User(username, password)
    network = Network()
    user.id = int(network.getP())
    print("You are user: ", user.id)
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
        user.addChat(chatData[1], chatData[2])
main()