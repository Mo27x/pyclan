import socket
from _thread import *
import pickle

server = "192.168.1.27"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for a connection, Server Started")

connected = set()
chats = {}
idCount = 0

def threaded_client(conn):
    global idCount
    conn.send(str.encode(str(idCount)))
    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()
            chatId = data[0]

            if chatId in chats:
                chat = chats[chatId]

                if data[1] == "get":
                    reply = chat.getChat()
                elif data[1] == "add":
                    chat.addMessage(data[2], data[3])
                elif data[1] == "user":
                    chat.addUser(data[2], data[3])
                elif data[1] == "join":
                    chat.addUser(data[2], data[3])
                reply = chat.getChat()
                conn.sendall(pickle.dumps(reply))
            else:
                break
        except:
            break

    print("Lost Connection")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    idCount += 1

    start_new_thread(threaded_client, (conn, gameId))