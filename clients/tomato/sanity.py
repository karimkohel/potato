from importlib.util import spec_from_file_location
from operator import truediv
from re import T
from speech import SpeechPatternRecognizer

spr = SpeechPatternRecognizer()

spr.speak("powered on")

# while True:

#     spr.waitForWakeupCall("tomato")

#     while True:
#         msg = spr.listen()
#         spr.speak("Comment: send result to server and get answer")
#         spr.speak("Comment: speak response")
#         spr.speak("Comment: carry out task")
#         break