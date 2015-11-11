# Reboot Python 01
> date: 2015-10-25


关键参数需要判断，再使用。

Git
提交作业用github

脚本vs平台
哪些参数可以动态提取，作为输入

云中 运维开发是核心。

运维老王 -- 互联网杂谈

@雪糕
@Ada
体会 @蜗牛的方法和思维

重点不是python语法

* python语法的学习，用python解决实际问题
* 学到方法论，解决问题的思维方法。化繁为简

平等+简单

编程是什么东西？
编程怎么来学？

> 不推荐买书
> 看网上简明的教程
> 编程用于解决实际问题
> 配合实际代码，做实际项目


## 语言对比

php web后端
python dropbox，知乎，豆瓣，成熟的案例和应用
js 操作前端的语言，操作浏览器


## 为什么学Pyhton

我们需要的语言是什么样的？

* 上手简单
* 功能健全
* 语言生态系统完善，第三方库多
* 有大公司成功的案例

## 实战课程目标

* python的基础，掌握基本的编程思想，具体两个任务

* access_log日式处理
    - url，ip，访问状态维度，统计访问次数
    - 排序，打印出访问次数最多的前10

* 简单的cmdb
    - 基于flask
    - 数据库mysql
    - 前端jquery+bootstrap
    - 简单粗暴的完成最简单的增删改查

* 上线系统


## 入门学习编程的方法

* 慢一点 多理解
* 多练习，记笔记，纸上写伪代码
* 把编程当作工具，去解决问题，编程是手段，不是目的
* 碰到问题google baidu
* 申请github账号，加入开源社区

## 版本选择 
python 2.7


```python
#!/usr/bin/env python
print 'hello world'
print 4+5 

name = "jiangk"
print name
```

数据结构
bool
str
num

tunple
list
dict

输入`raw_input()` 更适合学习
`input()`必须输入完整的python数据 字符串要带引号

编码：写中文
#coding=utf-8


```python
age = raw_input('input your age: ')
print age
```

* 注释 #
* 缩进来控制代码块

四则运算
```
>>> 1/2
0
>>> 1.0/2
0.5

>>> 10%3
1
>>> 10/3
3
>>> 10/3.0
3.3333333333333335
```

## string
'  不可以包含 '
"  可以包含 '
'''  适合写文档

```
print 'I'm a person'

print "I'm a person"

print '''
"adf ' adf'adf'adf
adf;''
'''

```

## bool类型
True
False
首字母大写


## if
if可以嵌套多层 (多层缩进)
```python
#!/usr/bin/env python

x = raw_input('please enter your name: ')
y = raw_input('please enter your age: ')

if x == 'WD':
    if y == '20':
        print 'nani'
    elif y == '10':
        print 'interesting'
    else:
        print 'I don"n know'
else:
    print 'not an age'
```


## while

```python
i = 0
while i < 20:
    print i
    i = i + 1

print 'end'
```

**str list 和 dict处理的水平，觉得了python的水平**


变量命名 用有意义的单词

> 优化 exec07 -teach
两个条件放到一起。

key in dict
key in dict.keys()
这两个写法应该是等同的吗？

狂奔的~蜗牛~~(316783812)  17:08:29
效果是等同，但是第一个就OK
dict.keys是吧key搞成了一个list

狂奔的~蜗牛~~(316783812)  17:08:45
然后key in list

>>> type(dict.keys())
<type 'list'>
>>> type(dict)
<type 'dict'>


dict查找很快
list查找很慢

# 课程介绍
* git and github

* 前端
    - html
    - css
        - bootstrap
    - javascript
        - jQuery
    - 异步请求和flask监听的端口交互，没有直接操作数据库的权限。

* python 数据处理，和各个接口的交互
    - flask 模块：监听端口 + 渲染页面

* 数据库 mysql
    sql 语句，存储数据，mysql链接数据库操作




