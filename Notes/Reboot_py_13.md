# Note 13

## 1. echart 迁徙图
geoCoord 包含所有的城市对应的经纬度数据

markLine

markPoint 绘制闪烁的点 + value


d3js 来做大数据可视化
http://d3js.org/


如果想拖动dataRange的时候能够实时获取后端数据，能实现吗？
d3是什么？
纯洁的蜗牛(316783812)  11:17:43
试试？
datarange我看下有没有change事件
如果没有的话，我们可以自己墨迹datarange
用小滑块模拟就成
传递数据，后端收一个limit即可


## 2. 实时内存

echart 动态数据图
http://echarts.baidu.com/echarts2/doc/example/dynamicLineBar.html

获取mem信息
```
$ cat /proc/meminfo 
MemTotal:        2035384 kB
MemFree:         1500200 kB
MemAvailable:    1597744 kB
Buffers:             764 kB
Cached:           199780 kB
```


建表
mysql> create table mem(mem int, time int);
Query OK, 0 rows affected (0.04 sec)

mysql> desc mem;
+-------+---------+------+-----+---------+-------+
| Field | Type    | Null | Key | Default | Extra |
+-------+---------+------+-----+---------+-------+
| mem   | int(11) | YES  |     | NULL    |       |
| time  | int(11) | YES  |     | NULL    |       |
+-------+---------+------+-----+---------+-------+
2 rows in set (0.00 sec)


## 3. time
python time模块详解
http://blog.csdn.net/kiki113/article/details/4033017

time.time()  时间戳形式，存储在db中，通用
    ||
time.localtime()
    ||
time.strftime(format[, tuple]) -> string


In [1]: import time

In [2]: time.time()
Out[2]: 1453528552.422136

In [3]: n_time = int(time.ti)
time.time      time.timezone  

In [3]: n_time = int(time.time())

In [4]: n_time
Out[4]: 1453528570

In [5]: time.ctime()
Out[5]: 'Sat Jan 23 13:57:49 2016'
    

In [6]: time.strftime('%y',time.localtime())
Out[6]: '16'

In [7]: time.localtime()
Out[7]: time.struct_time(tm_year=2016, tm_mon=1, tm_mday=23, tm_hour=13, tm_min=58, tm_sec=26, tm_wday=5, tm_yday=23, tm_isdst=0)

In [9]: time.localtime(n_time)
Out[9]: time.struct_time(tm_year=2016, tm_mon=1, tm_mday=23, tm_hour=13, tm_min=56, tm_sec=10, tm_wday=5, tm_yday=23, tm_isdst=0)

In [10]: time.strftime('%Y', time.localtime(n_time))
Out[10]: '2016'

In [11]: time.strftime('%H:%M:%S', time.localtime(n_time))
Out[11]: '13:56:10'


## 4.分享项目开发中可能用到的知识

一个项目必备的三类知识(python)

* python语言基础
* 框架知识(flask)
* 前端知识 -- 这是个看脸的社会

### 4.1 不完全统计的技能树

#### 4.1.1 代码的组织结构
包结构 vs 蓝图结构

virtualenv
虚拟环境，防止污染物理机环境

$ vim test.txt
flask

$ pip install -r test.txt

$ tree
.
├── app
│   ├── __init__.py   入口文件
│   ├── __init__.pyc
│   ├── main.py    入口文件包含模块
│   ├── main.pyc
│   ├── views.py   入口文件包含模块
│   └── views.pyc
└── run.py


```
$ cat run.py 
#!/usr/bin/env python

# app 文件 app.py
from app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9092,debug=True)
```

入口文件
```
$ cat app/__init__.py
from flask import Flask

app = Flask(__name__)

#register to it 注册其他模块
import views,main
```

入口文件包含模块
```
$ cat app/views.py
from . import app
# view模块
@app.route('/views')
def index():
    return "hello world"
```

入口文件包含模块
```
$ cat app/main.py
from . import app
# main模块
@app.route('/main')
def main():
    return "main"
```


RBAC（Role-Based Access Control，基于角色的访问控制）


#### 4.1.2 request和requests的关系

#### 4.1.3 python中的*arg **kwarg

*args 没有key 值，可以理解为list
**kwargs有key值的key=value



