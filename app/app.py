from flask import Flask, render_template
import socket
import sys

app = Flask(__name__)

@app.route("/")
def index():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return render_template('basic.html', hostname=hostname, ip_address=ip_address)
if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')
