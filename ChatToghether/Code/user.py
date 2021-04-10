from network import Network

class User:
    def __init__(self, username, password):#Constructor
        self.username = username
        self.password = password
        self.nChats = 0
        self.chats = {}
        self.network = Network()
        self.id = int(self.network.getP())
    
    def joinChat(self, chatId, code):
        return self.network.send([self.id, -1, "join", self.username, code, chatId])

    def getChat(self, chatId):
        return self.network.send([self.id, chatId, "get", self.username])

    def sendMessage(self, chatId, message):
        if message != None:
            return self.network.send([self.id, chatId,"add", self.username, message])
    
    def createChat(self, chatName, chatCode):
        if chatName != "" and chatCode != "":
            return self.network.send([self.id, -1, "create", self.username, chatName, chatCode])
    
    def addChat(self, chatId, chatName):
        if not chatId in self.chats:
            self.chats[chatId] = chatName