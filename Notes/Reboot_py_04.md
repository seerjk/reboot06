# Reboot Python 04
> date: 2015-11-14

## 1. 上节回顾
* 元组
    - 不可变
    - 可枚举
    - 操作 count, index
* 按值和按索引取值的区别
* 字典的定义
* 字典的特点：没顺序，查找快，key不重复。。。
* 遍历字典
    - key
    - items -- k,v
* 通用方法 len del for in
* in 判断元素，get 空值&空
* 更新字典
* 字典方法:clear,copy,formkeys,get,popitem
    - dict.popitem() 随机的
* 引用和复制

```
>>> a = {}
>>> b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'b' is not defined
>>> b = a
>>> b
{}
>>> b['name'] = "subin"
>>> a
{'name': 'subin'}
>>> b
{'name': 'subin'}
```

b 被a覆盖
```
>>> a = {}
>>> b = {}
>>> b = a
>>> id(a)
140053414546240
>>> id(b)
140053414546240
```

复制
```
>>> a = {}
>>> b = a.copy()
>>> id(a)
140053414547080
>>> id(b)
140053414545960
```

### 上节回顾---String
* 字符列表，不可变，list的查看方法，字符元组
* 字符串的定义，取字符
* 切片
* str.join()   '|'.join(['hello','world']) 创造新对象

对list和tuple对可以join --> str
```
>>> ":".join(['woniu', 'wd', 'subin'])
'woniu:wd:subin'
>>> ":".join(('woniu', 'wd', 'subin'))
'woniu:wd:subin'
```

* str.find()
* str.index()
* str.capitalize()  upper()  lower()
* str.replace()  先查找，找到才替换，找不到无变化
* str.split()
* 热身：通过多个字符分隔
* 热身：数据替换，分隔符{}

### 作业分析

可以考虑把key根据value排序后，单独放到一个list中。

## 2. 文件操作

### 2.1

打开文件 open
读文件 read readline readlines
写文件 write
关闭文件 close

### 2.2 文件的模式

如果想修改文件内容，需要提供文件的模式

* 读（默认值） ： r
* 写 ： w   全量写
* 追加： a  增量写
* + r+ w+

相对路径打开
```
>>> f = open('hello.py')
>>> f.read()
'hello\nworld\n'
```

绝对路径打开
```
>>> f = open('/home/jiangk/reboot06/04/hello.py')
>>> f.read()
'hello\nworld\n'
```

### 2.2 读取

```
>>> f = open('hello.py')
>>> print f.read()
hello
world

>>> 
```

按字符读
-1 全读出，无意义
0 不读

```
>>> f = open('hello.py')
>>> f.read(1)
'h'
>>> f.read(2)
'el'

>>> f = open('hello.py', 'r')
>>> f.read(-1)
'hello\nworld\n'

>>> f = open('hello.py', 'r')
>>> f.read(0)
''
```

按行读 readline()

```
>>> f = open('hello.py')
>>> print f.readline()
hello

>>> print f.readline()
world

>>> print f.readline()
```

加参数的readline 退化为read()

* readline() 不建议加参数

```
>>> f = open('hello.py')
>>> print f.readline(2)
he
>>> print f.readline(3)
llo
```

readlines()

* 用于遍历
* 返回的是list

```
>>> f = open('hello.py')
>>> print f.readlines()
['hello\n', 'world\n']
```

遍历

```
>>> f = open('hello.py')
>>> lines = f.readlines()
>>> for line in lines:
...     print line
... 
hello

world

```


```
>>> a = None
>>> b = ""
>>> a
>>> b
''
```

### 2.3 写操作

直接覆盖，文件内容清空，
```
>>> f = open('hello.py', 'w')
>>> 
```

w 不存在的文件，直接创建
```
>>> f = open('hello1.py')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IOError: [Errno 2] No such file or directory: 'hello1.py'
>>> f = open('hello1.py', 'w')
>>> f = open('hello2.py', 'w')
```


