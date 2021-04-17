class User:
    def __init__(self, username, password, chats: dict):
        self.username = username
        self.password = password
        self.chats = chats
        self.id = ""

    def addChat(self, chatId, chatName):
        if not chatId in self.chats:
            self.chats[chatId] = chatName
    
    def removeChat(self, chatId):
        if chatId in self.chats:
            del self.chats[chatId]