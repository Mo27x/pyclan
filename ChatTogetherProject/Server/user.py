from network import Network
class User:
    def __init__(self, username:str, password:str, chats: dict):
        self.username = username
        self.password = password
        self.chats = chats

    def signin(self, network: Network):
        return network.send([self,"signin", -1])
    
    def login(self, network: Network):
        return network.send([self,"login", -1])

    def createChat(self, chatName: str, chatCode: str, network: Network):
        if chatName != "" and chatCode != "":
            return network.send([self, "create", -1, chatName, chatCode])

    def joinChat(self, chatId: str, chatCode: str, network: Network):
        if chatId != ""  and chatCode != "":
            return network.send([self, "join", chatId, chatCode])

    def getChat(self, chatId: str, network: Network):
        if chatId in self.chats:
            return network.send([self, "get", chatId])

    def sendMessage(self, message: str, chatId: str, network: Network):
        if message != "" and chatId in self.chats:
            return network.send([self, "add", chatId, message])

    def quitChat(self, chatId: str, network: Network):
        if chatId != "":
            return network.send([self, "quit", chatId])

    def addChat(self, chatId: str, chatName: str):
        if not chatId in self.chats:
            self.chats[chatId] = chatName
    
    def removeChat(self, chatId: str):
        if chatId in self.chats:
            del self.chats[chatId]