import requests


x = requests.post("http://127.0.0.1:5050/potato",json={"msg" : "when is prayer"})

print(x.json())