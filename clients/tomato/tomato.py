from speech import SpeechPatternRecognizer
from handler import Handler
from tomatoFx import mappings as functions


# use this link for gpio interupts

spr = SpeechPatternRecognizer()
handler = Handler("127.0.0.1/potato:5050")


while True:
    spr.waitForWakeupCall("tomato")
    while True:
        command = spr.listen()
        # get json response
        response = handler.getResponse(command)
        # speak the msg part of that json
        spr.speak(response['msg'])
        # if json response has function code then execute said function
        if response["functionCode"]:
            functions[response["functionCode"]]()
        # if response has an exit flag then exit and wait for next wake up
        if response['exit']:
            break

