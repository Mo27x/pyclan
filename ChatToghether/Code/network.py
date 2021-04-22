import socket
import pickle

class Network:
    def __init__(self):#Constructor
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
<<<<<<< HEAD
        # self.server = "176.206.45.158"
        self.server = "192.168.1.27"
=======
        self.server = "176.206.56.226"
        server = "192.168.1.27"
>>>>>>> parent of 1fd383d (Now we can test)
        self.port = 5555
        self.addr = (self.server, self.port)
<<<<<<< HEAD:ChatTogether/Code/network.py
        self.connect()
=======
        self.p =  self.connect()

    def getP(self):#returns the user ID
        return self.p
>>>>>>> parent of f955452 (Ready to add GUI):ChatToghether/Code/network.py

    def connect(self):#connect user to server
        try:
            self.client.connect(self.addr)
<<<<<<< HEAD:ChatTogether/Code/network.py
=======
            return self.client.recv(2048)
>>>>>>> parent of f955452 (Ready to add GUI):ChatToghether/Code/network.py
        except:
            pass

    def send(self, data):#en-cript, send and recive data from server
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(4096))
        except socket.error as e:
            print(e)