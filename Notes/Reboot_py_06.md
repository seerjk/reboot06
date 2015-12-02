# 06 Note

# 1. 作业点评

x[0] if x[0]> x[1] else x[1]
print sorted(L, key = lambda x : max(x))
print sorted(mylist,key=lambda (x,y): x * (x > y) + y * (x <= y))

range(start, end, step)


list.append()
list.extend()  合并，展开
区别：
```
a = [1,2,3]
b = [4,5,6]
c = ['hello']
# c.append(a)
# c.append(b)
c.extend([a, b])

print c
```

支持负号：
```
expression = '-1+2+3'

if expression[0] == '-':
    expression = '0' + expression
```

逆波兰表达式算法：
https://zh.wikipedia.org/wiki/%E9%80%86%E6%B3%A2%E5%85%B0%E8%A1%A8%E7%A4%BA%E6%B3%95

http://www.cnblogs.com/stay-foolish/archive/2012/04/25/2470590.html

https://github.com/51reboot/actual_06_homework/blob/master/05/woniu/cal_recursion.py

可视化
echarts
http://echarts.baidu.com/doc/example.html
对中国地图支持好。

轮询
长连接
websocket

http://map.norsecorp.com/
websocket 实现 实时展示
前后端都要支持


## 2.上节回顾——函数
* 上节课主要内容
    - 函数创建
    - 函数的返回值
    - 位置参数
    - 关键字参数
    - 参数怎么设置默认值
    - 收集所有参数
    - 作用域
    - 列表推倒式
    - lambda表达式
    - sorted函数


## 3. 模块
可以直接用别人的库

* python自带模块
* 第三方模块  pip install 
* 自己写的模块

```
>>> import math
>>> math.factorial(5)
120
>>> math.factorial(3)
6
>>> 
>>> import os
>>> os.getcwd()
'/home/jiangk/reboot06/06'
```

### 3.1 调用模块
```
#文件1 hello.py
def hello_world():
    print 'hello world'
```

```
#文件2
import hello
hello.hello_world()
```

### 3.2 调用模块方法

```
from hello import hello_world
hello_world()
```

import * 不推荐，防止有函数名冲突。
```
from hello import *
hello_world()
```

### 3.3 __name__
__name__  是当前的文件名
__name__  用于区分是被手动执行，还是被其他模块import的

* 手工执行自己 __name__ == '__main__'
* 被其他文件import  __name__ == 模块自己的文件名


## 4. flask

flask 小，扩展好，上手容易
django 大，不好扩展

https://www.baidu.com/s?wd=windows%20flask%20%20%E6%90%AD%E5%BB%BA&rsv_spt=1&rsv_iqid=0xf38c002a00018b37&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=2&rsv_n=2&rsv_sug2=0&inputT=436&rsv_sug4=440

url
https://www.baidu.com/s
?wd=windows%20flask%20%20%E6%90%AD%E5%BB%BA
&rsv_spt=1
&rsv_iqid=0xf38c002a00018b37
&issp=1&f=8&rsv_bp=0
&rsv_idx=2
&ie=utf-8
&tn=baiduhome_pg
&rsv_enter=1
&rsv_sug3=2
&rsv_n=2
&rsv_sug2=0
&inputT=436
&rsv_sug4=440


?  后面是参数
https://baidu.com/test/aa?name=hello&age=10

### 4.2 flask 渲染页面
flask_web.py
```
from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
     return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9002)
```

默认渲染 `./templates/` 下的html文件
./templates/index.html
```
name: <input type="text" value="jiangk">
<input type="button" value="submit">
```

## 5. 前端

* html 超文本标记语言，描述语言
    - 标签，网页的内容
* css 层叠链式表，描述语言
    - 样式 外观
* javascript 编程语言
    - 动态，数据

sublime text 安装插件
http://www.cnblogs.com/Rising/p/3741116.html

前端插件  emmet  快速输入html


颜色表示方法：

* 单词  yello blue red
* GRB   #1A65B9
* RGB RGBA
    - rgb(255,255,0)
    - rgba(r,g,b,透明度)

```
<div style='width:200px;height:200px;background:#FF0000'>
</div>

<div style='width:200px;height:200px;background:rgba(255,0,0,0.5)'>
</div>
```

html:5

form 标签：和后端交互，提交数据

练习1：
输入 用户名 密码
如果用户名和密码都是 admin，网页显示 yes，否则显示 no

练习2：
user.txt


html中 <!-- -->注释   缩写为：
c
 没错，小写的C 然后 ctrl+e 展开

css中 /* */   注释  缩写为：
cm
ctrl+e展开就好了。

练习3
user.txt 表格形式显示web

作业：
