# coding:utf-8
from flask import Flask, render_template, request
import MySQLdb as mysql
import json
import time

# con = mysql.connect(host='localhost', user='root',
#                     passwd='redhat', db='jiangkun')
# con.autocommit(True)
# cur = con.cursor()


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


def getMem():
    with open('/proc/meminfo') as f:
        total = int(f.readline().split()[1])
        free = int(f.readline().split()[1])
        memAvailable = int(f.readline().split()[1])
        buf = int(f.readline().split()[1])
        cache = int(f.readline().split()[1])

        mem_usage = (total - free - buf - cache) / 1024
        print "mem_usage ", mem_usage
        # print "memAvailable ", memAvailable
        sql = 'insert into mem (mem,time) value (%s, %s)' % (mem_usage, int(time.time()))
        db.execute(sql)


while True:
    getMem()
    time.sleep(1)


