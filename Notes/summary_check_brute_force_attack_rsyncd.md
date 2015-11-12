# check_brute_force_attack_rsyncd的一些python总结

> auhtor: JiangKun
> date: 2015-11-3
> tag: python, python2.4, python2.7

## 1. main 主过程

```python
if __name__ == '__main__':
    # main process
    # 程序的主过程写在这里
```

## 2. file操作

### 2.1 安全打开文件

文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的。必须最后要调用 f.close()`关闭文件。

由于文件读写时都有可能产生`IOError`，一旦出错，后面的`f.close()`就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用`try ... finally`来实现

```python
f = open('ab.txt','r')
try:
    print f.read()
finally:
    if f:
    # if f is not None:
        f.close()
```

Python引入了`with`语句来自动帮我们调用`close()`方法：

```python
try:
    with open('ab.txt','r') as f:
        print f.read()
except IOError as err:
        print "File Error: %s" % (str(err))
```

### 2.2 文件的读操作 read(), readline(), readlines()

调用`read()`会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用`read(size)`方法，每次最多读取size个字节的内容。

另外，调用`readline()`可以每次读取一行内容，调用`readlines()`一次读取所有内容并按行返回`list`。因此，要根据需要决定怎么调用。

* 如果文件很小，`read()`一次性读取最方便
* 如果不能确定文件大小，反复调用`read(size)`比较保险
* 如果是配置文件，调用`readlines()`最方便

使用`readlines()`并去除空行：

```python
for line in f.readlines():
    print(line.strip()) 
    # 把末尾的'\n'删掉
```

#### 几种按行读文件的方法比较
##### (1. 最基本的读文件方法：

```python
# File: readline-example-1.py
 
file = open("sample.txt")
 
while 1:
    line = file.readline()
    if not line:
        break
    pass # do something
```

一行一行得从文件读数据，显然比较慢；不过很省内存。

在我的机器上读10M的sample.txt文件，每秒大约读32000行


##### (2. 用fileinput模块

```python
# File: readline-example-2.py
 
import fileinput
 
for line in fileinput.input("sample.txt"):
    pass
```

写法简单一些，不过测试以后发现每秒只能读13000行数据，效率比上一种方法慢了两倍多……

##### (3. 带缓存的文件读取

```python
# File: readline-example-3.py
 
file = open("sample.txt")
 
while 1:
    lines = file.readlines(100000)
    if not lines:
        break
    for line in lines:
        pass # do something
```

这个方法真的更好吗？事实证明，用同样的数据测试，它每秒可以读96900行数据！效率是第一种方法的3倍，第二种方法的7倍！

##### (4. 在Python 2.2以后，我们可以直接对一个file对象使用for循环读每行数据：

```python
# File: readline-example-5.py
 
file = open("sample.txt")
 
for line in file:
    pass # do something
```

##### (5. 而在Python 2.1里，你只能用xreadlines迭代器来实现：

```python
# File: readline-example-4.py
 
file = open("sample.txt")
 
for line in file.xreadlines():
    pass # do something
```


## 3. time和datetime模块

http://www.runoob.com/python/att-time-strptime.html
http://www.wklken.me/posts/2015/03/03/python-base-datetime.html
http://wangwei007.blog.51cto.com/68019/1102130


## 4. str 字符串操作
### 4.1 字符串分割 split()
split(...)
> S.split([sep [,maxsplit]]) -> list of strings
> Return a list of the words in the string S, using sep as the delimiter string.  If maxsplit is given, at most maxsplit splits are done. If sep is not specified or is None, any whitespace string is a separator and empty strings are removed from the result.



### 4.2 str 和 list 转换

str和list互相转换
方法1,join()和split()

```python
num_list = ['1','2','3','4']

# list --> str
num_str = ','.join(num_list)
print num_str

# str --> list
num_list2 = num_str.split(',')
print num_list2
```

方法2，

```python
# list(int) --> str
list_of_ints = range(10000)

txt_str = ','.join(str(x) for x in list_of_ints)

# str --> list(int)
txt_str = '1,2,3,4,5,6,7,8,9,10'
list2 = [int(i) for i in txt.split(',')]

# str --> list(str)
list2 = [i for i in txt.split(',')]
list2 = [str(i) for i in txt.split(',')]
```


方法3，map()

```python
txt = '1,2,3,4,5,6,7,8,9,10'
list3 = map(int,txt.split(','))
```

## 4.3 计算代码执行时间

```python
from time import clock as now

time_start = now()

# 执行的代码

time_stop = now()

