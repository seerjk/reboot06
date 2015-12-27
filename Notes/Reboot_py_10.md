# note 10

> date: 2015-12-26

## 1. 作业
    bug 作业里的问题
    
    关于：datetime时间的json转换
    json转换，也是转成json规定的时间格式
    其实用timestmp最靠谱

json
    数据交换格式
    {"name":"123"}
    []
    [[1, "reboot server", 4, "2016-10-01"]]

    $.get 和 $.getJSON的区别
        getJSON 多了一步获取JSON

理解JSON

python端
```
>>> import json
>>> a = {'a':1, 'b':2}
>>> a
{'a': 1, 'b': 2}
>>> json.dumps(a)
'{"a": 1, "b": 2}'
>>> a = {'a':1, 'b':2, 'c':[123]}
>>> json.dumps(a)
'{"a": 1, "c": [123], "b": 2}'
```

web chrome console
```
> '{"a": 1, "c": [123], "b": 2}'
< "{"a": 1, "c": [123], "b": 2}"

> JSON.parse('{"a": 1, "c": [123], "b": 2}')
< Object {a: 1, c: Array[1], b: 2}
```



## 2. 类
    面向过程
    面向对象开发

## 3. 函数式编程


## 4. 作业

### 1
课上练习加上删除功能（有余力的加上更新功能）
    完成 删除和更新操作。
    增加 错误处理
    学习 ORM flask sql achemy
登录

### 2
class小游戏，加入护甲，闪避的概率，和暴击的概率
    cat 闪避的概率 10% 护甲1
    dog 狗皮比较厚 护甲是3
    rat 奶妈 的护甲是 2

作业一定要做啊！！！

import random
print random.random()


装备基类+加4个派生类

装备有暴击概率，给基类中加上穿装备的函数。

add操作，增加装备

至少四个装备类（暴击）
    铠甲
    头盔
    鞋子
    闪避

还有武器+攻击和暴击



## 5.
ipython
直接用shell 命令
支持tab案件
? 看文档
?random.random


orm就用sqlalchemy

多线程 theading
多进程


二叉树

class Tree():
    self.value
    self.left
    self.right


如何制定python代码在运行的cpu的绑定的内存片（NUMA node）上运行。
指定

@PC 大大



开发一个app，从数据库，到web，到手机端大概过程能介绍一下么
蜗牛-51reboot(316783812)  18:06:07
主要接口一定要设计好
设计成带token的
api上做验证
宋翔(200853956)  18:06:57
看过雪峰写的，看着迷糊
蜗牛-51reboot(316783812)  18:07:00
@宋翔 
https://github.com/shengxinjing/My-Script/tree/master/flask-demo/token
这个代码你仔细看下
api设计
api一定要设计好
各个端都是通过api沟通
掉数据
身份认证要做好
你可以去听一下自动化班第一天的课，讲api设计的
蜗牛-51reboot(316783812)  18:08:19
最终所有的端，都是通过api获取数据 展示