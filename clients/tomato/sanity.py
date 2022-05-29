import requests


x = requests.post("http://192.168.2.10:5050/potato",json={"msg" : "give me a number"})

print(x.json())