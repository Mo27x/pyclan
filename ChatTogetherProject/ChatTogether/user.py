from network import Network
class User:
    def __init__(self, username, password, chats: dict):
        if username != "" and len(username) <= 10 and len(password) >= 8:
            self.username = username
            self.password = password
            self.chats = chats
        else:
            self = None
            return self      

    def signin(self, network):
        return network.send([self,"signin", -1])
    
    def login(self, network):
        return network.send([self,"login", -1])

    def createChat(self, chatName, chatCode, network):
        if chatName != "" and chatCode != "":
            return network.send([self, "create", -1, chatName, chatCode])

    def joinChat(self, chatId, chatCode, network):
        if chatId != ""  and chatCode != "":
            return network.send([self, "join", chatId, chatCode])

    def getChat(self, chatId, network):
        if chatId in self.chats:
            return network.send([self, "get", chatId])

    def sendMessage(self, message, chatId, network):
        if message != "" and chatId in self.chats:
            return network.send([self, "add", chatId, message])

    def quitChat(self, chatId, network):
        if chatId != "":
            return network.send([self, "quit", chatId])

    def addChat(self, chatId, chatName):
        if not chatId in self.chats:
            self.chats[chatId] = chatName
    
    def removeChat(self, chatId):
        if chatId in self.chats:
            del self.chats[chatId]