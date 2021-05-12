import random
import webbrowser
from datetime import datetime
import requests
import re
import urllib


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

def getTime(response,server, client):
    time = datetime.now()
    timeString = time.strftime( "%H: %M: %S")
    server.sendMessage(client, response + " "+ timeString, 0) 

def playMusic(response,server,client):
    
    songName = server.getMessage(client)
    try:
        searchLink = 'https://www.youtube.com/results?search_query={}'.format(songName.replace(" ", "+"))
        htmlPage = urllib.request.urlopen(searchLink)
        video_ids = re.findall(r"watch\?v=(\S{11})", htmlPage.read().decode())
        videoLink = "https://www.youtube.com/watch?v=" + video_ids[0]
        server.sendMessage(client, response,4)
        
    except TimeoutError:
        server.sendMessage(client,"internet connection error occured, try again later",0)
   
   

def getWeather(response, server, client):
    # Need to put Location instead of cairo
    api = 'http://api.openweathermap.org/data/2.5/weather?q=Cairo&appid=f1e62ab85ff8b2eca979678d57a6de2e&units=metric' 
    try:
        allData = requests.get(api).json()
        weather = allData['weather'][0]['description']
        temp = allData['main']['temp']
        server.sendMessage(client, response + " " + weather + ", with temperatures around " + str(int(temp)) + " degrees", 0)

    except TimeoutError:
        server.sendMessage(client,  " internet connection error occured, try again later", 0)
    except Exception:
        server.sendMessage(client,  " An error occured, try again later", 0)

mappings = {
    "random" : randomRange,
    "weather" : getWeather,
    "search" : googleSearch,
    "play " : playMusic
}
