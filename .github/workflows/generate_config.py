import requests
import os
import json
API_URL = os.getenv("API_URL")


def generate():
    data = json.load(open("config.json","r"))
    data["social"] = requests.get(API_URL + "socials").json()
    data["projects"] = requests.get(API_URL + "projects").json()
    
    json.dump(data, open("config.json","w"), ensure_ascii=False)

if __name__ == "__main__":
    generate()