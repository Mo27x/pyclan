class Chat:
    def __init__(self, id, name, code, users: list, messages):
        if id != "" and name != "" and code != "":
            self.id = id
            self.users = users
            self.name = name
            self.code = code
            self.messages = messages
        else:
            return None

    def addMessage(self, userId, username, message):
        if userId in self.users:
            self.messages = self.messages + ("\n" + str(username) + ": " + str(message))

    def getChat(self, username):
        if username in self.users:
            return [self.messages]
        else:
            return ["You did not joined this chat"]

    def addUser(self, username, id, code):
        if self.code == code and self.id == id and username not in self.users:
            self.users.append(username)
    
    def removeUser(self, username):
        if username in self.users:
            self.users.remove(username)