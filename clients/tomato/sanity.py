import requests


x = requests.post("http://127.0.0.1:8000/potato",json={"msg" : "what is the date"})

print(x.json())