from speech import SpeechPatternRecognizer
from handler import Handler
from tomatoFx import mappings

spr = SpeechPatternRecognizer()
handler = Handler("127.0.0.1/potato:5050", mappings)


while True:
    spr.waitForWakeupCall("tomato")
    while True:
        command = spr.listen()
        response = handler.getResponse(command)
        spr.speak(response['msg'])
        if response["function"]:
            handler.handleFunction(response['function'])

