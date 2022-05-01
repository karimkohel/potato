import random
from datetime import datetime
import requests
import re
import urllib
from bs4 import BeautifulSoup

def randomRange(response, server, client):
    try:
        #m7tag session 
        rangeInput = server.getMessage(client)
        number = random.randint(0, int(rangeInput))
        server.sendMessage(client, response + " " + str(number), 0)
    except ValueError:
        server.sendMessage(client, "Incorrect value you should enter only a number, ask again", 0)
        

def getDate(response):
    date = datetime.now()
    dateString = date.strftime(" %A ,%B %d, %Y ")
    return {"res" : response + dateString}

def getTime(response, server, client):
    time = datetime.now().time()
    time = time.strftime( "%H: %M: %S")
    server.sendMessage(client, response + " "+ time,0) 

def getWeather(response, server, client):
    api = 'http://api.openweathermap.org/data/2.5/weather?q=Cairo&appid=f1e62ab85ff8b2eca979678d57a6de2e&units=metric' 
    try:
        allData = requests.get(api).json()
        weather = allData['weather'][0]['description']
        temp = allData['main']['temp']
        server.sendMessage(client, response + " " + weather + ", with temperatures around " + str(int(temp)) + " degrees", 0)
    except TimeoutError:
        server.sendMessage(client,  "internet connection error occured, try again later", 0)
    except Exception:
        server.sendMessage(client,  "An error occured, try again later", 0)

        
def prayerTime(response, server, client):
    try:
    
        source = requests.get('https://egypt.timesprayer.com/en/prayer-times-in-cairo.html').text

        soup = BeautifulSoup(source, 'lxml')
        prayer_time = soup.find('div', id='countdown').text
        salah = soup.find('div', class_='info mobile').h3.text
        salah = salah.split(' ')
        server.sendMessage(client, response + " " +salah[2]+" in "+prayer_time, 0)
    except TimeoutError:
        server.sendMessage(client, "internet connection error occured, try again later", 0)


def goodBye(response, server, client):
    server.sendMessage(client, response, 9)

mappings = {
    "random" : randomRange,
    "weather" : getWeather,
    "time" : getTime,
    "date" : getDate,
    "prayer" : prayerTime,
    "goodbye" : goodBye
}