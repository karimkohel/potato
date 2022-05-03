import random
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pytz

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

def getTime(intent):
    
    time_f = datetime.now(pytz.timezone('Africa/Cairo')).time()
    time = time_f.strftime( "%H: %M: %S")
    return {"res":intent + " "+ time} 

def getWeather(intent):
    api = 'http://api.openweathermap.org/data/2.5/weather?q=Cairo&appid=f1e62ab85ff8b2eca979678d57a6de2e&units=metric' 
    try:
        allData = requests.get(api).json()
        weather = allData['weather'][0]['description']
        temp = allData['main']['temp']
        return {"res": intent + " " + weather + ", with temperatures around " + str(int(temp)) + " degrees"}
        
    except TimeoutError:
        
        return {"res": "internet connection error occured, try again later"}
    except Exception:
        
        return {"res": intent+"An error occured, try again later"}

        
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


def goodBye(intent):
    return {"res": intent }

mappings = {
    "random" : randomRange,
    "weather" : getWeather,
    "time" : getTime,
    "date" : getDate,
    "prayer" : prayerTime,
    "goodbye" : goodBye
}