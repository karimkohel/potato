#from speech import speak, takeCommand
import webbrowser
import urllib
import re
from pytube import YouTube
import os
import json

try:
    with open("settings.json") as f:
        settings = json.load(f)
except Exception:
    settings = {'speech_speed': 170, 'voice_number': 0, 'music_folder': ''}
    with open('settings.json', 'w') as f:
            json.dump(settings, f)


def googleSearch(response):
    webbrowser.open(response)

def youtubeSearch(response):
    webbrowser.open(response)

def downloadMusic(response): # handeling the pass but its done
    video = YouTube(response)
    print(response)
    audio = video.streams.last()
    musicPath = os.path.expanduser("D:\IMages\RED")
    audio.download(musicPath)
    



mappings = {
    "2" : googleSearch,
    "3" : youtubeSearch,
    "4" : downloadMusic
}