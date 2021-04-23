class User:
    def __init__(self, username:str, password:str, chats: dict):
        self.username = username
        self.password = password
        self.chats = chats

    def addChat(self, chatId: str, chatName: str):
        if not chatId in self.chats:
            self.chats[chatId] = chatName
    
    def removeChat(self, chatId: str):
        if chatId in self.chats:
            del self.chats[chatId]