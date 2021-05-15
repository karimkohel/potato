#from speech import speak, takeCommand
import webbrowser
import urllib
import re


def googleSearch(response):
    webbrowser.open(response)

def youtubeSearch(response):
    webbrowser.open(response)
    

mappings = {
    "2" : googleSearch,
    "3" : youtubeSearch,
    # "4":  playMusic
}