class User:
    def __init__(self, username, userId, chats: dict):
        self.username = username
        self.id = userId
        self.chats = chats

    def addChat(self, chatId, chatName):
        if not chatId in self.chats:
            self.chats[chatId] = chatName
    
    def removeChat(self, chatId):
        if chatId in self.chats:
            del self.chats[chatId]