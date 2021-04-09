
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.nChats = 0
        self.chats = {}
        self.id = 0
    
    def createChat(self):
        self.nChats += 1
    
    def joinChat(self, id):
        self.nChats += 1

    def getChat(self, id):
        return self.chats[id].getChat()