# coding:utf-8
from flask import Flask, render_template, request
import MySQLdb as mysql
import json
import time
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

# 饼图
@app.route('/ipmap')
def ipmap():
    return render_template('ipmap.html')


# {
#     name:'xxx',
#     value:'100',
#     geoCoord:[125.03,46.58]
# }


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

# map high mid low
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


@app.route('/ipmap4migratedata')
def ipmap4migratedata():
    res = {
        'geoCoord': {},
        '404': {},
        '200': {}
    }
    # city -- (x,y)
    sql = 'select city,geox,geoy from log_map_city where (status=200 or status=404) and city!="" group by city'

    # city value  where status = 200
    # select city,sum(value) from log_map_city where status=200 and city!="" group by city;
    # city value  where status = 404
    # select city,sum(value) from log_map_city where status=404 and city!="" group by city;



@app.route('/ipmap4migrate')
def ipmap4migrate():
    return render_template('ipmap4migrate.html')


# teach_homework
@app.route('/line')
def line():
    return render_template('ipmap4migrate_teach.html')


@app.route('/linedata')
def linedata():
    # IP和 geox geoy对应 来模拟city
    res = {
        "alldata": [],
        "dataRange_max": 0,
        "geodata": {
            "北京":[116.4551,40.2539],
            "上海":[121.4648,31.2891]
        },
        "beijingdata": [],
        "beijingpoint": [],
        "shanghaidata": [],
        "shanghaipoint": []
    }
    # sql = 'select * from log_map limit 100'
    '''
    sql = 'select * from log_map order by value desc limit 60'
    cur = db.execute(sql)
    
    for c in cur["cur"].fetchall():
        res['geodata'][c[0]] = [c[2],c[3]]
        if c[4] > res["dataRange_max"]:
            res["dataRange_max"] = c[4]
        if c[1] == 200:
            # beijing
            res['alldata'].append([
                {"name":'北京'},
                {"name":c[0]}
            ])
            res['beijingdata'].append([
                {"name":"北京"},
                {"name":c[0],"value":c[4]}
            ])
            res['beijingpoint'].append({
                "name":c[0],
                "value":c[4]
            })
        elif c[1] == 404:
            # shanghai
            res['alldata'].append([
                {"name":'上海'},
                {"name":c[0]}
            ])
            res['shanghaidata'].append([
                {"name":"上海"},
                {"name":c[0],"value":c[4]}
            ])
            res['shanghaipoint'].append({
                "name":c[0],
                "value":c[4]
            })
    '''
    sql = 'select * from log_map where status=200 order by value desc limit 10'
    cur = db.execute(sql)
    
    for c in cur["cur"].fetchall():
        res['geodata'][c[0]] = [c[2],c[3]]
        if c[4] > res["dataRange_max"]:
            res["dataRange_max"] = c[4]
        # beijing
        res['alldata'].append([
            {"name":'北京'},
            {"name":c[0]}
        ])
        res['beijingdata'].append([
            {"name":"北京"},
            {"name":c[0],"value":c[4]}
        ])
        res['beijingpoint'].append({
            "name":c[0],
            "value":c[4]
        })

    sql = 'select * from log_map where status=404 order by value desc limit 10'
    cur = db.execute(sql)
    
    for c in cur["cur"].fetchall():
        res['geodata'][c[0]] = [c[2],c[3]]
        if c[4] > res["dataRange_max"]:
            res["dataRange_max"] = c[4]
        # shanghai
        res['alldata'].append([
            {"name":'上海'},
            {"name":c[0]}
        ])
        res['shanghaidata'].append([
            {"name":"上海"},
            {"name":c[0],"value":c[4]}
        ])
        res['shanghaipoint'].append({
            "name":c[0],
            "value":c[4]
        })

    return json.dumps(res)

# mem 
@app.route('/mem')
def mem():
    return render_template('mem.html')

# 用于增量查询，记录开始查的timestamp
time_init = 0
@app.route('/memdata')
def memdata():
    global time_init
    res = {
        'x': [],
        'data': []
    }
    if time_init > 0:
        # 增量查
        sql = 'select * from mem where time > %s' % (time_init)
    else:
        # 首次 全量查询
        sql = 'select * from mem'

    print sql
    cur = db.execute(sql)

    for c in cur["cur"].fetchall():
        res['data'].append(c[0])
        # res['x'].append(c[1])
        t = time.strftime('%H:%M:%S', time.localtime(c[1]))
        res['x'].append(t)
        time_init = c[1]

    return json.dumps(res)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9092)
