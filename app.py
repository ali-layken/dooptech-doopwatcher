from flask import Flask
import requests

url = 'https://www.twitch.tv/doopieow' if True else 'https://www.twitch.tv/hasanabi'

app = Flask(__name__)

@app.get("/live")
def dooplive():
    return "Bro is Live!!!" if "isLiveBroadcast" in requests.get(url).text else "Bruh not live :("