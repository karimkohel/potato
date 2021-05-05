import speech
import random

def randomRange(intent):
    number = random.randint(0, 100)
    print(intent + " " + str(number))
    

# def flipCoin(intent):
#     coin = random.choice([True, False])
#     if coin:
#         return "head"
#     else:
#         return "tail"

# def goodBye(intent):
#     exit(0)



mappings = {
    "random" : randomRange,
}