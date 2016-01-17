# coding:utf-8
import MySQLdb as mysql

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

f = open('www_access_20140823.log')
# res = {}

# for l in f:
#     tmp = l.split(' ')
#     ip = tmp[0]
#     url = tmp[6]
#     status = tmp[8]

#     res[(ip,url,status)] = res.get((ip,url,status), 0) + 1

# for key in res:
#     sql = 'insert into log values("%s","%s","%s","%s")' %(key[0],key[1],key[2],res[key])
#     db.execute(sql)
#     print '("%s","%s","%s","%s")' %(key[0],key[1],key[2],res[key])

res = {}

for l in f:
    tmp = l.split(' ')
    status = tmp[8]

    res[status] = res.get(status, 0) + 1

for key in res:
    sql = 'insert into log_status values("%s","%s")' %(key, res[key])
    db.execute(sql)
    print '("%s","%s")' %(key, res[key])