#### 4.1.4 python的logging模块





#### 4.1.5 traceback模块





#### 4.1.6 datatable 分页问题

js前端的分页




#### 4.1.7 动态加载模块的三种方法

1.系统函数 `__import__()`
```
In [3]: mystring = __import__("string")

In [4]: mystring.
mystring.Formatter        mystring.expandtabs       mystring.replace

```

2. 使用exec

In [5]: myos = "import os as myos"

In [6]: exec myos

In [7]: myos.
Display all 218 possibilities? (y or n)
myos.EX_CANTCREAT      myos.chdir             myos.nice
myos.EX_CONFIG         myos.chmod             myos.open


3. imp模块
In [8]: import imp

In [9]: stringmodule = imp.load
imp.load_compiled  imp.load_module    imp.load_source    
imp.load_dynamic   imp.load_package   

In [9]: stringmodule = imp.load_module('string', *imp.find_module('string'))

In [10]: stringmodule.
stringmodule.Formatter        stringmodule.ljust


#### 4.1.8 装饰器
抽象验证过程  api/idc.py


#### 4.1.9 异常处理类要怎么弄？

先介绍类
异常类继承Exception
继承Exception类
自定义扩展一些方法
手动raise抛出错误的时候，可以多加参数
给出更详细的错误定位


#### 4.1.10 class
http://note.youdao.com/share/web/file.html?id=01fee680a1305c1395c273a333e7f199&type=note


http://www.cnblogs.com/wupeiqi/p/4493506.html   面向对象初级
http://www.cnblogs.com/wupeiqi/p/4766801.html   面向对象进阶



### 5. 职业发展

技术vs管理
* 没有纯管理
* 业务上要突出
* 技术骨干 -> 管理者 -> 领导者


运维 -- 运维开发 -- 运维开发架构

* 运维基础 基础运维
    - Linux
    - LAMP
    - 运维基本概念
* 工具语言 掌握运维 (打扎实基础)
    - shell
    - 业务运维 把业务运维好
    - 理解工具 zabbix，puppet
        * zabbix 的CS运行机制
        * client与server的通信方式
        * zabbix 的各种用法，和适用场景
* 开发思维
    - 语言研究者
    - 优化与挑毛病
        * 优化，效率更高
        * 复用，抽象出参数
    - 设计与逻辑思维
        * 不是写大脚本
        * 代码的复用
        * 语言 != 开发
        * 解决问题的思路(算法) **核心**
* 架构平台思维
    - 工具 --> 平台
        * 平台化，打通各类工具
    - 架构研究者
        * CS架构 puppet zabbix openfic 等 c-s通信方式
        * 架构映射到不同的工具上
    - 知识的迁移
        * 监控 --> 自动部署
        * 不停的总结一些东西
            - 为什么做的好
            - 上升到方法论
* 体系开源生态 (吹牛逼能力，表达) -- 总监
    - 知识体系化 (体系化的知识面)
        * 知识足够广
        * 能够体系化
    - 深度拥抱开源
        * 知识面的来源，吸取新知识，加入自己的知识体系
        * 存储
            - 块存储
            - 文件存储
    - 技术方向感
        * CTO 方向感

学习境界

* 独上西楼
    - 具有学习的意识
    - 不要混
* 衣带渐宽终不悔
    - 培训只是一个起点
    - 保持学习的状态
* 蓦然回首那人却在灯火阑珊处
    - 厚积薄发
    - 不明白的问题，找不到答案，持续努力

语言的学习

* 词汇语法不是全部
* 词汇
* 语法
* 听力
* 口语
* 写作

语法也不是计算机语言的全部

* 词汇
* 语法
* 数据结构
* 算法
* 架构

语法和python本身不要抓着不放

解决问题的过程

* 提出问题
* 分析问题
* 设计算法
* 编写程序
* 调试程序
* 得到结果


算法

* 数据结构(C) -- 严蔚敏 (8个月以内看完二叉树之前的东西)
* 伪代码解决思路
* 二叉树
* 锻炼思维能力

实践动手能力

* 不要关注怎么写代码
* 自己要想清楚
* 关注如何告诉计算机如何做

技术选型与架构能力

* 拥抱开源
* hadoop生态

