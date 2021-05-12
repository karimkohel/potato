#from speech import speak, takeCommand
from server.functions import playMusic
import webbrowser
import urllib
import re


def googleSearch(chatObj = None):
    if chatObj:
        search = chatObj[0].toPlainText()
        chatObj[1].append(f"potato: " + "here you go")
    else:
        pass
        # search = takeCommand()
        # speak("here you go")

    URl = "https://www.google.com/search?q=" + search
    webbrowser.open(URl)

# def youtubeSearch():
#     search = server.getMessage(client)
#     youtubeUrl = ("https://www.youtube.com/results?search_query=")
#     server.sendMessage(client, response)
#     webbrowser.open(youtubeUrl + search)
def playMusic(chatObj = None ):
    
    if chatObj:
        songName = chatObj[0].toPlainText()
        chatObj[1].append(f"potato: " + "On it")
    else:
        pass    

    searchLink = 'https://www.youtube.com/results?search_query={}'.format(songName.replace(" ", "+"))
    htmlPage = urllib.request.urlopen(searchLink)
    video_ids = re.findall(r"watch\?v=(\S{11})", htmlPage.read().decode())
    videoLink = "https://www.youtube.com/watch?v=" + video_ids[0]
    webbrowser.open(videoLink, new=2)
    
        
    
   


mappings = {
    "2" : googleSearch,
    "3" : youtubeSearch,
    "4":  playMusic
}