import random

def Adrew(a, b = None):
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


action1 = random.choice(["work", "play", "cry", "walk", "eat", "fight", "sleep", "sing", "steal", "study", "graffiti", "snowboard", "run", "jogg", "climb", "hug", "chill", "watch a movie"])
action2 = random.choice(["work", "play", "cry", "walk", "eat", "fight", "sleep", "sing", "steal", "study", "graffiti", "snowboard", "run", "jogg", "climb", "hug", "chill", "watch a movie"])
action3 = random.choice(["work", "play", "cry", "walk", "eat", "fight", "sleep", "sing", "steal", "study", "graffiti", "snowboard", "run", "jogg", "climb", "hug", "chill", "watch a movie"])

print("\nMe: Do you guys want to {}? ".format(action1))
print("Andrew: {}".format(Adrew(action1)))
print("Charlie: {}".format(Charlie(action1)))
print("Sofia: {}".format(Sofia(action1)))
print("Karen: {}".format(Karen(action1)))


print("\nMe: How about we try to {} today? ".format(action2))
print("Andrew: {}".format(Adrew(action2)))
print("Charlie: {}".format(Charlie(action2)))
print("Sofia: {}".format(Sofia(action2)))
print("Karen: {}".format(Karen(action2)))


print("\nMe: You guys still want to {}? Or is that off the table? ".format(action3))
print("Andrew: {}".format(Adrew(action3)))
print("Charlie: {}".format(Charlie(action3)))
print("Sofia: {}".format(Sofia(action3)))
print("Karen: {}".format(Karen(action3)))