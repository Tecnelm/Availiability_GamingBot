# coding: utf-8
import socket
import threading

import yaml
import threading
import win32api

class Client(threading.Thread):
    def __init__(self):
        super(Client, self).__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        with open("./config.yml", "r") as config:
            try:
                self.config = yaml.safe_load(config)
            except yaml.YAMLError as exc:
                print("ERROR: Load Config File")
        self.socket.connect((self.config["Server"]["ip"],self.config["Server"]["port"]))

    def run(self):
        while 1:
            r = self.socket.recv(999999).decode()
            print("receive message : "+r)
            if (r == self.config["Discord"]["response"]["ask"]["commande"]):
                self.socket.send(self.getIdleTime().encode())
                print("send iddle time")

    def getIdleTime(self):
        return str(int((win32api.GetTickCount() - win32api.GetLastInputInfo()) / (1000.0*60)))

client = Client()
client.run()
