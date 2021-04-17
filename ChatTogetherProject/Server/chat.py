class Chat:
    def __init__(self, id, name, code, users: list, messages):
        self.id = id
        self.users = users
        self.name = name
        self.code = code
        self.messages = messages

    def addMessage(self, userId, username, message):
        if userId in self.users:
            self.messages = self.messages + ("\n" + str(username) + ": " + str(message))

    def getChat(self, userId):
        if userId in self.users:
            return [self.messages]
        else:
            return ["You did not joined this chat"]

    def addUser(self, userId, id, code):
        if self.code == code and self.id == id:
            self.users.append(userId)
    
    def removeUser(self, userId):
        if userId in self.users:
            self.users.remove(userId)