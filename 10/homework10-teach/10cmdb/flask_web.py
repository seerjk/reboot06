# coding:utf-8
from flask import Flask, render_template, request
import MySQLdb as mysql
import json
# con = mysql.connect(host='localhost', user='root',
#                     passwd='redhat', db='jiangkun')
# con.autocommit(True)
# cur = con.cursor()
app = Flask(__name__)

class DB():
    def __init__(self, host, user, passwd, db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.conn = None
        self.connect()

    def connect(self):
        self.conn = mysql.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db)
        self.conn.autocommit(True)

    def execute(self, sql):
        # res = None
        msg = 'ok'
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
        except Exception, e:
            print e
            print "reconnect database"
            self.connect()
            # cur = self.conn.cursor()
            try:
                cur = self.conn.cursor()
                cur.execute(sql)
            except:
                msg = 'error in sql'
        
        return {"cur": cur, "msg": msg}

    def add():
        pass


db = DB('localhost', 'root', 'redhat', 'jiangkun')


@app.route('/', methods=['GET', 'POST'])
def index():
    print request.method
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        sql = 'select * from server10'

        cur = db.execute(sql)
        # try:
        #     res = cur.execute(sql)
        # except:
        #     con = mysql.connect(host='localhost', user='root',
        #             passwd='redhat', db='jiangkun')
        #     con.autocommit(True)
        #     cur = con.cursor()
        #     print "reconnect database"
        #     res = cur.execute(sql)
        print cur
        print cur["cur"]

        return json.dumps(cur["cur"].fetchall())


@app.route('/addhost')
def addhost():
    name = request.args.get('name')
    mem = request.args.get('mem')
    end_date = request.args.get('end_date')
    sql = 'insert into server10 (name,memory,end_date) values ("%s",%s,"%s")' % (name, mem, end_date)
    print sql
    res = 'ok'
    cur = db.execute(sql)

    # try:
    #     cur.execute(sql)
    # except:
    #     res = 'error in sql'
    return cur["msg"]


@app.route('/delhost', methods=['POST'])
def delhost():
    id = request.form.get('id')
    sql = 'delete from server10 where id=%s' %(id)

    res = 'ok'
    db.execute(sql)
    # try:
    #     cur.execute(sql)
    # except:
    #     res = 'error in sql'

    return res


# flask端 判断 DELETE操作
# 是 if request.method='DELETE' 吗？
# yes

# 但是jquery就没有便捷的方法，只能用$.ajax
# 这个基础函数去发送请求
# 指定 ajax 的type: delete 吗？
# yes



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9092)