```
jiangk@dev:~/reboot06/04$ ll
total 48
drwxrwxr-x 2 jiangk jiangk  4096 Nov 14 11:35 ./
drwxrwxr-x 9 jiangk jiangk  4096 Nov 14 10:43 ../
-rw-rw-r-- 1 jiangk jiangk     0 Nov 14 11:34 hello1.py
-rw-rw-r-- 1 jiangk jiangk     0 Nov 14 11:35 hello2.py
-rw-rw-r-- 1 jiangk jiangk    12 Nov 14 11:34 hello.py
-rw-r--r-- 1 jiangk jiangk 34776 Nov 14 10:59 libisccc.so.90
```

w的行为：

* 存在，清空
* 不存在，创建


file.write()

* 无返回值
* \n 需要自己加上，默认不换行
* 没有writeline()
* writelines() 列表，但是 \n 还是要自己加上
* 先写内存，不close，一般不flush写入disk（还看buffer大小）
    - 定期flush写disk
    - 强制flush写入disk，close()

```
>>> f = open('hello.py', 'w')
>>> f.write('hello\n')
>>> a = f.write('hello\n')
>>> print a
None
```

file.close()

* 操作完file, 记得要close()
* 文件对象的释放


close 后 文件对象还存在
```
>>> f = open('hello.py')
>>> id(f)
140584389326144
>>> f.read()
'hello\nsubin'
>>> f.close()
>>> print f
<closed file 'hello.py', mode 'r' at 0x7fdc5a963540>
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file
```

writelines()

```
>>> f = open('hello.py')
>>> print f.readlines()
['hello\n', 'subin']
>>> f.close()
>>> 

>>> f = open('hello.py', 'w')
>>> content_list = ['hello\n', 'subin']
>>> f.writelines(content_list)
>>> f.writelines(content_list)
>>> f.close()

>>> f = open('hello.py')
>>> print f.readlines()
['hello\n', 'subinhello\n', 'subin']
```

* r 读模式 只能read
* w 写模式 只能write

```
>>> f = open('hello.py')
>>> f.read()
'hello\nsubin\n'
>>> f.write('haha')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IOError: File not open for writing

>>> f = open('hello.py', 'w')
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IOError: File not open for reading

>>> f.write('hahaha')
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IOError: File not open for reading
>>> print f
<open file 'hello.py', mode 'w' at 0x7fdc590cc270>
```


* 不close，写大型代码，等坑呢
* 打开文件 后续都可以用with，就不用手动关闭了
* 文件里有空值  就不能这样判断结束么   while f.read():

#### a 追加模式
* 存在，则追加，不清空
* 不存在，创建
* 在文件末尾追加
* a 追加模式是一种写模式，不能read()

```
>>> f = open('hello.py', 'r')
>>> f.read()
'hahaha'
>>> f = open('hello.py', 'a')
>>> f.write('subin')
>>> f.close()
>>> 
>>> f = open('hello.py', 'r')
>>> f.read()
'hahahasubin'
```

```
>>> f = open('hello.py', 'a')
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IOError: File not open for reading
```

#### + 加模式

```
>>> f = open('hello.py')
>>> print f.read()
hello
subin

>>> f = open('hello.py', '+')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: mode string must begin with one of 'r', 'w', 'a' or 'U', not '+'
```

```
>>> f = open('hello.py', 'r+')
>>> f.read()
'hello\nsubin'
>>> f.write('\nI am wd')
>>> f.close()

>>> f = open('hello.py', 'r+')
>>> print f.read()
hello
subin
I am wd
```

不提倡 w+ 打开文件，会清空文件

```
>>> f = open('hello.py', 'w+')
>>> f.read()
''
>>> f.write('hello\n')
>>> f.read()
''
>>> f.close()

jiangk@dev:~/reboot06/04$ cat hello.py 
hello
```

a+
```
>>> f = open('hello.py', 'r')
>>> print f.read()
hello

>>> f = open('hello.py', 'a+')
>>> print f.read()
hello

>>>
```

## 4. 文件指针

文件打开时，文件指针指向文件首
文件的读写，永远从文件指针的下一个位置开始

a+ 向文件末尾写，不清空文件  ar == ra
r+ 从文件开头写，不清空文件  rw
w+ 先用w特性，清空文件       wr

> rw == r+
> wr == w+
> 能不能这样理解？

