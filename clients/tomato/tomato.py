#! /usr/bin/python

from speech import SpeechPatternRecognizer
from handler import Handler
from tomatoFx import mappings as functions


# use this link for gpio interupts
# https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/

spr = SpeechPatternRecognizer()
handler = Handler("http://192.168.2.10:5050/potato")


# while True:
    # spr.waitForWakeupCall("tomato")
while True:
    # for production
    # command = spr.listen()
    # for testing
    command = input("INPUT COMMAND: ")
    # get json response
    response = handler.getResponse(command)
    # speak the msg part of that json
    spr.speak(response['res'])
    # if json response has function code then execute said function
    if "functionCode" in response:
        functions[response["functionCode"]]()
    # if response has an exit flag then exit and wait for next wake up
    if "exit" in command:
        break

