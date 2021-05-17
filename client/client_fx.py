#from speech import speak, takeCommand
import webbrowser
import urllib
import re
from pytube import YouTube
import os
import json
import docx

def loadSettings():
    try:
        with open("settings.json") as f:
            settings = json.load(f)
            return settings
    except Exception:
        settings = {'speech_speed': 170, 'voice_number': 0, 'music_folder': ''}
        with open('settings.json', 'w') as f:
                json.dump(settings, f)
        return settings

def googleSearch(response):
    webbrowser.open(response)

def youtubeSearch(response):
    webbrowser.open(response)

def downloadMusic(response): # handeling the pass but its done
    video = YouTube(response)
    audio = video.streams.last()
    musicPath = os.path.expanduser("~/Desktop")
    try:
        audio.download(musicPath)
    except Exception:
        pass

def startWordProject(response):
    docName = response
    doc = docx.Document()
    doc.add_paragraph(docName)
    fileName = os.path.expanduser("D:\AAST") + "\\" + docName + ".docx"
    doc.save(fileName)
    os.startfile(fileName)
   

mappings = {
    "2" : googleSearch,
    "3" : youtubeSearch,
    "4" : downloadMusic,
    "5" : startWordProject
}