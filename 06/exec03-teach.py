# coding:utf-8

from flask import Flask, request, render_template
app = Flask(__name__)

user_dict = {}
for l in open('user.txt'):
    tmp = l.strip().split(' ')
    user_dict[tmp[0]] = tmp[1]
print user_dict

@app.route('/')
def index():
    # return render_template('index.html')
    return render_template('exec01.html')

@app.route('/login')
def login():
    # user_dict is a global var
    global user_dict
    user = request.args.get('user')
    pwd = request.args.get('pwd')
    res = 'no'

    if user in user_dict and user_dict[user] == pwd:
        res = 'OK'

    # for l in open('user.txt'):
    #     l = l.strip()
    #     temp = l.split(' ')

    #     if user==temp[0] and pwd==temp[1]:
    #         res = "OK"

    return res

@app.route('userlist')
def userlist():
    table_str = "<table>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9092, debug=True)
