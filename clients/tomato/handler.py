import requests

class Handler():
    def __init__(self, ip):
        self.ip = ip


    def getResponse(self, txtMsg):
        msg = {
            "msg":txtMsg
        }
        response = requests.post(self.ip, json=msg)
        return response
