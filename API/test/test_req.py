import requests
import json
for i in range(1):
    data = {"ID":"HAPC","message": "what is your name ?"}
    url = "http://14.236.238.0:8000/"
    response = requests.post(url, json=data, headers={"Content-Type": "application/json"})
    print("-----------------------------------output---------------------------------------\n")
    print(response.json())
    print("\n-----------------------------------output---------------------------------------")