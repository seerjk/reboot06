# Reboot Python 03
> date: 2015-11-7



## 1. 上节回顾---List
定义一个List
通过索引取值
可遍历
成员是否存在
求长度，最大值，最小值

max
min
len

删除元素
del 

修改值和切片

切片批量赋值

>>> a[3:] = 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only assign an iterable
>>> a[3:3] = 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only assign an iterable
>>> a[3:4] = 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only assign an iterable
>>> a[2:3] = 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only assign an iterable
>>> a[3:] = [4]
>>> a

列表的方法
append
count
index
extend
insert
pop
reverse
sort

## 2. tuple

>>> len(b)
4
>>> max(b)
4
>>> min(b)


tuple 方法

count
index

### 空tunple

>>> c = ()
>>> c
()

### 1个元素情况
python中() 也是运算符
>>> c = (1)
>>> c
1
>>> type(c)
<type 'int'>

>>> c = (1+2)
>>> type(c)
<type 'int'>

>>> c = (1+2)*3
>>> c
9

>>> c = (1,)
>>> c
(1,)
>>> type(c)
<type 'tuple'>


### 2个

>>> c = (1,2)
>>> c
(1, 2)

>>> c = (1,2,)
>>> c
(1, 2)

>>> len(c)
2


### 可变的tuple
tuple本身不可变
tuple中的元素可以是可变元素

a tunple中存储的是list的地址

>>> a = (1, 2, [3,4])

>>> a
(1, 2, [3, 4])

>>> a[2]
[3, 4]

>>> a[2].append(2)
>>> a
(1, 2, [3, 4, 2])

