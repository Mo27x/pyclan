from network import Network
from user import User
import os

def sendMessage(user):
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
    return user.sendMessage(message, chatId)
def joinChat(user):
    chatId = ""
    chatCode = ""
    while chatId == "":
        chatId = input("Insert the chat's ID: ")
    while chatCode == "":
        chatCode = input("Insert the chat's code: ")
    return user.joinChat(chatId, chatCode)

def createChat(user):
    chatName = ""
    chatCode = ""
    while chatName == "":
        chatName = input("Insert the name of the chat you want to create: ")
    while chatCode == "":
        chatCode = input("Insert the code of the chat you want to create: ")
    return user.createChat(chatName, chatCode)
def getChat(user):
    chatId = ""
    while chatId == "":
        chatId = input("Insert the chat's ID: ")
    user.getChat(chatId)

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
    print("You are user: ", user.id)
    while True:
        function = int(input("What you want to do: "))
        chatData = []
        if function == 1:
            chatData = createChat(user)
            print("The ID of the chat you created is: ", chatData[1])
        elif function == 2:
            chatData = joinChat(user)
        elif function == 3:
            chatData = sendMessage(user)
        else:
            chatData = user.getChat(1)
        print(chatData[0])
        user.addChat(chatData[1], chatData[2])
main()