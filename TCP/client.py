from socket import *
import threading

#Connects to a locla TCP server
HOST = gethostname()
PORT = 5000
ADDRESS = (HOST, PORT)
BUFFSIZE = 1024

#Connects to the server and gives a prompt to create a username
server = socket(AF_INET, SOCK_STREAM)
server.connect(ADDRESS)
print(server.recv(BUFFSIZE))
name = input('Enter your name: ')
#Sends the information to the server side
server.send(bytes(name, "utf-8"))

def write():
#Takes what the user types in the client and puts the username behind it
    while True:
        message = f'{name}: {input("")}'
        server.send(bytes(name, message))
        #Sends what the user types to the server side
        some_msg = client.recv(BUFFSIZE).decode('utf-8')

def receive():
#Code that connects the user to the server
    while True:
        record = server.recv(BUFFSIZE)
        #recieves messages from the server, aka from the bots
        if not record:
            #If there is an error, the user disconnects form the server
            print(f"Server disconnected")
            break
        print(record)
        #Gives the user ability to awnser the bots
        message = input('> ')
        if not message:
            #If there is an error, the user disconnects form the server
            print(f"Server disconnected")
            break
        #Sends the awnser back to the server
        server.send(bytes(message + '\n', "utf-8"))
    server.close()

receive()
write()


#Sources:
# Alzerqawee A. N. J. (2022), Lecture 10.pptx, OsloMet, downloaded from: https://oslomet.instructure.com/courses/23100/pages/10-dot-03-dot-2022-lecture-10?module_item_id=409890