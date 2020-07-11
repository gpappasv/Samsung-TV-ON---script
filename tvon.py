#!/usr/bin/env python
from flask import Flask 
from wakeonlan import send_magic_packet

app = Flask(__name__)

@app.route("/tvon")
def hello():
    for x in range (0, 7):
            send_magic_packet('84:C0:EF:57:C0:7F') //MAC ADDRESS OF THE SAMSUNG TV
    return "I have turned on the TV!"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")
