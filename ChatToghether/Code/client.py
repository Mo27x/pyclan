from network import Network
from user import User

def sendMessage(userx, n):#send the messages to the chat
    message = input("Insert message(premere invio per aggiornare la chat): ")
    if message != "":
        chat = n.send([1,"add",message, userx])

def main():#User data
    network = Network()#connect User
    user = User(input("Insert your username: "), input("Insert your password: "))#Data from user
    user.id = int(network.getP())#get ID user
    print("You are user: ", user.id)

    while True:
        chat = network.send([1, "get"])#get specific chat (1 is for template) the fisrt argument incates the chat ID
        oldChat = ""
        if oldChat != chat:
            print(chat)
        oldChat = chat
        sendMessage(user, network)
main()