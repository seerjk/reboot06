# Reboot Python 05

> date: 2015-11-21

## 1. 作业讲评
简单的nginx日志分析，的用途

* DDoS攻击的分析，攻击IP和流量
* 识别热点资源，上cache和CDN
* 上新资源，看它的访问量，和对原有资源的影响
* 集群日志，做实时汇聚
    - hash到某台机器
    - 均衡到某个机房，需要汇聚
    - ELK

uri

way1
[(status_code, uri, ip), count]  ==>
用list存放，查找，效率太低

way2
用dict，查找效率更高
{(ip_addr, status_code, request_url): request_times; }

ip_addr不可枚举， 来源不确定，超找需要遍历，效率低

way3
拆为两层，希望(ip, count)
{
    status_code: 
    {
        uri: (ip, count)
    }
}

拆成3层，每次都是找key，性能高很多
{
    status_code: 
    {
        uri: {ip, count}
    }
}

{
    200: 
    {
        '/data/uploads/2013/0424/14/51777eaea5036.JPG': {'42.92.56.130', 1},
        '/data/uploads/2013/0422/08/51748b0ef04e8.JPG': {'42.92.56.130', 1}
    }
}

统计过程，是对dict中的key做in判断

3重if  status_code, uri, ip

acc_dict = {}

ip = 42.92.56.130
uri = '/data/uploads/2013/0422/08/51748b0ef04e8.JPG'
status = 404

if status in acc_dict:
    if uri in acc_dict[status]:
        uri_dict = acc_dict[status]
        if ip in uri_dict:
            uri_dict[ip] += 1
        else:
            uri_dict[ip] = 1
    else:
        pass
else:
    pass

## 后续改进

减少一重for的方法
uriDcit[ip] = uriDict.get('ip',0)+1

处理为tree结构，

### 进一步提升效率
如果log很大，nG，需要做log的切割

多线程处理，并行处理

* 每个并行处理逻辑，运行同一个代码逻辑
* 最终把处理逻辑整合到一起

map-reduce

hadoop中file按块存储
多副本
namenode 索引
datanode 文件块
文件块的顺序，每块的偏移量
并行计算

#### es -- 倒排索引
https://zh.wikipedia.org/wiki/%E5%80%92%E6%8E%92%E7%B4%A2%E5%BC%95

* uri 统一资源标识符（Uniform Resource Identifier，或URI)是一个用于标识某一互联网资源名称的字符串。 

* url 统一资源定位符（或称统一資源定位器/定位地址、URL地址等，英语：Uniform / Universal Resource Locator，常缩写为URL），有时也被俗称为网页地址（網址）

1、URI是统一资源标识符，是一个用于标识某一互联网资源名称的字符串。 该种标识允许用户对任何（包括本地和互联网）的资源通过特定的协议进行交互操作。URI由包括确定语法和相关协议的方案所定义。由是三个组成部分：访问资源的命名机制、存放资源的主机名、资源自身的名称，由路径表示。
比如文件的URL，服务器方式用file表示，后面要有主机IP地址、文件的存取路径（即目录）和文件名等信息。有时可以省略目录和文件名，但“/”符号不能省略。
例：file://a:1234/b/c/d.txt代表获取资源使用ftp协议，资源目标是a主机的1234端口的b目录下的c目录下的d.txt。

2、URL是统一资源定位，是对可以从互联网上得到的资源的位置和访问方法的一种简洁的表示，是互联网上标准资源的地址。互联网上的每个文件都有一个唯一的URL，它包含的信息指出文件的位置以及浏览器应该怎么处理它。


## 1. 上节回顾——文件操作

上节课内容非常简单，主要就是几个函数

* open
* read
* readling
* readlines
* write
* writelines
* close

r+ a+ 的文件指针位置不同
r+ write 当前位置，覆盖
a+ write 末尾

write 需要加 \n
file.close() 缓存 --> disk

* 文件的模式
    - 读
    - 写
    - 追加

