import threading
import time

class ClientThread(threading.Thread):
    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))
        print("Connexion de %s %s" % (self.ip, self.port, ))

    def ask(self,commande):
        self.clientsocket.send(commande.encode())
        r = self.clientsocket.recv(9999)
        return r.decode()

    