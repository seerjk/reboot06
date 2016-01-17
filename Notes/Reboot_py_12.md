# Noet 12

# wenti
1. 多线程

2. evernote上问题

## 1. 作业思路

url管理模块
    待抓取的url
    已抓取的url

url内容下载
    requests

html 内容解析

控制器，控制具体逻辑

class来组织整个代码


* 防爬虫，用图片

http://unbug.github.io/codelf/
推荐个神器，变量命名的


## 2.python单元测试unittest
def add(num1, num2):
    return num1 + num2

add(1,3)==3
add('a', 1)

## 3. echarts
http://echarts.baidu.com/

http://echarts.baidu.com/echarts2/doc/start.html
标签式单文件引入

http://echarts.baidu.com/echarts2/doc/example/pie1.html

## 日志入库，可视化展示

create table log(ip varchar(100),url varchar(100),status int,value int);
create table log_status(status int,value int);


select status sum(value) from log group by status;

* log数据处理后存入db
* flask 后端接口
* echart 前端展示   $.getJSON('url', function(res){ ... })


mysql> create table log_map(ip varchar(100),status int,geox varchar(100),geoy varchar(100),value int);
Query OK, 0 rows affected (0.03 sec)

mysql> desc log_map;
+--------+--------------+------+-----+---------+-------+
| Field  | Type         | Null | Key | Default | Extra |
+--------+--------------+------+-----+---------+-------+
| ip     | varchar(100) | YES  |     | NULL    |       |
| status | int(11)      | YES  |     | NULL    |       |
| geox   | varchar(100) | YES  |     | NULL    |       |
| geoy   | varchar(100) | YES  |     | NULL    |       |
| value  | int(11)      | YES  |     | NULL    |       |
+--------+--------------+------+-----+---------+-------+


key q5mTrTGzCSVq5QmGpI9y18Bo

F454f8a5efe5e577997931cc01de3974


http://api.map.baidu.com/location/ip?
ak=E4805d16520de693a3fe707cdc962045
&ip=202.198.16.3
&coor=bd09ll

大于 200 强
10-200 中
10以下 弱

{
    'high': [],
    'mid': [],
    'low': []
}

## 作业
作业 实现效果http://echarts.baidu.com/echarts2/doc/example/map11.html
    所有404状态都去上海
    所有的200状态，都去北京

    北京:[116.4551,40.2539]
    上海:[121.4648,31.2891]
