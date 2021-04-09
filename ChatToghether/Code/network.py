import socket
import pickle

class Network:
    def __init__(self):#Constructor
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.gethostbyname(socket.gethostname())
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p =  self.connect()

    def getP(self):#returns the user ID
        return self.p

    def connect(self):#connect user to server
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048)
        except:
            pass

    def send(self, data):#en-cript, send and recive data from server
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(4096))
        except socket.error as e:
            print(e)