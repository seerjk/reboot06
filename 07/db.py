# coding:utf-8
# import
import MySQLdb as mysql

def execute(sql_str):
    # connect
    db = mysql.connect(user='root', passwd='redhat', db='jiangkun')
    db.autocommit(True)
    cur = db.cursor()

    # sql_str='insert into server values("python", 16)'
    # print cur.execute(sql)
    cur.execute(sql_str)
    return cur.fetchall()

if __name__ == "__main__":
    # sql_str='insert into server values("python", 16)'
    sql_str='select * from server'
    res_tuple = execute(sql_str)
    for c in res_tuple:
        print "%s %s %s" % c
