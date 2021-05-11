import random
import webbrowser
from datetime import datetime
import requests


def randomRange(response, server, client):
    server.sendMessage(client, "till what number should i guess")
    range1 = server.getMessage(client)
    number = random.randint(0, int(range1))
    server.sendMessage(client, response + " " + str(number), 0)

def googleSearch(response,server,client):
    server.sendMessage(client, response, 2)

def youtubeSearch(response,server,client):
    search = server.getMessage(client)
    youtubeUrl = ("https://www.youtube.com/results?search_query=")
    server.sendMessage(client, response)
    webbrowser.open(youtubeUrl + search)

def getDate(response,server, client):
    date = datetime.now()
    dateString = date.strftime(" %A ,%B %d, %Y ")
    server.sendMessage(client, response + " "+ dateString, 0)
    
def getWeather(response, server, client):
    # Need to put Location instead of cairo
    api = 'http://api.openweathermap.org/data/2.5/weather?q=Cairo&appid=f1e62ab85ff8b2eca979678d57a6de2e&units=metric' 
    try:
        allData = requests.get(api).json()
        weather = allData['weather'][0]['description']
        temp = allData['main']['temp']
        server.sendMessage(client, response + " " + weather + ", with temperatures around " + str(int(temp)) + " degrees", 0)

    except TimeoutError:
        server.sendMessage(client, response + " internet connection error occured, try again later", 0)
    except Exception:
        server.sendMessage(client, response  + " An error occured, try again later", 0)

mappings = {
    "random" : randomRange,
    "weather" : getWeather,
    "search" : googleSearch
}
