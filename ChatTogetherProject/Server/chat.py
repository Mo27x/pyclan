class Chat:
    def __init__(self, id: str, name: str, code: str, users: list, messages: list):
        if id != "" and name != "" and code != "":
            self.id = id
            self.name = name
            self.code = code
            self.users = users
            self.messages = messages
        else:
            return None

    def addMessage(self, username: str, message: str):
        if username in self.users:
            self.messages.append((str(username) + ": " + str(message)))
            return True

    def getChat(self, username: str):
        if username in self.users:
            return self.messages

    def addUser(self, username: str, id: str, code: str):
        if self.code == code and self.id == id and username not in self.users:
            self.users.append(username)
            return True
        else:
            return False
    
    def removeUser(self, username: str):
        if username in self.users:
            self.users.remove(username)
    
    def getUsers(self, username: str):
        if username in self.users:
            return self.users