print "Running: %d s" % (time_stop - time_start)
```


## 5. dict 字典的操作
### 5.1 遍历dict

遍历字典的几种方法

```python
#!/usr/bin/python 
dict={"a":"apple","b":"banana","o":"orange"} 

print "##########dict######################" 
for i in dict: 
        print "dict[%s]=" % i,dict[i] 

print "###########items#####################" 
for (k,v) in  dict.items(): 
        print "dict[%s]=" % k,v 

print "###########iteritems#################" 
for k,v in dict.iteritems(): 
        print "dict[%s]=" % k,v 

print "###########iterkeys,itervalues#######" 
for k,v in zip(dict.iterkeys(),dict.itervalues()): 
        print "dict[%s]=" % k,v 
```


### 5.2 修改

向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:

```python
std_dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# update existing entry 修改已经存在的entry
std_dict['Age'] = 8

# Add new entry 增加新的 entry
std_dict['School'] = "DPS School"

print "std_dict['Age']: ", std_dict['Age']
print "std_dict['School']: ", std_dict['School']
```

### 5.3 删除

字典值可以没有限制地取任何python对象，既可以是标准的对象，也可以是用户定义的，但键不行。

两个重要的点需要记住：

* 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住

* 2）键必须不可变，所以可以用数，字符串或元组充当，所以用列表就不行


## 6. list 

### 6.1 把list中str类型的item变为int类型item
In python, I want to convert all strings in a list to ints.

So if I have:

results = ['1', '2', '3']

How do I make it:

results = [1, 2, 3]

方法1

```python
results = [int(i) for i in results]
```

方法2

```python
results = map(int, results)
```


## 7. 适配python 2.4
### 7.1 datetime中的strptime()方法适配

```
import datetime, time
dt_date = datetime.datetime(*(time.strptime(date_string, format)[0:6]))
```

同时适配2.4和2.6的方法：

Based on Daniel's answer, this works for me when you're not sure under which Python version (2.4 vs 2.6) the script will be running:

```
from datetime import datetime
import time

if hasattr(datetime, 'strptime'):
    #python 2.6
    strptime = datetime.strptime
else:
    #python 2.4 equivalent
    strptime = lambda date_string, format: datetime(*(time.strptime(date_string, format)[0:6]))

print strptime("2011-08-28 13:10:00", '%Y-%m-%d %H:%M:%S')
```


### 7.2 file 的安全打开方式

python 2.4 中没有`with`语句，只能使用`try...finally...`的方式。

```python
f = open('ab.txt','r')
try:
    print f.read()
finally:
    if f:
        f.close()
```


## 8. 报错解决
### 8.1 TypeError: 'module' object is not callable 原因分析

> 原因分析：
Python导入模块的方法有两种：import module 和 from module import，区别是前者所有导入的东西使用时需加上模块名的限定，而后者不要。

源代码如下：

```python
import  urlparse
urlparse( 'http://www.cwi.nl:80/%7Eguido/Python.html')
```

报错如下：

```python
Traceback (most recent call last):
File  "my.py" , line  3 ,  in  ?
urlparse( 'http://www.cwi.nl:80/%7Eguido/Python.html')
TypeError:  'module'  object is   not  callable
```

"TypeError: 'module' object is not callable"这个信息是说你试图把`urlparse`这个模块作为一个函数来调用，但它却无法调用。

`urlparse`这个模块包含`urlparse`和`urlsplit`等函数。我把`urlsplit`也拖了进来，它的名字和模块名不同。这个可能能帮助你发现问题。以下是调用它们的两种方法。

解决方法1：
```python
>>>  import  urlparse
>>> urlparse.urlparse( 'http://www.cwi.nl:80/%7Eguido/Python.html')
( 'http' ,  'www.cwi.nl:80' ,  '/%7Eguido/Python.html',  '' ,  '' ,  '' )
>>> urlparse.urlsplit( 'http://www.cwi.nl:80/%7Eguido/Python.html')
( 'http' ,  'www.cwi.nl:80' ,  '/%7Eguido/Python.html',  '' ,  '' )
>>>
```

解决方法2：
```python
>>>  from  urlparse  import  urlparse, urlsplit
>>> urlparse( 'http://www.cwi.nl:80/%7Eguido/Python.html')
( 'http' ,  'www.cwi.nl:80' ,  '/%7Eguido/Python.html',  '' ,  '' ,  '' )
>>> urlsplit( 'http://www.cwi.nl:80/%7Eguido/Python.html')
( 'http' ,  'www.cwi.nl:80' ,  '/%7Eguido/Python.html',  '' ,  '' )
>>>
```





