import pickle
from network import Network

def main():
    run = True
    n = Network()
    user = int(n.getP())
    user = User(input("Insert your username: "), input("Insert your password: "))
    print("You are user: ", user)

    while run:
        try:
            chat = n.send("get")
            
        except:
            run = False
            print("Could't get chat")
            break