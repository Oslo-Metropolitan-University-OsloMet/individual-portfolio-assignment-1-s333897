
from socket import *
from chatrecord import ChatRecord
from threading import Thread
from time import ctime


HOST = gethostname()
PORT = 5000
ADDRESS = (HOST, PORT)
BUFFSIZE = 1024

record = ChatRecord()
server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)


class ClientHandler(Thread):

    def __init__(self, client, record):
        Thread.__init__(self)
       # self._name = None
        self._client = client
        self._record = record

    def run(self):
        self._client.send(bytes("Welcome to the chat room!", "utf-8"))
        self._name = self._client.recv(BUFFSIZE)
        self._client.send(bytes(self._record, "utf-8"))
        while True:
            message = self._client.recv(BUFFSIZE)
            if not message:
                print("Client disconnencted")
                self._client.close()
                break
            else:
                message = self._name + ' ' + \
                    ctime() + '\n' + message
                self._record.add(message)
                self._client.send(bytes(self._record, "utf-8"))


while True:
    print(f"Waiting for connection ...")
    client, address = server.accept()
    print(f"... connected from: ", address)
    handler = ClientHandler(client, record)
    handler.start()

#Sources:
# Alzerqawee A. N. J. (2022), Lecture 10.pptx, OsloMet



