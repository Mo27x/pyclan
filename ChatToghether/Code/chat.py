import json
class Chat:
    def __init__(self, id, name,username, userId, code):
        self.id = id
        self.chatFile = open("chat" + str(self.id) + ".txt", "w+")
        self.chatFile.close()
        self.users = {}
        self.name = name
        self.code = code
        self.addUser(userId,username, self.code, self.id)

    def addMessage(self, username, message, userId):#add a new message
        if userId in self.users:
            self.chatFile = open("chat" + str(self.id) + ".txt", "a")
            self.chatFile.write(str(username) + ": " + str(message) + "\n")
            self.chatFile.close()

    def getChat(self, userId):#create a new file storing the chat messages
        if userId in self.users:
            self.chatFile = open("chat" + str(self.id) + ".txt", "r")
            ret = self.chatFile.read()
            self.chatFile.close()
            return [ret, self.id, self.name]

    def addUser(self, userId, username, code, id): # add a new user to chat
        if self.code == code and self.id == id and userId not in self.users:
            self.users[userId] = username
            return self.getChat(userId)