from socket import *
import threading

HOST = gethostname()
PORT = 5000
ADDRESS = (HOST, PORT)
BUFFSIZE = 1024

server = socket(AF_INET, SOCK_STREAM)
server.connect(ADDRESS)
print(server.recv(BUFFSIZE))
name = input('Enter your name: ')
server.send(bytes(name, "utf-8"))

def write():
    while True:
        message = f'{name}: {input("")}'
        server.send(bytes(name, message))
        some_msg = client.recv(BUFFSIZE).decode('utf-8')

def receive():
    while True:
        record = server.recv(BUFFSIZE)
        if not record:
            print(f"Server disconnected")
            break
        print(record)
        message = input('> ')
        if not message:
            print(f"Server disconnected")
            break
        server.send(bytes(message + '\n', "utf-8"))
    server.close()

receive()
write()


#Sources:
# Alzerqawee A. N. J. (2022), Lecture 10.pptx, OsloMet, downloaded from: https://oslomet.instructure.com/courses/23100/pages/10-dot-03-dot-2022-lecture-10?module_item_id=409890