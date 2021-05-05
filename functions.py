import speech
import random

def randomRange(intent, server, client):
    range1 = server.sendMessage(client, "what is range")
    number = random.randint(int(range1))
    print(intent + " " + str(number))
    server.sendMessage(client, intent + " " + str(number))
    client.close()

    

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