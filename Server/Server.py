import socket
import threading
from . import ClientThread
import yaml

class TCPServer (threading.Thread):
    def __init__(self):
        super(TCPServer, self).__init__()
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        with open("./config.yml", "r") as config:
            try:
                self.config = yaml.safe_load(config)["Server"]
            except yaml.YAMLError as exc:
                print("ERROR: Load Config File")

        self.server.bind((self.config["ip"],self.config["port"]))
        self.client=[]
        self.server.listen(2)

    def run(self):
        while 1:
            (client, (ip,port)) = self.server.accept()
            cli = ClientThread.ClientThread(ip,port,client)
            cli.daemon = True
            self.client.append(cli)
    def get_client(self):
        return self.client




