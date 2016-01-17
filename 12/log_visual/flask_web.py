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
    # elif request.method == 'POST':
    #     sql = 'select * from log_status'

    #     cur = db.execute(sql)
    #     print cur
    #     print cur["cur"]

    #     return json.dumps(cur["cur"].fetchall())

@app.route('/statusdata')
def statusdata():
    sql = 'select * from log_status'
    cur = db.execute(sql)
    # result = cur["cur"].fetchall()

    res = {
        "legend": [],
        "data": []
    }

    for r in cur["cur"].fetchall():
        res["legend"].append(r[0])
        res["data"].append({
            "name":r[0],
            "value":r[1]
            # "value":int(r[1])
        })

    return json.dumps(res)


@app.route('/ipmap')
def ipmap():
    return render_template('ipmap.html')


# {
#     name:'xxx',
#     value:'100',
#     geoCoord:[125.03,46.58]
# }
@app.route('/mapdata')
def mapdata():
    # sql = 'select ip,geox,geoy,sum(value) from log_map group by ip;'
    # cur = db.execute(sql)

    # res = {
    #     "legend": [],
    #     "data": []
    # }
    # for r in cur["cur"].fetchall():
    #     res["data"].append({
    #         "name": r[0],
    #         "value": r[3],
    #         "geoCoord":[r[1],r[2]]
    #     })
    # sql = 'select * from log_map limit 10'
    
    status_list = ['200', '404', '304', '206']
    res = {}

    for i in status_list:
        res[i] = []
        sql = 'select * from log_map where status=%s' %(i)
        cur = db.execute(sql)

        for r in cur["cur"].fetchall():
            tmp = {}
            tmp['name'] = r[0]
            tmp['value'] = r[4]
            tmp['geoCoord'] = [float(r[2]), float(r[3])]
            res[i].append(tmp)

    return json.dumps(res)

@app.route('/ipmap2data')
def ipmap2data():
    sql = 'select * from log_map'
    cur = db.execute(sql)
    res = {
        "high": [],
        "mid": [],
        "low": []
    }

    for r in cur["cur"].fetchall():
        tmp = {}
        tmp['name'] = r[0]
        tmp['value'] = r[4]
        tmp['geoCoord'] = [float(r[2]), float(r[3])]

        if  r[4] > 200:
            res['high'].append(tmp)
        elif r[4] < 10:
            res['low'].append(tmp)
        else:
            res['mid'].append(tmp)

    return json.dumps(res)


@app.route('/ipmap2')
def ipmap2():
    return render_template('ipmap2.html')

@app.route('/ipmap3data')
def ipmap3data():
    sql = 'select * from log_map'
    cur = db.execute(sql)
    res = {
        "high": [],
        "mid": [],
        "low": []
    }
    max_num = 0
    for r in cur["cur"].fetchall():
        tmp = {}
        tmp['name'] = r[0]
        tmp['value'] = r[4]
        tmp['geoCoord'] = [float(r[2]), float(r[3])]

        if r[4] > max_num:
            max_num = r[4]

        if  r[4] > 200:
            res['high'].append(tmp)
        elif r[4] < 10:
            res['low'].append(tmp)
        else:
            res['mid'].append(tmp)

    res['max'] = max_num
    
    return json.dumps(res)

@app.route('/ipmap3')
def ipmap3():
    return render_template('ipmap3.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9092)