* 错误处理
    - try
    - except
    - else
    - finaly

捕获异常，方式程序中断，处理异常，打日志

## 3. 函数

* 咱们现在写一些小程序是没问题的
* 如果我们写的log日志分析功能，在其他地方也能用到，该肿么办
* 所以我们需要函数
    - 执行一系列语句

* 代码复用
    - 不用一直复制代码
* 更加易读
    - 通过函数来组织一个功能

和数学上函数的区别
> sin()
> 数学上函数 一定有输入输出
> 都是完成某件事情

1. 一个函数只能有1个return

```
def testFunction():
    return 1
    # 后面无效了
    print 'aaa'

def testFunction():
    if true:
        return 1
    else:
        1
        2
        3
        4
        return 0
```

定义函数

```
>>> def hello():
...     print 'hello'
...     print 'subin'
... 
>>> hello()
hello
subin
```

return 后面语句不会执行
```
>>> def hello():
...     return 'subin'
...     return 'hello'
... 
>>> hello()
'subin'
```

### 参数

*　一种输入
* 参数本身 -- 变量
* 形参 -- 函数声明
* 实参 -- 函数调用

```
>>> a = 'subin'
>>> def changeName(name):   // name = a
...     name = 'woniu'      // name = 'woniu' 不影响a
...     print name
... 
 
>>> id(a)
140678429775696
>>> a
'subin'
>>> 
>>> changeName(a)
woniu
>>> id(a)
140678429775696
>>> a
'subin'
```

值传递，过程分析
```
>>> a = 'subin'
>>> name = a
>>> id(name)
140678429775696
>>> id(a)
140678429775696
>>> name = 'woniu'
>>> id(name)
140678429788224
>>> name
'woniu'
>>> a
'subin'
```

参数为list，是引用

```
>>> b = ['subin', 'wd']
>>> def changeName(name_list):   // name_list = b
...     name_list[0] = 'woniu'
...     print name_list
... 
>>> print b
['subin', 'wd']
>>> changeName(b)
['woniu', 'wd']
>>> print b
['woniu', 'wd']
```

list，dict直接作为形参，相当于引用，函数外面的操作影响了原本变量值。

引用传递，过程分析如下：

```
>>> a = ['subin', 'wd']
>>> name = a
>>> id(name)
140678429085352
>>> id(a)
140678429085352
>>> 
>>> name[0] = 'woniu'
>>> id(name)
140678429085352
>>> id(a)
140678429085352
>>> 
>>> name
['woniu', 'wd']
>>> a
['woniu', 'wd']
```

另外一个，
```
>>> a = ['subin', 'wd']
>>> def change(name):
...     name = []
...     name[0] = 'woniu'
...     print name
... 
>>> a
['subin', 'wd']
>>> change(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in change
IndexError: list assignment index out of range
```

chang函数中做copy

```
>>> def change(name):
...     name_copy = name[:]
...     name_copy[0] = 'woniu'
...     print name_copy
... 
>>> a = ['subin', 'wd']
>>> id(a)
140678429089520
>>> a
['subin', 'wd']
>>> change(a)
['woniu', 'wd']
>>> a
['subin', 'wd']
```


传参数，注意位置，顺序，参数个数

```
def hello(name, age):
    print name
    print age

hello('subin', 20)
hello(20, 'subin')
```

位置参数，位置参数很多的时候，容易把顺序弄乱

```
def hello_world(name, word):
    print "%s, %s" % (name, word)

hello_world('wd', 'hello')

def hello_world(word, name):
    print "%s, %s" % (name, word)

hello_world('wd', 'hello')
```

### 关键字参数

忽略位置参数，指定参数关键字
python 的好特性

相当于在传参数的时候就已经进行了赋值

```
def hello(name, age):
    print name
    print age

hello(age = 2, name = 'subin')
hello(name = 'subin', age = 2)
```

