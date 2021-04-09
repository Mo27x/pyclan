import json
from user import User
class Chat:
    def __init__(self, id):
        self.id = id
        self.chatFile = open("chat" + str(self.id) + ".txt", "r")
        self.chatFile.close()
        self.users = {}

    def addMessage(self, message, sender):
        data = open("chat" + str(self.id) + ".txt", "a")
        sdata = data.write(str(sender) + ": " + str(message) + "\n")
        data.close()

    def getChat(self):
        data = open("chat" + str(self.id) + ".txt", "r")
        sdata = data.read()
        data.close()
        return sdata
    def addUser(self, user, id):
        self.users[self.id] = user