# coding:utf-8
from flask import Flask, render_template, request
import json

app = Flask(__name__)

user_list = [['1', 'jiji', '12345'], ['2', 'mumu', '11134']]

@app.route('/')
def index():
    return render_template('jq01.html')

@app.route('/add')
def add():
    name = request.args.get('name')
    passwd = request.args.get('passwd')
    id_num = request.args.get('id_num')

    print "*" * 20
    print "name: %s ; passwd: %s" % (name, passwd)
    print "*" * 20
    user_list.append([id_num, name, passwd])
    res = json.dumps(user_list)
    print res

    return res



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9092, debug=True)