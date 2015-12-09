# coding:utf-8

from flask import Flask, request
import use

app = Flask(__name__)
# 初始化 user_dict
use.update_data()

@app.route('/')
def index():
    return use.get_html()

@app.route('/add')
def add():
    user = request.args.get('user')
    pwd = request.args.get('pwd')

    if not user or not pwd:
        return '<p>need user and pwd</p>' + use.get_html()
    else:
        use.user_dict[user] = pwd
        use.update_file()

    return use.get_html()

@app.route('/delete')
def delete():
    user = request.args.get('user')
    if user in use.user_dict:
        use.user_dict.pop(user)
        use.update_file()
        return use.get_html()
    else:
        return '<p>user no exist</p>' + use.get_html()


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=9092)