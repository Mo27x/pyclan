class Chat:
<<<<<<< HEAD
    def __init__(self, id, name, code, users, messages: list):
        if id != "" and name != "" and code != "":
            self.id = id
            self.name = name
            self.code = code
            self.users = users
            self.messages = messages
        else:
            return None

    def addMessage(self, username, message):
        if username in self.users:
            self.messages.append((str(username) + ": " + str(message)))
            return True

    def getChat(self, username):
        if username in self.users:
            return self.messages

    def addUser(self, username, id, code):
        if self.code == code and self.id == id and username not in self.users:
            self.users.append(username)
            return True
        else:
            return False
    
    def removeUser(self, username):
        if username in self.users:
            self.users.remove(username)
    
    def getUsers(self, username):
        if username in self.users:
            return self.users
=======
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
>>>>>>> parent of c05a3bd (Upgraded)
