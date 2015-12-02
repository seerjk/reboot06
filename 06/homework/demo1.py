# coding:utf-8
from flask import Flask
app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return "<h1>hello world</h1>"

@app.route('/reboot')
def reboot():
    return "<h1>hello, reboot</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9002, debug=True)