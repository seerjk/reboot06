# coding:utf-8
import MySQLdb as mysql
import json
import requests

# log --> db
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


db = DB('localhost', 'root', 'redhat', 'jiangkun')

# 61.159.140.123 - - [23/Aug/2014:00:01:42 +0800] "GET /favicon.ico HTTP/1.1" 404 \ "-" "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36 LBBROWSER" "-"

# 本地缓存IP数据 dic存储，不用每次都去网络获取，提升效率
ip_cache = {}

def getGeo(ip):
    key = "q5mTrTGzCSVq5QmGpI9y18Bo"
    url = "http://api.map.baidu.com/location/ip?ak=%s&coor=bd09ll&ip=" %(key)
    ip_url = url + ip
    # print ip_url

    if ip_cache.has_key(ip):
        return ip_cache[ip]
    else:
        try:
            ip_info = requests.get(ip_url)
            print ip_info.content
            res_json = ip_info.json()
            ip_cache[ip] = res_json['content']['point']
            return res_json['content']['point']
        except:
            print 'ip error %s' % (ip)
            return 'error'


f = open('www_access_20140823.log')
res = {}

for l in f:
    tmp = l.split(' ')
    ip = tmp[0]
    status = tmp[8]
    res[(ip,status)] = res.get((ip,status), 0) + 1

for key in res:
    print key, res[key]
    geo = getGeo(key[0])
    print geo
    # break
    if geo == 'error':
        print 'no ip_geo info'
    else:
        sql = 'insert into log_map values("%s","%s","%s","%s","%s")' %(key[0], key[1], geo['x'], geo['y'], res[key])
        db.execute(sql)
    # print '("%s","%s")' %(key, res[key])
