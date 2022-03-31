# individual-portfolio-assignment-1-s333897
Creator: Thomas Kvam - s333897
Subject: DATA2410
Date: 31.03.2022

I first tried to make the bots using java, but quickly figured out i should learn python. I kept my java code and uploaded it to this repository, but it is the only code for the bots. The java code is able to create a chatroom where a user can type in questions and the bost will respond with a randomised answer. But this code is independent and does not reqiure a server. Therefor it can only be used offline.  

So without knowing any python i started these taskes. 

First of i created bots in python by using the instructions given in the assignment. From there i developed them a bit by making them able to have diffrent responses every time they got asked something. I gave each bot a list of things they liked and didn't, and from there they would give a random response out of 3 good responses, 3 bad responses or one response where if they were asked something that wasn't in the list they would give a default response. With the python code, the bots answred a premade question, but that could be changed to an input easily. 

After i created the bots i looked at lecture 10 on canvas. There i found a skeleton code for both a TCP server and a client. Using this i was able to create a server that a user could create a username and start chatting. I created a local server(server.py) that i could run using cmd, and i could launch another cmd that could connect to the server by using the client.py. The only issue here was to implement the bots and make them respond to the users inputs. 

As soon as i enter my username i get:

C:\Users\thoma>py -3.10 PycharmProjects/individual-portfolio-assignment-1-s333897/TCP/server.py
Waiting for connection ...
... connected from:  ('10.45.20.7', 51554)
Traceback (most recent call last):
  File "C:\Users\thoma\PycharmProjects\individual-portfolio-assignment-1-s333897\TCP\server.py", line 160, in <module>
    server.send(bytes("variable", 'utf-8'))
OSError: [WinError 10057] En forespørsel om å sende eller motta data ble forkastet fordi socketen ikke er tilkoblet og (ved sending på en datagramsocket som bruker et sendto-kall) ingen adresse var angitt
  
I have tried a lot of different fixes, but as soon as this error doesn't show up i get another error. This error came when i tried implementing the bots, but i apperently cant send some information between the client and the server, but i am able to send other information.   

Therefor this code is not entirely complete, but the bots work by themselves, and there server and the client works together without the bots. 


