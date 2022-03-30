from socket import *

HOST = gethostname()
PORT = 5000
ADDRESS = (HOST, PORT)
BUFFSIZE = 1024

server = socket(AF_INET, SOCK_STREAM)
server.connect(ADDRESS)
print(server.recv(BUFFSIZE))
name = input('Enter your name: ')
server.send(bytes(name, "utf-8"))

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
    server.send(message + '\n')
server.close()

#Sources:
# Alzerqawee A. N. J. (2022), Lecture 10.pptx, OsloMet, downloaded from: https://oslomet.instructure.com/courses/23100/pages/10-dot-03-dot-2022-lecture-10?module_item_id=409890