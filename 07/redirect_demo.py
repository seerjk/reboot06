# coding:utf-8
import db
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    # return redirect('/login')
    sql_str = "select * from server"
    res_tuple = db.execute(sql_str)

    print '*' * 20
    print url_for('login')
    print url_for('login', name='user', pwd='123')
    return render_template('print_table.html', data=res_tuple)

@app.route('/test')
def test():
    return redirect('/login')

@app.route('/login')
def login():
    return "OK"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9092)
