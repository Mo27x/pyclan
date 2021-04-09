import pickle
from network import Network
from user import User

def sendMessage():
    chat = n.send([1,"add", input("Insert message"), userx])

def main():
    run = True
    n = Network()
    user = int(n.getP())
    userx = User(input("Insert your username: "), input("Insert your password: "))
    print("You are user: ", user)

    while run:
        chat = n.send([1, "get"])
        oldChat = chat
        sendMessage()
        if oldChat != chat:
            print(chat)
main()