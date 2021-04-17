class User:
    def __init__(self, username, password, chats: dict):
        if username != "" and len(password) >= 8:
            self.username = username
            self.password = password
            self.chats = chats
        else:
            return None

    def addChat(self, chatId, chatName):
        if not chatId in self.chats:
            self.chats[chatId] = chatName
    
    def removeChat(self, chatId):
        if chatId in self.chats:
            del self.chats[chatId]