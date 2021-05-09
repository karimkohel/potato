import speech
import random
import google
import webbrowser
from datetime import datetime

def randomRange(response, server, client):
    server.sendMessage(client, "till what number should i guess")
    range1 = server.getMessage(client)
    number = random.randint(0, int(range1))
    server.sendMessage(client, response + " " + str(number))
    # client.close()

def googleSearch(response,server,client):
    search=server.getMessage(client)
    URl=("https://www.google.com/search?q=")
    server.sendMessage(client, response)
    webbrowser.open(URl+search)

def youtubeSearch(response,server,client):
    search=server.getMessage(client)
    youtube_Url=("https://www.youtube.com/results?search_query=")
    server.sendMessage(client, response)
    webbrowser.open(youtube_Url+search)

def Time(response,server,client):
    server.getMessage(client)
    getTime=now.strftime("%H %M %p")
    server.sendMessage(client, response + " " + getTime)






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