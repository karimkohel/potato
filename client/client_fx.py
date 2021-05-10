from speech import speak, takeCommand


def googleSearch(typingbox = None):
    if typingbox:
        search = typingbox.toPlainText()
    else:
        search = takeCommand()
    URl = ("https://www.google.com/search?q=")
    webbrowser.open(URl + search)

def youtubeSearch():
    search = server.getMessage(client)
    youtubeUrl = ("https://www.youtube.com/results?search_query=")
    server.sendMessage(client, response)
    webbrowser.open(youtubeUrl + search)













mappings = {
    "2" : googleSearch,
    "3" : youtubeSearch
}