文件指针当前所处的位置，即当前读取点距离文件头位置的偏移量。

```
>>> f = open('hello.py', 'r+')
>>> f.read()
'hello\nsubin\n haha'

>>> f = open('hello.py', 'r+')
>>> f.write('haha')
>>> f.read()
'o\nsubin\n haha'
```

rw  wr
```
>>> f = open('hello.py', 'rw')
>>> f.close()
>>> f = open('hello.py', 'r')
>>> f.read()
'hello\n'
>>> f = open('hello.py', 'wr')
>>> f = open('hello.py', 'r')
>>> f.read()
''
```

file.tell()
```
>>> f = open('hello.py', 'r+')
>>> f.tell()
0
>>> f.read()
'hahao\nsubin\n haha'
>>> f.read()
''
>>> f = open('hello.py', 'r+')
>>> print f.read()
hello
subin
 haha

>>> f.tell()
18
>>> f = open('hello.py', 'r+')
>>> f_str = f.read()
>>> len(f_str)
18

```


>>> f = open('hello.py')
>>> f.read()
'hahao\nsubin\n haha\n\n\n\na'
>>> 
>>> 
>>> f = open('hello.py', 'a+')
>>> f.tell()
0
>>> f.write('aaa')
>>> f.tell()
3  ### 这个应该是在末尾，2.7.6 有bug，升级到2.7.10

a+ 写后，都会放到末尾


file.seek()

```
>>> f = open('hello.py', 'r+')
>>> print f.read()
hahao
subin
haha

>>> f.tell()
17
>>> f.read()
''
>>> f.seek(0)
>>> f.tell()
0
>>> f.read()
'hahao\nsubin\nhaha\n'
>>> f.seek(0)
>>> f.read(1)
'h'
>>> f.tell()
1
>>> f.read(1)
'a'
>>> f.seek(5)
>>> f.read()
'\nsubin\nhaha\n'
>>> f.seek(5)
>>> f.read(1)
'\n'
```

seek  a+ 注意写的问题

```
>>> f = open('hello.py', 'a+')
>>> f.read()
'hahao\nsubin\nhaha\n'
>>> f.write('\nhaha')
>>> f.read()
''
>>> f.seek(0)
>>> f.read()
'hahao\nsubin\nhaha\n\nhaha'
>>> f.seek(5)
>>> f.read()
'\nsubin\nhaha\n\nhaha'


>>> f = open('hello.py', 'r+')
>>> f.seek(0)
>>> f.read()
'hahao\nsubin\nhaha\n\nhaha'
>>> f.seek(6)
>>> f.write('woniu')
>>> f.tell()
11
>>> f.read()
'\nhaha\n\nhaha'
>>> f.seek(0)
>>> print f.read()
hahao
woniu
haha

haha
>>>
```

a+ 中 seek() write() 也是末尾追加

* write()前先判断，文件打开方式
    - a  a+ 文件指针都先移动到末尾，seek可以实现任意位置读
    - r+   当前文件指针的位置写，可以在文件任意位置写入

```
>>> f = open('hello.py', 'a+')
>>> f.tell()
0
>>> f.read()
'hahao\nwoniu\nhaha\n\nhaha'
>>> f.tell()
22
>>> 
>>> f.seek(5)
>>> f.read()
'\nwoniu\nhaha\n\nhaha'
>>> 
>>> f.tell()
22
>>> f.seek(5)
>>> f.seek(6)
>>> f.write('subin')
>>> 
>>> f.tell()
11
>>> f.read()
''
>>> f.seek(0)
>>> f.read()
'hahao\nwoniu\nhaha\n\nhahasubin'
```

* 要知道 文件指针的位置，seek() 移动文件指针的位置
* 要知道 写几个字符，可能会覆盖，可能会追加


seek(n)  n 大于文件长度，会补x00

