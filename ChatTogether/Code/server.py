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
IdsFile = open("Ids.txt", "r")
chatsId = IdsFile.readlines()
IdsFile.close()
Ids = []
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
    userId = ''.join(random.choice(letters) for i in range(6))
    return userId
def assembleClass(dictClass: dict):
    return Chat(dictClass["id"],dictClass["name"],dictClass["code"],dictClass["users"], dictClass["messages"])

def assembleUserClass(dictClass: dict):
    return User(dictClass["username"], dictClass["id"], dictClass["chats"])

def updateUsers(user: User):
    global users
    with open("users.json", "r") as usersFile:
        users = json.load(usersFile)
    users[user.id] = user.__dict__
    with open("users.json", "w") as usersFile:
        json.dump(users, usersFile)
def updateChats(chat: Chat):
    global chats
    with open("chats.json", "r") as chatsFile:
        chats = json.load(chatsFile)
    chats[chat.id] = chat.__dict__
    with open("chats.json", "w") as chatsFile:
        json.dump(chats, chatsFile)
def updateIds(id):
    if id not in Ids:
        with open("Ids.txt", "a") as IdsFile:
            IdsFile.write(id + "\n")
        return True
    else:
        return False

def threaded_client(conn):
    global users
    global chats
    global Ids
    userId = get_random_id()
    while userId in Ids:
        userId = get_random_id()
    conn.send(userId.encode())
    reply = []
    reply: list
    while True:
        # try:
            reply = []
            data = pickle.loads(conn.recv(4096))
            if data == None:
                break
            user = data[0]
            user : User
            chatId = data[2]
            isChat = False
            if user.id != userId and user.id in users and user.username == users[user.id]["username"]:
                user = assembleUserClass(users[user.id])
            else:
                if updateIds(userId):
                    Ids.append(userId)
                updateUsers(user)
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
                    reply = chat.getChat(user.id)
                elif data[1] == "add":
                    chat.addMessage(user.id, user.username, data[3])
                    reply = chat.getChat(user.id)   
                elif data[1] == "join":
                    chat.addUser(user.id, data[2], data[3])
                    reply = chat.getChat(user.id)
                elif data[1] == "quit":
                    user.removeChat(chat.id)
                    chat.removeUser(user.id)
                    reply.append("You has been remove correctly")

                chats[chatId] = chat.__dict__
                with open("chats.json", "w") as chatsFile:
                    json.dump(chats, chatsFile)
                reply.append(user)
                conn.send(pickle.dumps(reply))
            elif chatId == -1:
                if data[1] == "create":
                    chatId = get_random_id()
                    while chatId in Ids:
                        chatId = get_random_id()
                    if updateIds(chatId):
                        Ids.append(chatId)
                    chat = Chat(chatId, data[3], data[4], [user.id], "Let's groove chatting on chatTogether")
                    updateChats(chat)
                    user.addChat(chat.id, chat.name)
                    updateUsers(user)
                    reply = chat.getChat(user.id)
                    reply2 = [user, chat.id]
                    reply.extend(reply2)
                conn.send(pickle.dumps(reply))
            else:
                conn.send(pickle.dumps(["The typed wrong data", user]))
        # except:
        #     break
    print("Lost Connection")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))