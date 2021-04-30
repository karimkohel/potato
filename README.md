# potato
A  beuatiful AI assistant to help students with their uni life that is centralized on a server somewhere

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
