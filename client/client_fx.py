#from speech import speak, takeCommand
import webbrowser
import urllib
import re


def googleSearch(response):
    webbrowser.open(response)

def youtubeSearch(response):
    webbrowser.open(response)

# def playMusic(chatObj=None):
    
#     if chatObj:
#         songName = chatObj[0].toPlainText()
#         chatObj[1].append(f"potato: " + "On it")
#     else:
#         pass    

#     searchLink = 'https://www.youtube.com/results?search_query={}'.format(songName.replace(" ", "+"))
#     htmlPage = urllib.request.urlopen(searchLink)
#     video_ids = re.findall(r"watch\?v=(\S{11})", htmlPage.read().decode())
#     videoLink = "https://www.youtube.com/watch?v=" + video_ids[0]
#     webbrowser.open(videoLink, new=2)
    

mappings = {
    "2" : googleSearch,
    "3" : youtubeSearch,
    # "4":  playMusic
}