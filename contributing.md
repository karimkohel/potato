# Contributing to Potato
Before getting into any of the contrib title you should run the app localy using a local test server and client server

#### steps for opening a successfull pull request
1. fork the repo
2. work on whatever part you see fit
3. commit regularly
4. fetch regularly
5. open pull request

## Setup

- clone the repo 
	- `git clone https://github.com/karimkohel/potato.git`
- start a new python env
- install all dependencies:
	- `pip install -r requirements.txt`
- to work on the server you should
	- change the socket ip addres from remot server to local server in client/voicewindow.py and client/chatwindow.py
	- start the server from server/server.py
- start the client app from client/potato.py

## What can you do right now
 - Add Intents in server/intents.json
