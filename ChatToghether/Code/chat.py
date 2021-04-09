import json
from user import User
class Chat:
    def __init__(self, id, name):
        self.id = id
        self.chatFile = open("chat" + str(self.id) + ".txt", "w")
        self.chatFile.close()
        self.users = {}
        self.name = name

    def addMessage(self, message, user):#add a new message
        data = open("chat" + str(self.id) + ".txt", "a")
        sdata = data.write(str(user.username) + ": " + str(message) + "\n")
        data.close()

    def getChat(self):#create a new file storing the chat messages
        data = open("chat" + str(self.id) + ".txt", "r")
        sdata = data.read()
        data.close()
        return sdata
    def addUser(self, user, id):#add a new use to chat
        self.users[self.id] = user