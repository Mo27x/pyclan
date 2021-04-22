class User:
    def __init__(self, username, password):#Constructor
        self.username = username
        self.password = password
        self.nChats = 0
        self.chats = {}
        self.id = -1

    def addChat(self, chatId, chatName):
        if not chatId in self.chats:
            self.chats[chatId] = chatName