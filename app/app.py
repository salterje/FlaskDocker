from flask import Flask, render_template
import socket
import sys
import time
import os

app = Flask(__name__)

@app.route("/")
def index():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    local_time = time.asctime()
    uname = os.uname()
    actual_os = uname[3]
    KEY1 = os.environ.get('KEY1')
    KEY2 = os.environ.get('KEY2')

    return render_template('basic.html', hostname=hostname,
                            ip_address=ip_address, local_time=local_time,
                            actual_os=actual_os, KEY1=KEY1, KEY2=KEY2)

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')
