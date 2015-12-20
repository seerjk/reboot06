# coding:utf-8
import MySQLdb as mysql
from flask import Flask, request, render_template
import json

app = Flask(__name__)
con = mysql.connect(user="root", passwd="redhat", db="jiangkun")
con.autocommit(True)
cur = con.cursor()

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/list')
def list():
    sql = "select * from user"
    cur.execute(sql)
    res_json = json.dumps(cur.fetchall())
    print res_json
    return res_json


@app.route('/add')
def add():
    name = request.args.get('name')
    passwd = request.args.get('passwd')
    sql = "insert into user (name, passwd) values (%s, %s)" % (name, passwd)
    cur.execute(sql)
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=9092)