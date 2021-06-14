# Potato
A  beuatiful AI assistant to help students with their uni life that is centralized on a server somewhere

## What can it do
Potato is mainly an assistant that would help you use your computer with voice command with functionality as but not limited to:

 - opening up search windows with your default browser
 - play or download whatever music you desire
 - answer random questions like what time is it or when is the next prayer
 - chat with you about random topics 
 - control your screen brightness
 - open up an new word document for your next report
 - roll a die or toss a coin
 - take a screen shot of your computer

## How to use potato
Potato has 2 main windows, the voice and text chat windows and it will have full functionality in both modes.

#### Text with potato
to text with potato you have to choose the text page and you can start texting right away.

#### Voice chat with potato
to use voice chat just open the voice window and minimize potato so that it is listining in the background and waiting for you to start chatting by saying `hey potato`.

you can start chatting with potato while it is in the background without clicking on it, asking what you need and then sending it away is as easy as calling it with `go away` so it goes back to the background awaiting your next call.

to close potato completely using voice command you can use keyword `exit` in any context and potato will exit entirely.


### How to start developement
 - clone the repo by opening gitbash in the desired folder and running the command 
 
`git clone https://github.com/karimkohel/potato.git`

 - check the projects section of the repo on github to see where we are on development
 - check your conda env is working and install libraries in said env with `pip install -r requirements.txt`
 - after editing a file you should always commit when you finish a specific edit

`git add .`

`git commit -m "your msg"`

 - remember to push after a work session for other contributers to work on the updated version

`git push`

 - and when starting to work again on the local repo always pull in changes that other people did while you were away with

`git pull`

#### server script
the server script will host the main logic and body of the project with the sockets working to accept and send data to clients all over

#### client app
client app will use a gui and a text to speach engine/speach recognition engine to recieve and output the speach to users that is fetched from server script over a socket


### ERROR CODES:

|Code |Def  |
| --- | --- |
|0CVXXX|Client Voice Error |
|0CCXXX|Client Chat Error |
|0CSXXX|Client Socket Error|
|0SIXXX|Server Intents Error|
|0SFXXX|Server Function Error|
|0SSXXX|Server Socket Error|