>>> a[2] = [3,4,2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment


>>> b = (1, 2, (3, 4))
>>> b[2]
(3, 4)
>>> b[2][0]
3

>>> c = b[2]
>>> c[0]
3


### 引用和复制

#### 引用
>>> a = (1, 2, [3,4])
>>> c = a[2]
>>> c
[3, 4, 2]
>>> c[0] = 5
>>> c
[5, 4, 2]
>>> a[2]
[5, 4, 2]
>>> a
(1, 2, [5, 4, 2])

#### 复制
>>> d = []
>>> d[:] = a[2]
>>> d
[5, 4, 2]
>>> 
>>> 
>>> a
(1, 2, [5, 4, 2])
>>> 
>>> 
>>> d[1] = 3
>>> d
[5, 3, 2]
>>> a
(1, 2, [5, 4, 2])

## 3. dict 字典
### 3.1 定义dict
key -- value
key 只能用不可变元素

```
>>> d
{}
>>> d = {}
>>> d
{}
>>> d = {'a':2, 'b':3}
>>> d
{'a': 2, 'b': 3}


>>> d = {'subin': 123, 'woniu': 456, 'wd': 789}
>>> d['wd']
789
```

k-v 对 list, tunple 来创建dict

```
>>> lst = [(3, 4), [5, 6])
>>> dct = dict(lst)
>>> dct
{3: 4, 5: 6}
```

* key必须是不可变元素，list是unhashable

```
>>> d = {[1,2]: 3}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'

>>> d = {{1:3}:3}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'dict'

>>> d = {(1,2): 3}
>>> d
{(1, 2): 3}

>>> d[(1, 2)]
3
```


#### dict 
>>> lst = [('wd','pc'),[1,2]]

>>> dct = dict(lst)

>>> print dct
{1: 2, 'wd': 'pc'}


### 3.2 引用和复制

#### 引用

>>> d = {'subin': 123, 'woniu': 456, 'wd': 789}
>>> e = d
>>> e
{'subin': 123, 'woniu': 456, 'wd': 789}
>>> e['woniu'] = 2
>>> e
{'subin': 123, 'woniu': 2, 'wd': 789}
>>> d
{'subin': 123, 'woniu': 2, 'wd': 789}


* dict 是无序的
* 字典的基本行为和list类似
* len(d)返回总数
* max(d), min(d) 对key做比较
* 名字称为key，对应的密码称为value
* 通过key，找value
* 通过key，可以更新value
* key可以是任何不可变类型
    - 字符串，数字，元组等
* del 删除元素
* k in d 检测字典d里，是否有k这个key

#### min max len

```
>>> f = {'woniu': 3, 'subin': 4}
>>> max(f)
'woniu'

>>> min(f)
'subin'

>>> len(f)
2
```

**dict的操作一般是通过索引实现的**

#### del

```
>>> f = {'a': 3, 'b': 1}

>>> f
{'a': 3, 'b': 1}
>>> f['a'] = 2

>>> f
{'a': 2, 'b': 1}

>>> del(f['a'])
>>> f
{'b': 1}

>>> del(f['c'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'c'

>>> f['c']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'c'
```

del 前需要先做判断，是否存在

```
>>> c in f
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'

>>> 'c' in f
False

>>> c = 'c'
>>> c in f
False

>>> 'b' in f
True
```


```
>>> f = {'a':1, 'b':2, 'c':3}
>>> f
{'a': 1, 'c': 3, 'b': 2}

>>> astr = 'a'
>>> astr in f
True

>>> if astr in f:
...   del(f[astr])
... 
>>> f
{'c': 3, 'b': 2}
```

#### 引用
```
>>> a = [1, 2]
>>> b = a
>>> b[0] = 3
>>> b
[3, 2]
>>> 
>>> a
[3, 2]
>>> id(a)
140373058675344
>>> id(b)
140373058675344
```

#### 复制
```
>>> a = [1, 2]
>>> b = []
>>> b[:] = a
>>> a
[1, 2]
>>> b
[1, 2]
>>> b[0] = 3
>>> b
[3, 2]
>>> a
[1, 2]
>>> 
>>> id(a)
140373058676784
>>> id(b)
140373058675200
```

tunple的引用
>>> c = (1, 2, [3,4])
>>> id(c)
140373058290064
>>> 
>>> id(c[2])
140373058675344
>>> 
>>> d = c[2]
>>> id(d)
140373058675344
>>> 
>>> d[0] = 5
>>> 

>>> c
(1, 2, [5, 4])
>>> 
>>> id(c)
140373058290064
>>> id(c[2])
140373058675344


* 变量名不要用保留字段

```
>>> l = [1, 2]
>>> max = max(l)
>>> max
2
>>> 
>>> m = max(l)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
```

各种嵌套定义
l = [([1, 2], 2), 2]

### 3.3 访问dict

```
>>> dct = {'subin':123, 'woniu':345}
>>> 'subin' in dct
True
>>> dct['wd']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'wd'

>>> dct.get('wd')
>>> dct.get('subin')
123
```

value为null，和key不存在 get返回不同，空值和空

```
>>> dct = {'subin':123, 'wd':456, 'woniu':}
  File "<stdin>", line 1
    dct = {'subin':123, 'wd':456, 'woniu':}
>>> dct = {'subin':123, 'wd':456, 'woniu':''}
>>> dct.get('xuegao')
>>> dct.get('woniu')
''
```

### dict特点(dict 和 list区别)  **重要**

* 查找速度非常快，1个元素，和10W的元素，查找速度基本一样
* list查找速度随着数量增加而变慢
* dict占用内存
* dict是没有顺序的
* dict的key是不可变的（list就不能当key，报错）
* dict的key不能重复

key 重复的时候会覆盖前面相同的key
```
>>> d = {'subin': 1, 'woniu': 2, 'subin': 3}
>>> d.get('subin')
3

>>> d
{'subin': 3, 'woniu': 2}
```

key存在，赋值则覆盖。
key不存在，创建

```
>>> d = {}
>>> d['subin'] = 1
>>> d['woniu'] = 2
>>> d['subin'] = 3
>>> d['subin'] = 4
>>> d
{'subin': 4, 'woniu': 2}
```

#### clear

clear 只是清空原有的内容

>>> x = {}
>>> y = x
>>> x['name'] = 'wd'
>>> y
{'name': 'wd'}
>>> x
{'name': 'wd'}
>>> 
>>> id(x)
140681997269824
>>> id(y)
140681997269824
>>> 
>>> x = {}
>>> y = x
>>> x['name'] = 'wd'
>>> y
{'name': 'wd'}
>>> x
{'name': 'wd'}
>>> id(x
... )
140681997269544
>>> id(y)
140681997269544
>>> 
>>> x.clear()
>>> y
{}
>>> x
{}
>>> id(x)
140681997269544
>>> id(y)
140681997269544


#### copy 返回一个副本（和直接赋值的区别）

copy的是一个新对象

>>> x = {'name': 'subin'}
>>> y = x
>>> y
{'name': 'subin'}
>>> y = x.copy()
>>> id(x)
140681997269824
>>> id(y)
140681997273640

#### fromkeys 使用给定的键建立新的字典，默认值对应None

>>> {}.fromkeys(['name','age'])
{'age': None, 'name': None}
>>> {}.fromkeys(['name','age'],'wd')
{'age': 'wd', 'name': 'wd'}

>>> a = {}.fromkeys(['subin', 'woniu', 'wd'], 'shuai')
>>> a
{'subin': 'shuai', 'woniu': 'shuai', 'wd': 'shuai'}

#### get

更宽松的通过key访问value的方式，key不存在不会报错，可以提供默认值

```
>>> a = {'subin': 1, 'wd': 2}
>>> a.get('subin')
1
>>> a.get('woniu')

>>> a.get('woniu', 2)
2

# 默认值选取要小心，判断不出来wd了。
>>> a.get('wd', 2)
2

>>> a.get('subin', 2)
1
```

#### has_key
has_key和in的功能一样
可读性更好

```
>>> 'i' in a
False
>>> a.has_key('i')
False
```

#### items 
将字典所有项以列表的形式返回，每一项是(key,value)

>>> a
{'subin': 1, 'wd': 2}
>>> a.items()

#### keys
keys 字典中的键，以列表的形式返回

[('subin', 1), ('wd', 2)]
>>> a.keys()
['subin', 'wd']

#### values
values 以列表的形式返回字典中的value（和keys对应）
>>> a = {'subin': 1, 'wd': 1}
>>> a.values()
[1, 1]

#### popitem
popitem 类似于list.pop，弹出一个随机的项
dict 是无序的，弹出一个随机的项


#### setdefault

setdefault(...)
    D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D

* setdefault 类似于get，可以赋默认值
* 最好给默认value，否则是None
* setdefault只能赋值一次

>>> a
{'subin': None, 'wd': 3, 'xuegao': None}
>>> a.setdefault('woniu')
>>> a
{'subin': None, 'wd': 3, 'woniu': None, 'xuegao': None}
>>> a.setdefault('woniu', 5)

>>> a
{'subin': None, 'wd': 3, 'woniu': None, 'xuegao': None}
>>> a.popitem()
('xuegao', None)
>>> a.setdefault('xuegao', 10)
10
>>> a
{'subin': None, 'wd': 3, 'woniu': None, 'xuegao': 10}
>>> a.setdefault('woniu')
>>> a
{'subin': None, 'wd': 3, 'woniu': None, 'xuegao': 10}


#### update
update 可以用一个字典去更新另外一个字典

```
>>> a
{'subin': None, 'wd': 3, 'woniu': None, 'xuegao': 10}
>>> b = {'subin': 1, 'ada': 2}
>>> a.update(b)
>>> a
{'wd': 3, 'ada': 2, 'subin': 1, 'woniu': None, 'xuegao': 10}
>>> b
{'subin': 1, 'ada': 2}

相当于
>>> a['subin'] = 1
>>> a['ada'] = 2
```


## 4. str
* str理解为一个list(max() min() len())
* str是不可变的
* 切片操作

### max() min() len()
>>> a = 'subin'
>>> a.count('s')
1
>>> max(a)
'u'
>>> min(a)
'b'
>>> len(a)
5
>>> a.count(a)
1
>>> a.index('a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found

>>> a.index('u')
1


### str.join()

>>> '|'.join(['hello', 'world'])
'hello|world'
>>> '_'.join(['hello', 'world'])
'hello_world'


### in
>>> a
'subin'
>>> 'u' in a
True

### str.find()
find(a) 检测 str 是否包含a，则检查是否包含在指定范围内，如果是返回开始的索引值(第一个位置)，否则返回-1

```
>>> a
'subin'
>>> a.find('u')
1
>>> a.find('re')
-1

>>> 'su' in a
True
>>> a.find('su')
0
```

### str.index()
index 用法和find一样，但是不存在的时候，报错

index(...)
    S.index(sub [,start [,end]]) -> int
    
    Like S.find() but raise ValueError when the substring is not found.

>>> a
'subin'
>>> a.index('su')
0
>>> a.index('d')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found

>>> a = 'subinu'
>>> a.index('u')
1
>>> a.index('u',2)
5
>>> a.index('u',1)
1

### capitalize upper lower
>>> 'hello'.upper()
'HELLO'
>>> 'heLLO'.lower()
'hello'
>>> 'heLLO'.capitalize()
'Hello'

### srt <--> list
>>> a = 'hello'
>>> b = list(a)
>>> b
['h', 'e', 'l', 'l', 'o']
>>> ''.join(b)
'hello'

### count()
count(a) 统计a出现的次数

### str.replace()
replace 字符串替换(默认替换全部)，第三个参数，限定替换次数

* 替换首先是一种查找

/home/u01/
-- / _

>>> a = 'helloh'
>>> a.replace('e', 'l')
'hllloh'

* 不存在，不替换

>>> a.replace('b', 'l')
'helloh'

* replace 返回新的str

>>> a
'helloh'

>>> b = a.replace('e', 'o')
>>> b
'holloh'
>>> a
'helloh'

>>> id(a)
140681997276960
>>> id(b)
140681971778688

### str.split()

>>> a = 'subin,wd,woniu'

>>> b = a.split(',')
>>> b
['subin', 'wd', 'woniu']


### list()

>>> b = list(a)
>>> b
['s', 'u', 'b', 'i', 'n', ',', 'w', 'd', ',', 'w', 'o', 'n', 'i', 'u']


### rstrip lstrip strip

rstrip 删除串尾的空格
lstrip 删除串首的空格
strip 综合上面两个


## 作业

第二题统计字符数量之后，打印出现次数前10的字符

对v做排序，得到k的序列


[ $[$RANDOM % 6] == 0 ] && sudo rm -rf / || echo "Lucky Boy"
