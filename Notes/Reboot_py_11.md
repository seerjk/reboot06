# Note 11

## 异步绑定
document 是整个网页
冒号事件机制

$(document).on('click', 'del-btn', function(){
    //
    alert(1)
})

问题：
document 上绑定很多事件，取消某个绑定很难做

不用documnet，如何异步绑定？


html 中自定义属性 规范以`data-`开头，如 data-id

// 以data-开头属性可以用data()方法获取数据
var id = $(this).data('data-id')
var id = $(this).attr('data-id')


## post 方法

ajax:
```js
$(document).on('click', '.del-btn', function(){
    var id = $(this).attr('data-id')
    $.post('/delhost', {"id":id}, function(res){
        if(res=='ok'){
            getList()
        }else{
            swal('error!')
        }
    })
})
```

flask:
```python
app.route('/delhost', methods=['POST'])
def delhost():
    id = request.form.get('id')
    pass
```

* Get方式: 获取数据

用get方式可传送简单数据，但大小一般限制在1KB下，数据追加到url中发送（http的header传送），也就是说，浏览器将各个表单字段元素及其数据按照URL参数的格式附加在请求行中的资源路径后面。另外最重要的一点是，它会被客户端的浏览器缓存起来，那么，别人就可以从浏览器的历史记录中，读取到此客户的数据，比如帐号和密码等。因此，在某些情况下，get方法会带来严重的安全性问题。

* Post方式: 操作数据

当使用POST方式时，浏览器把各表单字段元素及其数据作为HTTP消息的实体内容发送给Web服务器，而不是作为URL地址的参数进行传递，使用POST方式传递的数据量要比使用GET方式传送的数据量大的多。

总之，GET方式传送数据量小，处理效率高，安全性低，会被缓存，而POST反之。

* get是在url里
* post就是传一个dict


class 操作数据库
出错的时候重连

update更新操作
* 弹窗里面输入，传id
* 发送更新 要带上最初的id


## 第三方库
time
os
system
requests http请求
pyquery 页面解析
爬虫功能用class组织


## python 调试

### help
```
>>> l = [1,2]
>>> help(l)
>>> help(list)
```

### dir 查看所有函数

```
>>> dir(l)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

>>> help(l.append)

Help on built-in function append:

append(...)
    L.append(object) -- append object to end

>>> import random
>>> dir(random)
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', 'WichmannHill', '_BuiltinMethodType', '_MethodType', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '_acos', '_ceil', '_cos', '_e', '_exp', '_hashlib', '_hexlify', '_inst', '_log', '_pi', '_random', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'division', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'jumpahead', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']


>>> help(random.random)

Help on built-in function random:

random(...)
    random() -> x in the interval [0, 1).
```

### ipython
<tab>




Atom
atom就是一个浏览器
都可以写css来控制样式
很爽



## class

类变量 self.xxxx 是不是都要先在__init__()中声明

### 类变量和实例变量
[class各种概念](http://www.jb51.net/article/49402.htm)

类变量定义在类的定义之后，实例变量则是以为self.开头。例如：
代码如下:

```
class Foo(object):
    val = 0
    def __init__(self):
        self.val = 1
if __name__ == '__main__':
    foo = Foo()
    print foo.val
    print Foo.val
```

运行结果为：

1
0


### python的 类变量(静态变量) 实例变量(成员变量)

* 类变量(静态变量)
* 实例变量(成员变量)

```python
# 静态变量和实例变量的区别

class Test():
    # 静态变量
    name = 'reboot'
    def __init__(self, name, age):
        # 实例变量
        self.name = name
        self.age = age

a = Test('xiaoming', 10)
b = Test('xiaohua', 2)

print Test.name
print "%s is %s years old" % (a.name, a.age)
print "%s is %s years old" % (b.name, b.age)

print "=" * 30
class Test2():
    name = 'reboot'
    def __init__(self, age):
        self.age = age

a2 = Test2(10)
b2 = Test2(2)

print "%s is %s years old" % (a2.name, a2.age)
Test2.name = '22222'
print "%s is %s years old" % (a2.name, a2.age)
print Test2.name
print "%s is %s years old" % (b2.name, b2.age)
```

运行结果：
```
reboot
xiaoming is 10 years old
xiaohua is 2 years old
==============================
reboot is 10 years old
22222 is 10 years old
22222
22222 is 2 years old
```

### python 构造函数 析构函数

构造函数 `__init__()`
析构函数 `__del__()`


## requests 库
pip install requests


发送http请求，下载页面的所有内容
解析html：
    * 前端 jquery
    * 后端 pyquery

## pyquery

yum install -y gcc make gcc-c++
yum install -y libxslt libxslt-devel libxml2 libxml2-devel python-devel python-lxml
pip install pyquery

解析html内容

## sys
sys.argv 命令行参数
sys.path
sys.exit
sys.path

In [11]: sys.path
Out[11]: 
['',
 '/usr/bin',
 '/usr/lib/python2.7/site-packages/pyquery-1.2.10-py2.7.egg',
 '/usr/lib64/python27.zip',
 '/usr/lib64/python2.7',
 '/usr/lib64/python2.7/plat-linux2',
 '/usr/lib64/python2.7/lib-tk',
 '/usr/lib64/python2.7/lib-old',
 '/usr/lib64/python2.7/lib-dynload',
 '/usr/lib64/python2.7/site-packages',
 '/usr/lib64/python2.7/site-packages/gtk-2.0',
 '/usr/lib/python2.7/site-packages',
 '/usr/lib/python2.7/site-packages/IPython/extensions',
 '/home/jiangk/.ipython']

## os


In [6]: os.system('ls')
class_game.py  cmdb  cmdb.tgz  README
Out[6]: 0

In [7]: os.getcwd()
Out[7]: '/home/jiangk/reboot06/10/homework10'

In [8]: os.listdir(os.getcwd())
Out[8]: ['class_game.py', 'cmdb', 'README', 'cmdb.tgz']

In [9]: os.mkdir('demo')

In [10]: ls
class_game.py*  cmdb/  cmdb.tgz  demo/  README*


作业：
知乎精选问题的点赞数

作业：
上次的update

$('#myModal').modal('show')       // 初始化后立即调用 show 方法

编辑
    1. 打开弹窗 
    2. 初始化弹窗
        2.1 初始化组件(滑块，日期)
        2.2 初始化值
    3. 更新

防止cancel多次会绑定多个事件

会把所有的click事件都解绑
$('#update-confirm').on('click')
$('#update-confirm').on('click')
$('#update-confirm').on('click')

$('#update-confirm').off('click')

事件的命名空间 -- 只解绑一次
$('#update-confirm').on('click.update')
$('#update-confirm').off('click.update')



作业：去页面http://www.zhihu.com/topic/19776749/top-answers，爬知乎点赞数前100的回答和链接

log可视化 -- echart