import speech
import random

def randomRange(intent, server, client):
    server.sendMessage(client, "till what number should i guess")
    range1 = server.getMessage(client)
    number = random.randint(0, int(range1))
    server.sendMessage(client, intent + " " + str(number))
    # client.close()

    

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