# Potato

A beuatiful AI assistant to help students with their uni life that is centralized on a server somewhere


## Badges

![GitHub top language](https://img.shields.io/github/languages/top/karimkohel/potato?style=flat-square)

![GitHub issues](https://img.shields.io/github/issues/karimkohel/potato?style=flat-square)

![GitHub Repo stars](https://img.shields.io/github/stars/karimkohel/potato?style=flat-square)
## Installation 

Just install using the installer in the [Latest Release](https://github.com/karimkohel/potato/releases),
 then find the executable in the main folder with the name **potato.exe**
## Demo

#### Main Window
- Potato has 2 main windows, the voice and text chat windows and it will have full functionality in both modes.
- You can acces both windows from the main window.
![Main window](https://raw.githubusercontent.com/karimkohel/potato/main/demo/main.PNG)

#### Chat Window
- Open the text window to chat normally as you would any chat application.
- Potato will chat with you casually or carry out the tasks you request.
![Chat window](https://raw.githubusercontent.com/karimkohel/potato/main/demo/chat.PNG)

#### Voice Window
- Open the voice window and minimize potato so that it is listining in the background and waiting for you to start chatting by saying **Hey potato**.
- You can start chatting with potato while it is in the background without clicking on it, asking what you need and then sending it away is as easy as calling it with **go away** so it goes back to the background awaiting your next call.
- To close potato completely using voice command you can use keyword **exit** in any context and potato will exit entirely.
![Chat window](https://raw.githubusercontent.com/karimkohel/potato/main/demo/voice.PNG)
## Tech Stack

##### **Client:** 
- PyQT5
- Pyttsx3
- Google speech recognition
- Pytube
- Docx
- PyautoGUI

##### **Server:**
- Tensforflow 2.0
- Keras
- NLTK
- Requests
- Threaded sockets
- Urllib3
- BeautifulSoup4
## Features and Functions

Potato is mainly an assistant that would help you use your computer with voice command with functionality as but not limited to:

 - opening up search windows with your default browser
 - play or download whatever music you desire
 - answer random questions like what time is it or when is the next prayer
 - chat with you about random topics 
 - control your screen brightness
 - open up an new word document for your next report
 - roll a die or toss a coin
 - take a screen shot of your computer
 - go in and out of focus in voice chat to help you with tasks without another IO method
## Contributing

Contributions are always welcome!

See [contributing.md](https://github.com/karimkohel/potato/blob/main/contributing.md) for ways to get started.

Please adhere to this project's `code of conduct`.
## Support

For general support [open an issue](https://github.com/karimkohel/potato/issues) describing your problem or feature request

- Be as detailed as possible in issue description
- include what error code you got if any

#### Error codes
|Code |Def  |
| --- | --- |
|0CVXXX|Client Voice Error |
|0CCXXX|Client Chat Error |
|0CSXXX|Client Socket Error|
|0SIXXX|Server Intents Error|
|0SFXXX|Server Function Error|
|0SSXXX|Server Socket Error|

## Authors

- [@karimkohel](https://www.github.com/karimkohel)
- [@NourhanElyamany](https://www.github.com/NourhanElyamany)
- [@Mohameosama](https://www.github.com/Mohameosama)
- [@omar9991](https://www.github.com/omar9991)