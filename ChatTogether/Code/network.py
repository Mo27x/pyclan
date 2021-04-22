import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.server = "176.206.45.158"
        self.server = "192.168.1.27"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.connect()

    def connect(self):#connect user to server
        try:
            self.client.connect(self.addr)
        except:
            pass

    def send(self, data):#en-cript, send and recive data from server
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(4096))
        except socket.error as e:
            print(e)