```
>>> f = open('hello.py', 'r+')
>>> f.read()
'hahao\nwoniu\nhaha\n'
>>> f.tell()
17
>>> f.seek(22)
>>> f.read()
''
>>> f.tell()
22
>>> f.write('subin')
>>> f.seek(22)
>>> f.write('subin\n')
>>> f.tell()
28
>>> f.seek(0)
>>> f.read()
'hahao\nwoniu\nhaha\n\x00\x00\x00\x00\x00subin\n'
>>> f.seek(0)
>>> print f.read()
hahao
woniu
haha
subin

>>> f.tell()
28

>>> f.seek(17)
>>> f.write('hello')
>>> f.seek(0)
>>> f.read
<built-in method read of file object at 0x7fb756b6c540>
>>> f.read()
'hahao\nwoniu\nhaha\nhellosubin\n'
```

a+
seek()移动会生效
seek 对读有效

```
>>> f.write('haha')
>>> f.read()
''
>>> f.tell()
32
```

## 5. 捕获异常
try...except...else...finally

```
try:
  可能出错的代码
except:
  如果出错 必须
else:
  如果不出错 非必须
finaly:
  出不出错都执行 非必须
```

```
>>> try:
...   f = open('ss')
... except:
...   print 'not exist'
... else:
...   print f.read()
... finally:
...   print 'always'
... 
not exist
always
```

```
>>> try:
...   f = open('hello.py')
... else:
...   print f.read()
... except:
...   print 'not exist'
... finally:
...   print 'always'
... 
hahao
woniu
haha
hellosubin
hahajiangk
always
```


## 总结
* 三种模式 r w a
* 不用w+
* a+ 只要write()  会跑到最后
* seek() 移动文件指针
* r+ 



1. open默认以读模式打开，并且我们打开的，一定是个存在的文件，否则会报错。而这个文件，可以是相对路径，也可以是绝对路径

2. 但是我们以写模式打开的时候，如果这个文件不存在，则创建，这里面不会报错

3. 文件指针的问题

4. readline()和readliens()是不用加参数的，不是我们期望的读取几行的结果

5. read函数参数的问题：负数和没有参数是一样的效果

6. close不是必须的，但是我们操作完一个文件的时候尽量去close它

7. 可以用+模式解决既可以读，又可以写的问题

8. read模式可以用readline和readliens读一行和读多行，但是write模式只写一行，用writelines()

9. 在a+模式下，文件指针对写不起作用（一定是在追加），但是对读起作用。注意这里和r+的区别

10. tell()函数返回当前文件指针的位置

11. seek()函数将文件指针移动到指定的位置，如果查找的位置超出了文件的长度，这个时候，仍然是将文件指针指到指定的位置，对于读，相当于是放到了文件末尾，但是写，会补充相应个数的0值，然后在指定的位置写入。如果是负值，则会报参数错误（也就是参数的取值范围是自然数）。

12. 在r+模式下，seek可以实现从指定位置修改一个文件

13. 在a+模式下，不管怎么移动文件指针，对写都不起作用，写一定还是在文件末尾追加，但是可以通过seek去实现从任意位置的读

14. truncate函数按照指定的大小截断源文件



## 作业

http://51reboot.sinaapp.com/publish/04.htm#20

简单的nginx日志分析
日志文件在/home/shre/www_access_20140823.log
期望输出一个list，分别存储这http状态，访问url，ip，访问次数，如下图

可以优化的地方
http://segmentfault.com/a/1190000002727070

### 大文件读取的方式

如果知道偏移（offset）和长度（limit, size）的话，可以在open文件后用fp.seek(offset[, whence])来定位偏移。fp.read([size])可以给出可选参数size来指定读取字节的长度。

如果不知道偏移和长度的话，`fp.readlines([size])`也不是一个好方法。`readlines()`同样会把所有行都载入内存，而`xreadlines()`却会产生一个迭代器，通过惰性方式来读取。

但是，从python2.3开始，`xreadlines()`作为一项方法已经被废弃（deprecated），转而推荐使用更加pythonic的写法：

```python
for line in fp:
    do_something_with(line)
```

`for line in f`p的方式是和`xreadlines()`完全等效的。

此外，对于初学者而言，打开大量文件不关闭文件句柄是一个常见的毛病。这在写小程序时没啥问题，但一旦程序变大、功能加强后，可能就会出现资源不够用的情况。所以，一般推荐用with context来打开文件：

```python
from __future__ import with_statement

with open('/path/to/file', 'rb') as fp:
    for line in fp:
        do_something_with(line)
```