### 形参的默认值
```
def hello(name = 'subin', age = 20):
    print name
    print age

hello('subin', 30)
hello(30, 'subin')
hello('wd')

hello(name = 'wd')
hello(age = 20, name = 'subin')
hello()
```

1. 只给一个默认值？
2. 只给一个默认值，关键字的顺序？

```
# def hello(name = 'subin', age):
#     print name
#     print age
# SyntaxError: non-default argument follows default argument
# 如果def hello(name = 'subin', age): 方式是可行的：
# hello(subin)  这样就有问题，传给name或者age无法确定
# 给name，是位置参数
# 给age，和位置参数矛盾

def hello(name , age = 20):
    print name
    print age

hello('subin')

# hello(age = 20)
# TypeError: hello() takes at least 1 argument (1 given)
```

* 位置参数一定要在关键字参数之前
* 位置参数，注意顺序
* 关键字参数，不管顺序
* 先按照位置赋值，再按照关键字赋值
* 不论声明函数，还是调用函数，关键字参数一定要放在位置参数之后
* 关键字参数与位置无关

* 实参 个数要与形参一直，默认值
* 不论声明函数，还是调用函数，关键字参数一定要放在位置参数之后，中间不能互相掺杂
* 关键字参数与位置无关

```
def hello(name , age = 20):
    print name
    print age

hello(age = 30, 'subin')
# SyntaxError: non-keyword arg after keyword arg
hello('subin', age = 30)
# 可行
```

```
# def hello(name , age = 20, sex):
# SyntaxError: non-default argument follows default argument
def hello(name , age = 20, sex = 'male'):
    print name
    print age
    print sex

hello('subin', 20, 'mail')
hello('subin', 'mail', 20)
hello('subin', sex = 'mail', age = 20)
hello('subin', age = 20)
hello('subin', sex = 'mail')
hello('subin')
```

函数自身当成变量

* 函数内部可以调用函数，调用之前需要先定义

* 函数内部不能定义函数，函数不要嵌套定义

* 函数当做形式参数

```
# arg: function name
def hello3():
    return 'subinggg'

def hello(function):
    return function()

print hello(hello3)
```

## 3. 特殊函数
### 3.1 递归函数

* 函数自己调用自己
* 防止死循环，要有结束条件
* 树的遍历，一定要递归


### 3.2 map函数(映射)
map(function, sequence)
统计单词，做单词计数

I am subin
i, 1
a, 1
m, 1
s, 1
u, 1
b, 1
i, 1
n, 1


### 3.3 reduce


### 3.4 filter

filter(function, sequence)
function 返回必须是bool
用于过滤


### 3.5 lambda 匿名函数

* 不能很复杂
* 很灵活
* 一行代码搞定的事情

lambda <参数>:函数体

* 隐函数，定义一些简单的操作

```
map(lambda x: x**2, [1,2,3])
```

### 3.6 列表推到式

生成序列
兼顾了filter
兼顾了lambda
兼顾了sequence

[expression for item in sequence]

```
>>> a = [1, 2, 3, 4, 5]
>>> [i**2 for i in a if i%2 == 1]
[1, 9, 25]

>>> [i**2 for i in [1,2,3,4,5] if i%2 == 1]
[1, 9, 25]

>>> [i**2 for i in range(1,6) if i%2 == 1]
[1, 9, 25]
```

## 作业1
* 一个list[(1,4),(5,1),(2,3)],根据每个元组中的较大值进行排序
    - 期待结果：[(2,3),(1,4),(5,1)]
    - 要求：用sorted和lambda完成
    - 级别1：用lambda中用max
    - 级别2：lambda中不用max
    - 提示：True乘以4 ==4 Fale乘以2 == 0

```
print True*4
print False*4
```

* 用函数，优化log分析的功能
* 实现加减乘除功能的函数
    - 级别1 不支持优先级
    - 级别2 支持优先级，但是没有括号
    - def operate(str):
    - operate('1+2+3-5') == 1