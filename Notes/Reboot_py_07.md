# Note 07

## 1.作业讲解

./liaoyao
flask重定向路由:
redircte()

./zhuang_xuebing
index.html  --  jijia模板

./wojiawu
def func():
    global user_dict

./songxiang
bootstrap  样式

GET
POST

RESTful API
@app.route('/user')
if request.methon="GET":

http://item.jd.com/11076338.html
排序，查找，二叉树，列表，堆
红黑树

https://leetcode.com/problemset/algorithms/


## 2. 复习
优化log日志处理代码

### 期中回顾

* 变量
* 逻辑判断
* 循环
* list
* 字符串
* dict
* 函数
* 文件
* 前端基础
* 模块
* flask

语句和逻辑判断
变量
if else
for while
break continue

期中回顾——list
定义list
遍历
删除
取值
list的方法
元组

期中回顾——dict
字典是什么
取值
遍历
删除
dict的方法

期中回顾——字符串
定义
切片
切割
查找
替换

期中回顾——文件操作
打开文件
读文件
写文件
关闭文件

期中回顾——前端基础
html常用标签
css作用及常用属性
javascript

期中回顾——函数
函数创建
返回值
参数
作用域

期中回顾——模块
模块的定义
模块的使用
python自带模块
第三方模块

## 3.

180.153.191.128:22 
woniu
woniu123

```
mysql -ureboot -preboot123
```

```
show databases;


create database jiangkun;
use jiangkun;

// 建表
create table server(host varchar(100), memory int);
// 表结构
desc server;
//  insert
insert into server values('local', 4);

select * from server;

// update 一定要用where指定条件
update server set memory=1 where host="local";

update server set memory=16 where host="test";
select * from server where host="test";

//limit 限制影响的行数
update server set memory=5 limit 4;

// 没有where 会死人的
update server set memory=1;

// delete
delete from server where memory=2;

// drop table
drop table server;

// 远程连接
update user set Host='*' where User='reboot';
```

封装在一个db模块，使用的时候用db.execute()
```
# coding:utf-8
# import
import MySQLdb as mysql

# connect
db = mysql.connect(user='reboot', passwd='reboot123', db='jiangkun')
db.autocommit(True)
cur = db.cursor()

sql='insert into server values("python", 16)'

print cur.execute(sql)
# 返回sql语句执行影响的行数

# cur.fetchall() 返回执行结果 tuple
# print cur.fetchall()
 
for c in cur.fetchall():
    print "%s memory is %s" % c
```

db.py
```
$ cat db.py 
# coding:utf-8
# import
import MySQLdb as mysql

def execute(sql_str):
    # connect
    db = mysql.connect(user='reboot', passwd='reboot123', db='jiangkun')
    db.autocommit(True)
    cur = db.cursor()
        
    # print cur.execute(sql)
    cur.execute(sql_str)

if __name__ == "__main__":
    sql_str='insert into server values("python", 16)'
    execute(sql_str)
```


主键+自增
```
MariaDB [jiangkun]> create table server(id int not null auto_increment primary key, host varchar(100), memory int);
Query OK, 0 rows affected (0.01 sec)

MariaDB [jiangkun]> desc server;
+--------+--------------+------+-----+---------+----------------+
| Field  | Type         | Null | Key | Default | Extra          |
+--------+--------------+------+-----+---------+----------------+
| id     | int(11)      | NO   | PRI | NULL    | auto_increment |
| host   | varchar(100) | YES  |     | NULL    |                |
| memory | int(11)      | YES  |     | NULL    |                |
+--------+--------------+------+-----+---------+----------------+
3 rows in set (0.00 sec)

MariaDB [jiangkun]> insert into server (host, memory) values ('reboot', 2);
Query OK, 1 row affected (0.07 sec)

MariaDB [jiangkun]> insert into server (host, memory) values ('reboot', 2);
Query OK, 1 row affected (0.00 sec)

MariaDB [jiangkun]> insert into server (host, memory) values ('reboot', 2);
Query OK, 1 row affected (0.00 sec)

MariaDB [jiangkun]> insert into server (host, memory) values ('reboot', 2);
Query OK, 1 row affected (0.01 sec)

MariaDB [jiangkun]> insert into server (host, memory) values ('reboot', 2);
Query OK, 1 row affected (0.00 sec)

MariaDB [jiangkun]> insert into server (host, memory) values ('reboot', 2);
Query OK, 1 row affected (0.00 sec)

MariaDB [jiangkun]> insert into server (host, memory) values ('reboot', 2);
Query OK, 1 row affected (0.00 sec)

MariaDB [jiangkun]> insert into server (host, memory) values ('reboot', 2);
Query OK, 1 row affected (0.01 sec)

MariaDB [jiangkun]> select * from server;
+----+--------+--------+
| id | host   | memory |
+----+--------+--------+
|  1 | reboot |      2 |
|  2 | reboot |      2 |
|  3 | reboot |      2 |
|  4 | reboot |      2 |
|  5 | reboot |      2 |
|  6 | reboot |      2 |
|  7 | reboot |      2 |
|  8 | reboot |      2 |
+----+--------+--------+
8 rows in set (0.01 sec)

MariaDB [jiangkun]> select * from server where id > 5;
+----+--------+--------+
| id | host   | memory |
+----+--------+--------+
|  6 | reboot |      2 |
|  7 | reboot |      2 |
|  8 | reboot |      2 |
+----+--------+--------+
3 rows in set (0.00 sec)

MariaDB [jiangkun]> delete from server where id < 4;
Query OK, 3 rows affected (0.01 sec)

MariaDB [jiangkun]> select * from server;
+----+--------+--------+
| id | host   | memory |
+----+--------+--------+
|  4 | reboot |      2 |
|  5 | reboot |      2 |
|  6 | reboot |      2 |
|  7 | reboot |      2 |
|  8 | reboot |      2 |
+----+--------+--------+
5 rows in set (0.00 sec)
```

cur.fetchall()
cur.fetchone()
和readline很像，有指针，第二次 fetchall() 就没有数据了，指向最后



Flask redirect
Flask url_for

redirect 用于判断用户是否登陆后的跳转状态

```
# coding:utf-8
import db
from flask import Flask, render_template, url_for, redirect                      

app = Flask(__name__)

@app.route('/')
def index():
    # return redirect('/login')
    sql_str = "select * from server"
    res_tuple = db.execute(sql_str)

    print '*' * 20
    print url_for('login')
    print url_for('login', name='user', pwd='123')
    return render_template('print_table.html', data=res_tuple)

@app.route('/test')
def test():
    return redirect('/login')

@app.route('/login')
def login():
    return "OK"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9092)
```

输出

```
********************
/login
/login?pwd=123&name=user
```


bootstrap
http://v3.bootcss.com/
http://cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css


http://v3.bootcss.com/css/#forms

图标：
http://v3.bootcss.com/components/
font-awesome  不常用图标

登陆状态：
    session  -- 后端flask全局变量
    登陆样式   http://v3.bootcss.com/examples/signin/

## 作业
上节课作业放到数据库
    id 列
    name 可以重复
    按照ID来删除

jinja 模板

bootstrap 美化 table form

功能拆分

路由拆分
    add
    delete
