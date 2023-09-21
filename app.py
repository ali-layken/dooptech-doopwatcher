from flask import Flask, request
from datetime import datetime

import requests
import time 

url = 'https://www.twitch.tv/doopieow' if True else 'https://www.twitch.tv/hasanabi'
peer = "10.213.213.1"
ping_timeout = 5


app = Flask(__name__)

def routelog():
    app.logger.info("doopwatcher" + request.path + " " + request.method + " FROM: " + request.remote_addr)

def timestamp():
    now = datetime.now()
    return str(now.hour) + ":" + str(now.minute) + ":" + str(now.second) + "." + str(now.microsecond)

@app.get("/live")
def dooplive():
    routelog()
    return "Bro is Live!!!" if "isLiveBroadcast" in requests.get(url).text else "Bruh not live :("

@app.post("/ping")
def pong():
    routelog()
    time.sleep(ping_timeout)
    if request.is_json:
        data = list(request.json.values())
        rn = timestamp()
        if data:
            nextaddr = "http://" + data.pop(0) + ":5000/ping"
            try:
                resp = requests.post(nextaddr, json=dict(enumerate(data)))
                return "Ponged thru " + request.host + " at: " + \
                       rn + \
                       "\n" + \
                       resp.text, 200
            except:
                return "Bad IP data, died at node: " + \
                       request.host + \
                       " at: " + rn, 400
        else:
            return "Ponged back from " + request.host + " at: " + rn, 200
    else:
        return "Content type is not supported.", 400
    

    