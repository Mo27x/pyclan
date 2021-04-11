import socket
from _thread import *
import pickle
import json
from chat import Chat
from user import User

server = "192.168.1.27"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for a connection, Server Started")

chats = {}
users = {}
nChats = 0
idCount = 0

def threaded_client(conn, i):
    global idCount
    global users
    global nChats
    global chats
    conn.send(str.encode(str(idCount)))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(4096))#de-code
            if data == None:
                break
            # if data[0].id in users:
            #     idCount -= 1
            else:
                users[idCount] = data[0]
            user = data[0]
            chatId = int(data[2])

            if chatId in chats:
                chat = chats[chatId]
                if data[1] == "get":
                    reply = chat.getChat(user.id)#get messages from file
                elif data[1] == "add":
                    chat.addMessage(user.username, data[3], user.id)#add the message
                elif data[1] == "join":
                    chat.addUser(user.id, user.username, data[2], data[3])#add user to chat
                reply = chat.getChat(user.id)#update the chat
                conn.send(pickle.dumps(reply))#en-code the chat and send it
            
            elif chatId == -1:
                if data[1] == "create":
                    nChats += 1
                    chats[nChats] = Chat(nChats, data[3], user.username, user.id, data[4]) # create a new chat
                    # chatsFile = open("chats.json", "w")
                    # json.dump(chats, chatsFile)
                    # chatsFile.close()
                    reply = chats[nChats].getChat(user.id)
                conn.send(pickle.dumps(reply))
            else:
                break
        except:
            break
    print("Lost Connection")
    conn.close()

while True:
    conn, addr = s.accept()#tries to accept connection and adress for chat
    print("Connected to: ", addr)
    idCount += 1

    start_new_thread(threaded_client, (conn,1))