import speech
import random.randint

def random_range(index1,index2):
    number=random.randint(int(index1),int(index2))
    return number

def flip_coin():
    coin=random.choice([True,False])
    if coin:
        return "head"
    else:
        return "tail"    

"""
Basic setup of a function

def function(intent):
    speech.speak(intent + data)

where intent is the bot response to a given command
and the data is the task you got in the function

"""