#! /usr/bin/python
from speech import SpeechPatternRecognizer
from handler import Handler
import tomatoFx as tfx
from time import sleep

fire = False
gas = False

def listenForFire():
    global fire
    fire = True
def listenForGas():
    global gas
    gas = True
    
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(, GPIO.RISING, callback=listenForFire, bouncetime=100)
GPIO.add_event_detect(BUTTON_GPIO, GPIO.RISING, callback=listenForGas, bouncetime=100)

spr = SpeechPatternRecognizer()
handler = Handler("http://192.168.2.10:5050/potato")


# while True:
    # spr.waitForWakeupCall("tomato")

while True:
    while fire or gas:
        if fire:
            spr.speak("Fire fire fire, call 911")
        if gas:
            spr.speak("Gas allert, gas allert")

    command = spr.listen()
    # command = input("INPUT COMMAND: ")
    response = handler.getResponse(command)
    spr.speak(response['res'])
    if "functionCode" in response:
        functions[response["functionCode"]]()
    if "exit" in command:
        break