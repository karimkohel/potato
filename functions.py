import speech
import random

def random_range(intent):
    number = random.randint(0, 100)
    return number

def flip_coin(intent):
    coin = random.choice([True, False])
    if coin:
        return "head"
    else:
        return "tail"

def goodBye(intent):
    exit(0)

"""
Basic setup of a function

def function(intent):
    send(intent + data)

where intent is the bot response to a given command
and the data is the task you got in the function

"""

mappings = {

}