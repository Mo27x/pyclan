class Chat:
    def __init__(self, id, name, code, users, messages: list):
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
            self.messages.append((str(username) + ": " + str(message)))
            return True

    def getChat(self, username):
        if username in self.users:
            return self.messages

    def addUser(self, username, id, code):
        if self.code == code and self.id == id and username not in self.users:
            self.users.append(username)
            return True
    
    def removeUser(self, username):
        if username in self.users:
            self.users.remove(username)
    
    def getUsers(self, username):
        if username in self.users:
            return self.users