import threading
from socket import *
from chatrecord import ChatRecord
from threading import Thread
from time import ctime
import random

#Sets the TCP server as a local server
HOST = gethostname()
PORT = 5000
ADDRESS = (HOST, PORT)
BUFFSIZE = 1024

record = ChatRecord()
server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

#Start of implementation of bots
def Andrew(a, b = None):
    action = a + "ing"
    bad_things = ["fighting", "complaining", "yelling", "screaming", "singing", "hugging", "running", "jogging", "climbing"]
    good_things = ["stealing", "eating", "sleeping", "working", "graffitiing", "studying"]

    good_responses = ["Sure, {} sounds good", "YES! Let's go {}!", "I'm down for {} if everyone else wants to."]
    bad_response = ["Have oyu lost your mind? {} is never the answer.", "Maybe {} is not the best usage of our time",
                    "Well, if we have nothing better to do."]

    randoGood = random.choice(good_responses)
    randoBad = random.choice(bad_response)

    if action in bad_things:
        return randoBad.format(action)
    elif action in good_things:
        return randoGood.format(action)
    return "I can't right now, sorry"

def Charlie(a, b = None):
    action = a + "ing"
    bad_things = ["fighting", "complaining", "yelling", "screaming", "climbing", "stealing", "graffitiing", "vandalising"]
    good_things = ["singing", "eating", "sleeping", "hugging", "working", "walking", "jogging"]

    good_responses = ["I wouldn't mind {} right now", "Alright, let's go {}", "I thought you would never ask."]
    bad_response = ["Seriously? {} again?", "Maybe today is not the day for {}", "Haven't we been {} a little much lately?"]

    randoGood = random.choice(good_responses)
    randoBad = random.choice(bad_response)

    if action in bad_things:
        return randoBad.format(action)
    elif action in good_things:
        return randoGood.format(action)
    return "Didn't we do that yesterday?"

def Sofia(a, b = None):
    alternatives = ["hiking", "singing", "swimming", "fighting", "crying", "playing", "jogging"]
    b = random.choice(alternatives)

    action = a + "ing"
    bad_things = ["fighting", "complaining", "yelling", "screaming", "stealing", "graffitiing",
                  "vandalising"]
    good_things = ["singing", "eating", "sleeping", "hugging", "working", "running", "jogging", "climbing", "running"]

    good_responses = ["YEAH! {} let's gooo!", "I'd always go {} with you ;) ", "Mmmm, ok :D {} sounds good!"]
    bad_response = [" {} again? What about {}? :O", "Hmmm, {}? I'd rather do some {}, what about you guys? :P ",
                    "Isn't {} bad? How about we just do some {} instead? :) "]

    randoGood = random.choice(good_responses)
    randoBad = random.choice(bad_response)

    if action in bad_things:
        return randoBad.format(action, b)
    elif action in good_things:
        return randoGood.format(action)
    res = "Yeah, {} is an option. Or we could do some {}.".format(action, b)
    return res


def Karen(a, b = None):
    action = a + "ing"
    bad_things = ["fighting", "complaining", "yelling", "screaming", "graffitiing", "stealing"]
    good_things = ["singing", "eating", "sleeping", "hugging", "working", "studying", "running"]

    good_responses = ["Come on man, {} is so lame", "Dude, just give up on your {} business. No one likes you", "Maybe, but i'd rather go {} with someone else."]
    bad_response = ["Yess! {} time!", "Cool, {} seems like something fun",
                    "You sure? I'm the master of {}, you will loose."]

    randoGood = random.choice(good_responses)
    randoBad = random.choice(bad_response)

    if action in bad_things:
        return randoBad.format(action)
    elif action in good_things:
        return randoGood.format(action)
    return "I would never do anything like that with you"
#End of implementation of bots



class ClientHandler(Thread):
#Code that tells wen a user has logged into the client
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
               # message = self._name + ' ' + \
               # ctime() + "\n" + message
               # self._record.add(message)
                self._client.send(bytes(self._record, "utf-8"))


while True:
#Code that constantly checks for connections and accepts any
    print(f"Waiting for connection ...")
    client, address = server.accept()
    print(f"... connected from: ", address)
    handler = ClientHandler(client, record)
    handler.start()

    some_msg = client.recv(BUFFSIZE).decode('utf-8')

    #Code that tries to make the bots respond to what ever the user types in the client
    action = random.choice(["work", "play", "cry", "walk", "eat", "fight", "sleep", "sing", "steal", "study", "graffiti", "snowboard", "run", "jogg", "climb", "hug", "chill", "watch a movie"])
    def check_activity(in_msg):

        return [x for x in action if
                (x in in_msg)]

    variable = ['{}'.format(Andrew(check_activity(some_msg))),
              '{}'.format(Charles(check_activity(some_msg))),
              '{}'.format(Sofia(check_activity(some_msg))),
              '{}'.format(Karen(check_activity(some_msg))),]

    var_str = ''.join(map(str, output))
    data.send(bytes(out_str, 'utf-8'))


#Sources:
# Alzerqawee A. N. J. (2022), Lecture 10.pptx, OsloMet. https://oslomet.instructure.com/courses/23100/pages/10-dot-03-dot-2022-lecture-10?module_item_id=409890



