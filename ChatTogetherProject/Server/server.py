import socket
from _thread import *
import pickle
import json
import string
import random
from chat import Chat
from user import User

server = "192.168.1.27"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
usernameFile = open("usernames.txt", "r")
usernames = usernameFile.readlines()
usernameFile.close()
chatsIdFile = open("chatsId.txt", "r")
chatsId = chatsIdFile.readlines()
chatsIdFile.close()
chats = {}
with open("chats.json", "r") as chatsFile:
    chats = json.load(chatsFile)
users = {}
with open("users.json", "r") as usersFile:
    users = json.load(usersFile)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for a connection, Server Started")


def get_random_id():
    letters = string.ascii_lowercase
    Id = ''.join(random.choice(letters) for i in range(6))
    return Id
def assembleClass(dictClass: dict):
    return Chat(dictClass["id"],dictClass["name"],dictClass["code"],dictClass["users"], dictClass["messages"])

def assembleUserClass(dictClass: dict):
    return User(dictClass["username"], dictClass["password"], dictClass["chats"])

def updateUsers(user: User):
    global users
    with open("users.json", "r") as usersFile:
        users = json.load(usersFile)
    users[user.username] = user.__dict__
    with open("users.json", "w") as usersFile:
        json.dump(users, usersFile)
def updateChats(chat: Chat):
    global chats
    with open("chats.json", "r") as chatsFile:
        chats = json.load(chatsFile)
    chats[chat.id] = chat.__dict__
    with open("chats.json", "w") as chatsFile:
        json.dump(chats, chatsFile)
def updateUsernames(username):
    if username not in usernames:
        with open("usernames.txt", "a") as usernameFile:
            usernameFile.write(username + "\n")
        return True
    else:
        return False
def updateChatsId(chatId):
    if chatId not in chatsId:
        with open("chatsId.txt", "a") as chatsIdFile:
            chatsIdFile.write(chatId + "\n")
        return True
    else:
        return False

def getChatUsers(chat: Chat):
    chatUsers = []
    for username in chat.users:
        chatUsers.append(users[username]["username"])
    return chatUsers

def threaded_client(conn):
    global users
    global chats
    global usernames
    reply = []
    user = None
    logged = False
    while True:
        try:
            reply = []
            data = pickle.loads(conn.recv(4096))
            if data == None:
                break
            if not logged:
                user = data[0]
            chatId = data[2]
            isChat = False
            for idChat in chats:
                if idChat == chatId:
                    isChat = True
                    chat = chats[idChat]
                    break
            if isChat:
                chat = assembleClass(chats[chatId])
                with open("chats.json", "r") as chatsFile:
                    chats = json.load(chatsFile)
                if data[1] == "get":
                    reply.append(chat.getChat(user.username))
                elif data[1] == "add":
                    chat.addMessage(user.username, user.username, data[3])
                    reply.append(chat.getChat(user.username))
                elif data[1] == "join":
                    if chat.addUser(user.username, data[2], data[3]):
                        user.addChat(chat.id, chat.name)
                        reply = chat.getChat(user.username)
                    else:
                        reply = ["Id or code is wrong"]
                elif data[1] == "quit":
                    user.removeChat(chat.id)
                    chat.removeUser(user.username)
                    reply.append("You have been remove correctly")
                chats[chatId] = chat.__dict__
                with open("chats.json", "w") as chatsFile:
                    json.dump(chats, chatsFile)
                reply.append(user)
                if data[1] == "get" or data[1] == "add" or data[1] == "join":
                    if chat.getUsers(user.username) != None:
                        reply.append(chat.getUsers(user.username))
                    else:
                        reply.append(False)
                conn.send(pickle.dumps(reply))
            elif chatId == -1:
                if data[1] == "create":
                    chatId = get_random_id()
                    while chatId in usernames:
                        chatId = get_random_id()
                    if updateChatsId(chatId):
                        usernames.append(chatId)
                    chat = Chat(chatId, data[3], data[4], [user.username], ["Let's groove chatting on chatTogether"])
                    updateChats(chat)
                    user.addChat(chat.id, chat.name)
                    updateUsers(user)
                    reply.append(chat.getChat(user.username))
                    reply2 = [user, getChatUsers(chat), chat.id]
                    reply.extend(reply2)
                elif data[1] == "login":
                    if user.username in users:
                        if user.username == users[user.username]["username"] and user.password == users[user.username]["password"]:
                            user = assembleUserClass(users[user.username])
                            logged = True
                            reply = ["Welcome back to chat together", user, logged]
                    else:
                        reply = ["Username or password is wrong", user, logged]
                elif data[1] == "signin":
                    if updateUsernames(user.username) == False:
                        reply = ["The username you entered still exists", user, logged]
                    else:
                        usernames.append(user.username)
                        updateUsers(user)
                        logged = True
                        reply = ["Welcome to chat together", user, logged]
                conn.send(pickle.dumps(reply))
            else:
                conn.send(pickle.dumps(["You typed wrong data", user]))
        except:
            break
    print("Lost Connection")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))