# coding:utf-8
# import
import MySQLdb as mysql

# connect
db = mysql.connect(user='root', passwd='redhat', db='jiangkun')
db.autocommit(True)
cur = db.cursor()

# sql = 'insert into server values("python", 16)'
sql = 'select * from server'

# 返回sql语句执行影响的行数
print cur.execute(sql)

# cur.fetchall() 返回执行结果 tuple
# print cur.fetchall()

for c in cur.fetchall():
    print "%s memory is %s" % c
