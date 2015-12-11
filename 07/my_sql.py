# import
import MySQLdb as mysql

# connect
db = mysql.connect(user='root', passwd='redhat', db='jiangkun')
db.autocommit(True)
cur = db.cursor()

sql = 'insert into server values("python", 16)'

print cur.execute(sql)
