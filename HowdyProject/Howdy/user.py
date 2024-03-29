class User:
    def __init__(self, username: str, password: str, chats: dict):
        self.username = username
        self.password = password
        self.chats = chats

    def signin(self, network):
        return network.send([self, "signin", -1])

    def login(self, network):
        return network.send([self, "login", -1])

    def createChat(self, chatName: str, chatCode: str, network):
        if chatName != "" and chatCode != "":
            return network.send([self, "create", -1, chatName, chatCode])

    def joinChat(self, chatId: str, chatCode: str, network):
        if chatId != "" and chatCode != "":
            return network.send([self, "join", chatId, chatCode])

    def getChat(self, chatId: str, network):
        if chatId in self.chats:
            return network.send([self, "get", chatId])

    def sendMessage(self, message: str, chatId: str, network):
        if message != "" and chatId in self.chats:
            return network.send([self, "add", chatId, message])

    def quitChat(self, chatId: str, network):
        if chatId != "":
            return network.send([self, "quit", chatId])
