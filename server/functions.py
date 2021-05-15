import random
import webbrowser
from datetime import datetime
import requests
import re
import urllib
from bs4 import BeautifulSoup

def randomRange(response, server, client): #done
    server.sendMessage(client, "till what number should i guess")
    range1 = server.getMessage(client)
    number = random.randint(0, int(range1))
    server.sendMessage(client, response + " " + str(number), 0)

def googleSearch(response,server,client): #done
    server.sendMessage(client, response, 1)
    searchTopic = server.getMessage(client)
    url = "https://www.google.com/search?q=" + searchTopic
    server.sendMessage(client, url, 2)


def getDate(response,server, client): #done
    date = datetime.now()
    dateString = date.strftime(" %A ,%B %d, %Y ")
    server.sendMessage(client, response + " "+ dateString, 0)

def getTime(response,server, client): #done
    time = datetime.now().time()
    time = time.strftime( "%H: %M: %S")
    server.sendMessage(client, response + " "+ time,0) 

def youtubeSearch(response,server,client): #done
    server.sendMessage(client, response, 1)
    try:
        youtubeTopic = server.getMessage(client)
        searchLink = 'https://www.youtube.com/results?search_query={}'.format(youtubeTopic.replace(" ", "+"))
        htmlPage = urllib.request.urlopen(searchLink)
        video_ids = re.findall(r"watch\?v=(\S{11})", htmlPage.read().decode())
        videoLink = "https://www.youtube.com/watch?v=" + video_ids[0]
        server.sendMessage(client, videoLink,3)
        
    except TimeoutError:
        server.sendMessage(client,"internet connection error occured, try again later",0)
   

def getWeather(response, server, client): #done
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

def prayerTime(response, server, client):
    """ Legacy function """
    try:
        source = requests.get('https://egypt.timesprayer.com/en/prayer-times-in-cairo.html').text
        soup = BeautifulSoup(source, 'lxml')
        prayer_time = soup.find('div',id='countdown').text
        salah = soup.find('div',class_='info mobile').h3.text
    except:
        try:
            source = requests.get('https://www.prayer-times.info/en/egypt/cairo/').text
            soup = BeautifulSoup(source, 'lxml')
            prayer_time = soup.find('div',id='next_pray').text
            salah = soup.find('div',id='next_pray').h3.text
        except:
            source = None
    if source == None:
        server.sendMessage(client, "sorry cannot find prayer time right now. Maybe try again later", 0)
    else:
        server.sendMessage(client, "sorry cannot find prayer time right now. Maybe try again later", 0)
        server.sendMessage(response + " " + prayer_time)

mappings = {
    "random" : randomRange,
    "weather" : getWeather,
    "search" : googleSearch,
    "youtube" : youtubeSearch,
    "time" : getTime,
    "date" : getDate,
    "prayer" : prayerTime
}
