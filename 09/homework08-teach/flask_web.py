# coding:utf-8
from flask import Flask,request,render_template,session,redirect,url_for
app = Flask(__name__)
# session必须配置一个加密密钥
app.secret_key='adfdsafjk;l!#$dadfdsafasdfsaf'


import MySQLdb as mysql
import json

con= mysql.connect(user="root",passwd="redhat",db="jiangkun")
con.autocommit(True)
cur = con.cursor()


@app.route('/')
def index():
    if 'username' not in session:
        print url_for('login')
        return redirect(url_for('login'))
    else:
        return render_template('index.html')


@app.route('/loginaction')
def loginaction():
    name = request.args.get('name')
    pwd = request.args.get('pwd')
    if name == 'admin' and pwd == '123':
        session['username'] = 'admin'
    
    print url_for('index')
    return redirect(url_for('index'))
    # else:
    #     pass
    #     return 'error'


@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('index'))


@app.route('/list')
def list():
    sql='select * from server'
    cur.execute(sql)
    return json.dumps(cur.fetchall())


@app.route('/add')
def add():
    name = request.args.get('name')
    mem = request.args.get('mem')

    sql = 'insert into server (host, memory) values ("%s",%s)'%(name,mem)
    cur.execute(sql)
    return 'ok'


@app.route('/del')
def delelt():
    server_id = request.args.get('id')
    sql='delete from server where id='+server_id
    cur.execute(sql)
    return 'ok'


@app.route('/login')
def login():
    return render_template('login.html')


if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True,port=9092)