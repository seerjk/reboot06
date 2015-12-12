from flask import Flask, request, render_template
import json
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/name')
def name():
    print "*" * 20
    print "/name"
    print "*" * 20
    # return "I am woniu"
    # return {'name': 'reboot', 'age':1}
    # name =  {'name': 'reboot', 'age':1}
    # res = json.dumps(name)
    arr = [['reboot','123'], ['admin','admin123']]
    res = json.dumps(arr)
    print res
    return res

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9092, debug=True)
