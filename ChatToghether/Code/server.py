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
    global nChats
    global chats
    conn.send(str.encode(str(idCount)))
    reply = ""
    while True:
        # try:
            data = pickle.loads(conn.recv(4096))#de-code
            print(data)
            if data == None:
                break
            chatId = data[1]
            idCount += 1

            if chatId in chats:
                chat = chats[chatId]
                if data[2] == "get":
                    reply = chat.getChat(data[0])#get messages from file
                elif data[2] == "add":
                    chat.addMessage(data[3], data[4], data[0])#add the message
                
                reply = chat.getChat(data[0])#update the chat
                print(chats)
                print(chat.users)
                conn.send(pickle.dumps(reply))#en-code the chat and send it
            
            elif chatId == -1:
                print(chats)
                if data[2] == "create":
                    nChats += 1
                    chats[nChats] = Chat(nChats, data[4], data[3], data[0], data[5]) # create a new chat
                    reply = chats[nChats].getChat(nChats)

                elif data[2] == "join":
                    reply = chat.addUser(data[0], data[3], data[4], data[5])#add user to chat

                print(chats)
                conn.send(pickle.dumps(reply))
            else:
                break
        # except:
        #     break
    print(chats)
    print("Lost Connection")
    conn.close()

while True:
    conn, addr = s.accept()#tries to accept connection and adress for chat
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,1))