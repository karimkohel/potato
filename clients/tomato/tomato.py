#! /usr/bin/python

from speech import SpeechPatternRecognizer
from handler import Handler
from tomatoFx import tomato


# use this link for gpio interupts
# https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/

spr = SpeechPatternRecognizer()
handler = Handler("http://192.168.2.10:5050/potato")


# while True:
    # spr.waitForWakeupCall("tomato")

while True:
    # command = spr.listen()
    command = input("INPUT COMMAND: ")
    response = handler.getResponse(command)
    spr.speak(response['res'])
    if "functionCode" in response:
        functions[response["functionCode"]]()
    if "exit" in command:
        break

