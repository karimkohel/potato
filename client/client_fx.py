import webbrowser
from pytube import YouTube
import os
import docx
from pyautogui import screenshot

if os.name != "posix" :
    import screen_brightness_control as sbc

def googleSearch(response):
    webbrowser.open(response)

def youtubeSearch(response):
    webbrowser.open(response)

def downloadMusic(response):
    video = YouTube(response)
    audio = video.streams.filter(only_audio=True).first()
    musicPath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    try:
        audio.download(musicPath)
    except Exception:
        pass

def startWordProject(response):
    docName = response
    doc = docx.Document()
    doc.add_paragraph(docName)
    fileName = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')+"\\"+ docName + ".docx"
    doc.save(fileName)
    os.startfile(fileName)

def screenShot(response):
    screenShot = screenshot()
    directory = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')+"\\"
    screenShot.save(directory + "screenshot.png")  
   
def higherbrightness(response):
    if os.name != "posix" :
        sbc.set_brightness('+25')

def lowerBrightness(response):
    if os.name != "posix" :
        sbc.set_brightness('-25')

mappings = {
    "2" : googleSearch,
    "3" : youtubeSearch,
    "4" : downloadMusic,
    "5" : startWordProject,
    "6" : screenShot,
    "7" : lowerBrightness,
    "8" : higherbrightness,
}