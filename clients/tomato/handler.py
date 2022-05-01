import requests

class Handler():
    def __init__(self, ip, functions):
        self.functions = functions
        self.ip = ip
    
    # there should be a master table with all request codes
    def handleRequest(self, requestCode):
        self.functions[requestCode]()

    def getResponse(self, txtMsg):
        msg = {
            "msg":txtMsg
        }
        response = requests.post(self.ip, json=msg)
        return response
