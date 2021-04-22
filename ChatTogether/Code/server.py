import socket
from _thread import *
import pickle
import json
import string
import random
from chat import Chat
from user import User
import time

server = "192.168.1.2"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
usernames = []
with open("usernames.txt", "r") as usernamesFile:
    usernames = usernamesFile.readlines()
chatsId = []
with open("chatsId.txt", "r") as chatsIdFile:
    chatsId = chatsIdFile.readlines()
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
<<<<<<< HEAD:ChatTogetherProject/Server/server.py
    return User(dictClass["username"], dictClass["password"], dictClass["chats"])
=======
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
>>>>>>> parent of c05a3bd (Upgraded):ChatTogether/Code/server.py

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
                if data[1] == "get":
                    reply.append(chat.getChat(user.username))
                elif data[1] == "add":
                    chat.addMessage(user.username, data[3])
                    reply.append(chat.getChat(user.username))
                elif data[1] == "join":
                    if chat.addUser(user.username, data[2], data[3]):
                        user.addChat(chat.id, chat.name)
                        reply = [chat.getChat(user.username)]
                    else:
                        reply = ["Id or code is wrong"]
                elif data[1] == "quit":
                    user.removeChat(chat.id)
<<<<<<< HEAD:ChatTogetherProject/Server/server.py
                    chat.removeUser(user.username)
                    reply.append("You have been remove correctly")
                chats[chat.id] = chat.__dict__
                reply.append(user)
                if data[1] == "get" or data[1] == "add" or data[1] == "join":
                    if chat.getUsers(user.username) != None:
                        reply.append(chat.getUsers(user.username))
                    else:
                        reply.append(False)
=======
                    chat.removeUser(user.id)
                    reply.append("You has been remove correctly")

                chats[chatId] = chat.__dict__
                with open("chats.json", "w") as chatsFile:
                    json.dump(chats, chatsFile)
                reply.append(user)
>>>>>>> parent of c05a3bd (Upgraded):ChatTogether/Code/server.py
                conn.send(pickle.dumps(reply))
            elif chatId == -1:
                if data[1] == "create":
                    chatId = get_random_id()
                    while chatId in chatsId:
                        chatId = get_random_id()
                    chat = Chat(chatId, data[3], data[4], [user.username], ["Let's groove chatting on chatTogether"])
                    chats[chat.id] = chat.__dict__
                    user.addChat(chat.id, chat.name)
<<<<<<< HEAD:ChatTogetherProject/Server/server.py
                    chatsId.append(chat.id)
                    reply.append(chat.getChat(user.username))
                    reply2 = [user, chat.getUsers(user.username), chat.id]
=======
                    updateUsers(user)
                    reply = chat.getChat(user.id)
                    reply2 = [user, chat.id]
>>>>>>> parent of c05a3bd (Upgraded):ChatTogether/Code/server.py
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
                    if user.username in usernames:
                        reply = ["The username you entered still exists", user, logged]
                    else:
                        users[user.username] = user.__dict__
                        usernames.append(user.username)
                        logged = True
                        reply = ["Welcome to chat together", user, logged]
                conn.send(pickle.dumps(reply))
            else:
                conn.send(pickle.dumps(["You typed wrong data", user]))
        except:
            break
    print("Lost Connection")
    conn.close()

def accept_connections():
    while True:
        conn, addr = s.accept()
        print("Connected to: ", addr)
        start_new_thread(threaded_client, (conn,))

while True:
    try:
        start_new_thread(accept_connections, ())
        time.sleep(1)
    except KeyboardInterrupt:
        print("Program termianted")
        with open("usernames.txt", "w") as usernamesFile:
            usernamesFile.writelines(usernames)
        with open("chatsId.txt", "w") as chatsIdFile:
            chatsIdFile.writelines(chatsId)
        with open("chats.json", "w") as chatsFile:
            json.dump(chats,chatsFile)
        with open("users.json", "w") as usersFile:
            json.dump(users,usersFile)
        exit()