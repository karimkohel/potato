#! /usr/bin/python
from speechTomato import SpeechPatternRecognizer
from handler import Handler
import tomatoFx as tfx
from time import sleep

spr = SpeechPatternRecognizer()
hardware = tfx.HardWare(25, 6, 21, spr) # input pins for fire, gas, touch
handler = Handler("http://192.168.2.10:5050/potato")


while True:
    spr.waitForWakeupCall("tomato", hardware)
    while True:

        if hardware.checkAlarm():
            break

        command = spr.listen()
        print("In main loop i heard: ", command)
        response = handler.getResponse(command)
        spr.speak(response['res'])
        if "functionCode" in response:
            functions[response["functionCode"]]()
        print(command.find("exit") >= 0)
        if command.find("exit") >= 0:
            break