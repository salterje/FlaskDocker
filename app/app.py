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

    return render_template('basic.html', hostname=hostname,
                            ip_address=ip_address, local_time=local_time,
                            actual_os=actual_os)

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')
