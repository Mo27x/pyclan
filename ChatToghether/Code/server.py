import socket
from _thread import *
import pickle
from chat import Chat

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
nChats = 0
idCount = 0
chats[1] = Chat(1,"YYKM")

def threaded_client(conn, i):
    global idCount
    conn.send(str.encode(str(idCount)))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(4096))#de-code
            chatId = data[0]

            if chatId in chats:
                chat = chats[chatId]
                if not data:
                    break
                else:
                    if data[1] == "get":
                        reply = chat.getChat()#get messages from file
                    elif data[1] == "add":
                        chat.addMessage(data[2], data[3])#add the message
                    elif data[1] == "join":
                        chat.addUser(data[2], data[3])#add user to chat
                    
                    reply = chat.getChat()#update the chat
                    conn.send(pickle.dumps(reply))#en-code the chat and send it
            elif data[1] == "create":
                chats[nChats] = Chat(nChats)#create a new chat
                conn.send(pickle.dumps(chats[nChats].getChat()))
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