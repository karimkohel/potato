import speech_recognition as sr
import pyttsx3 as tts
import os

class SpeechPatternRecognizer():

    def __init__(self):

        self.settings = {'speech_speed': 160, 'voice_number': 1, 'music_folder': ''}

        if os.name == "posix" :
            self.settings["voice_number"] = 17

        # init text to speech engine with specified settings
        self.speaker = tts.init()
        voices = self.speaker.getProperty('voices')
        self.speaker.setProperty('voice', voices[self.settings['voice_number']].id)
        self.speaker.setProperty('rate', self.settings["speech_speed"])

        # init speech recognizer engine with google
        self.recognizer = sr.Recognizer()

    def speak(self, text):
        self.speaker.say(text)
        try:
            self.speaker.runAndWait()
        except Exception as e:
            print("Cheack your internet connection please, error : " + str(e))

    def listen(self, stealthMode = False):

        while True:
            try:
                with sr.Microphone(device_index=1) as mic:
                    self.recognizer.adjust_for_ambient_noise(mic)
                    audio = self.recognizer.listen(mic, phrase_time_limit=4)

                    text = self.recognizer.recognize_google(audio)
                    text = text.lower()

                    return text
            except sr.UnknownValueError:
                if stealthMode:
                    continue
                else:
                    self.speak("Sorry didn't get that, try again")
            except sr.WaitTimeoutError:
                pass
            except Exception as e:
                self.speak("Cheack your internet connection please, error : " + str(e))
                print(e)

    def waitForWakeupCall(self, text, hardware):

        while (not hardware.touched) or hardware.thereIsFire or hardware.thereIsGas:
            print("waiting for wake UP")
            audio = self.listen(stealthMode=True)
            print("in wake up i heard : ", audio)

            if audio.find(text) >= 0:
                self.speak("hey there")
                break
        hardware.touched = False

    def confirmCommand(self, text = "are you sure you want to confirm your last command"):
        self.speak(text)
        confirmation = self.listen()
        if confirmation.find("yes") >= 0:
            return True
        else:
            return False

