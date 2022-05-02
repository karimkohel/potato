import random
from datetime import datetime
import requests
from bs4 import BeautifulSoup

def randomRange(intent):
    try:
        #m7tag session 
        rangeInput = server.getMessage(client)
        number = random.randint(0, int(rangeInput))
        server.sendMessage(client, intent + " " + str(number), 0)
    except ValueError:
        server.sendMessage(client, "Incorrect value you should enter only a number, ask again", 0)
        

def getDate(intent):
    date = datetime.now()
    dateString = date.strftime(" %A ,%B %d, %Y ")
    return {"res" : intent + dateString}

def getTime(intent, server, client):
    time = datetime.now().time()
    time = time.strftime( "%H: %M: %S")
    server.sendMessage(client, intent + " "+ time,0) 

def getWeather(intent, server, client):
    api = 'http://api.openweathermap.org/data/2.5/weather?q=Cairo&appid=f1e62ab85ff8b2eca979678d57a6de2e&units=metric' 
    try:
        allData = requests.get(api).json()
        weather = allData['weather'][0]['description']
        temp = allData['main']['temp']
        server.sendMessage(client, intent + " " + weather + ", with temperatures around " + str(int(temp)) + " degrees", 0)
    except TimeoutError:
        server.sendMessage(client,  "internet connection error occured, try again later", 0)
    except Exception:
        server.sendMessage(client,  "An error occured, try again later", 0)

        
def prayerTime(intent):
    try:
    
        source = requests.get('https://egypt.timesprayer.com/en/prayer-times-in-cairo.html').text

        soup = BeautifulSoup(source, 'lxml')
        prayer_time = soup.find('div', id='countdown').text
        salah = soup.find('div', class_='info mobile').h3.text
        salah = salah.split(' ')
        return {"res": intent + " " +salah[2]+" in "+prayer_time}
    except TimeoutError:
        return {"res": "internet connection error occured, try again later"}


def goodBye(intent, server, client):
    server.sendMessage(client, intent, 9)

mappings = {
    "random" : randomRange,
    "weather" : getWeather,
    "time" : getTime,
    "date" : getDate,
    "prayer" : prayerTime,
    "goodbye" : goodBye
}