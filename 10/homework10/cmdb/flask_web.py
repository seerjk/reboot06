# coding: utf-8
from flask import Flask, render_template, request
import MySQLdb as mysql
import json

con = mysql.connect(host='127.0.0.1', user='root', passwd='redhat', db='jiangkun')
con.autocommit(True)
cur = con.cursor()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    print request.method
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        sql = 'select * from server10'
        cur.execute(sql)
        res = cur.fetchall()
        # print res
        # print json.dumps(res)
        return json.dumps(res)


@app.route('/addhost')
def addhost():
    name = request.args.get('name')
    mem = request.args.get('mem')
    end_date = request.args.get('end_date')
    sql = 'insert into server10 (name, memory, end_date) values ("%s", %s, "%s")' % (name, mem, end_date)

    res = 'ok'
    # print sql
    try:
        cur.execute(sql)
    except:
        # except (attrubutibe Error,mysqldb.opeartionError)
        # 捕获mysql.operationerror
        res = 'error in sql'
        # 打印日志

    return res

@app.route('/delhost')
def delhost():
    del_id = request.args.get('id')
    sql = 'delete from server10 where id=%s' % (del_id)
    res = 'ok'
    try:
        cur.execute(sql)
    except:
        res = 'error in sql'
        
    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=9092)