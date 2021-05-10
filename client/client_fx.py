from speech import speak, takeCommand
import webbrowser


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

def youtubeSearch():
    search = server.getMessage(client)
    youtubeUrl = ("https://www.youtube.com/results?search_query=")
    server.sendMessage(client, response)
    webbrowser.open(youtubeUrl + search)



mappings = {
    "2" : googleSearch,
    "3" : youtubeSearch
}