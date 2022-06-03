import RPi.GPIO as GPIO
import smtplib
import dotenv

class HardWare():

    thereIsFire = False
    thereIsGas = False
    touched = False

    def __init__(self, firePin, gasPin, touchPin, spr):
        GPIO.setmode(GPIO.BCM)
        self.touchPin = touchPin
        self.gasPin = gasPin
        self.firePin = firePin
        self.spr = spr

        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(dotenv.senderMail, dotenv.mailPassword)
        print("logged in mail server")

        GPIO.setup(firePin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(gasPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(touchPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.add_event_detect(firePin, GPIO.BOTH, callback=self.listenForFire, bouncetime=50)
        GPIO.add_event_detect(gasPin, GPIO.BOTH, callback=self.listenForGas, bouncetime=50)
        GPIO.add_event_detect(touchPin, GPIO.BOTH, callback=self.listenForTouch, bouncetime=50)


    def listenForFire(self, channel):
        if GPIO.input(self.firePin):
            subject = "Fire Alarm"
            body = "Tempurature rising quickly indicating a fire might be occuring in the house. Call 911"
            self.handleMails(subject, body)
            self.thereIsFire = True
            while GPIO.input(self.firePin):
                self.spr.speak("FIRE")
        else:
            HardWare.thereIsFire = False


    def listenForGas(self, channel):
        if GPIO.input(self.gasPin):
            subject = "Gas Alarm"
            body = "Gas levels rising quickly indicating a gas leak might be occuring in the house. Call 911"
            self.handleMails(subject, body)
            self.thereIsGas = True
            while GPIO.input(self.gasPin):
                self.spr.speak("GAS")
        else:
            self.thereIsGas = False


    def listenForTouch(self, channel):
        if GPIO.input(self.touchPin):
            print("touch")
            self.touched = True


    def handleMails(self, mailSubject, mailBody):
        email = f"Subject: {mailSubject}\n\n{mailBody}"
        for receiver in dotenv.receivingMails:
            self.server.sendmail(dotenv.senderMail, receiver, email)

    def checkAlarm(self):
        return (self.thereIsFire or self.thereIsGas)

        