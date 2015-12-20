# Note 08

## 1. 作业讲解

把第六次课的作业，从存文件，到存数据库，
美化web界面：前端表单和表格用bootstrap美化

### bianji

g  全局变量
before_request
after_request


db class  类，建立后一直使用，出错后自动重连

POST 要用调试软件看参数，参数更长
    POST
    id = request.form.get('id')
GET  直接看到参数，


分页:
    * 取出所有数据，分页和检索在前端做 -- 数据量小合适
    * SQL每次只查出10条
        - page 当前第几页
        - num  每页显示多少个
        * 同步执行SQL
        * 异步执行SQL，URL不变，页面不刷新
```
@app.route('/',methods = ['GET','POST'])
def index():
    
    # RESTful API  用http method来区分，只用写一个路由
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        try:
            g.cursor.execute("INSERT INTO user(username,password) VALUES ('%s','%s')" % (name,password))
        except Exception as e:
            abort(500)
        return redirect(url_for('index'))
    
    # 1  第一页，当前第几页
    page = int(request.args.get('page',1))
    # 每页多少个
    num = 5

    # 总共多少行
    g.cursor.execute("SELECT COUNT(*) FROM `user`")
    total = g.cursor.fetchone()[0]

    if total % num == 0:
        pages = total / num
    else:
        pages = total / num + 1
    start_position = (page - 1 ) * num
    
    # 分页查   limit 1, 5
    g.cursor.execute("SELECT * FROM `user` limit %s,%s" % (start_position,num))

    data = g.cursor.fetchall()
    print data
    return render_template('homework.html',userdata = data,pages = pages)
```

### SQLAlchemy
使用ORM预定义好的 sql操作
Python数据库ORM SQLAlchemy 
SQLAlchemy是Python编程语言下的一款开源软件。提供了SQL工具包及对象关系映射（ORM）工具

http://www.sqlalchemy.org/

http://docs.sqlalchemy.org/en/rel_1_0/orm/tutorial.html

#### flask-sqlalchemy
http://flask-sqlalchemy.pocoo.org/2.1/
http://flask-sqlalchemy.pocoo.org/2.1/quickstart/



### session

session 理解为dict

from session import flask
session['user'] = 'woniu'

def getdata():
    if session['user'] = 'woniu'：
        pass do

@app.before_request
def before_request():
白名单：help页面不做session验证

装饰器
@login_


### jinja2模板
http://docs.jinkan.org/docs/jinja2/
{% for %}
{% endfor %}

{% if %}
{% enif %}

变量：
{{d}}

### lizheng
@app.errorhandler(404)
def page_not_found(error):
    return "error: ", error


宽度：
添加<div style="width:40%;margin:1 auto;">

## 2. bootstrap

http://v3.bootcss.com/

css/
theme  主题
bootstrap.css  不压缩
bootstrap.min.css  压缩
bootstrap.css.map  压缩前后的对应关系 方便调试

fonts/
http://v3.bootcss.com/components/

js/
bootstrap.js
bootstrap.min.js
jquery.js

### 2.1 bootstrap 布局

栅格系统
    * container 容器
        * row 一行
        * con-md-数字 占几列 (一共12列)  md -- middle


http://v3.bootcss.com/css/#grid


容器 container
    “行（row）”必须包含在 .container （固定宽度）或 .container-fluid （100% 宽度）中，以便为其赋予合适的排列（aligment）和内补（padding）。

    .container （固定宽度）不管屏幕多宽，写死中间的宽度，两边留白
    .container-fluid （100% 宽度）

    <div class="container"></div>


字体图标
http://v3.bootcss.com/components/#glyphicons
http://fontawesome.io/icons/


## 3. javascript

    1. 基本语法
        * 变量
            a = 1
            var a = 1 (js)
        * 函数式编程：函数名做参数

    2. dom 浏览器文档元素
        * 原生的js很难写
        * 浏览器的兼容性问题
        * 100% 用jquery取代

    3. bom 去除主体以外的浏览器本身(浏览器的功能 console)
        * 不是课程重点
        * 不能被jquery取代

### 3.1 基本语法
变量
    a = 1 (py)
    var a = 1 (js)

    golbal a = 1 (py)
    a = 1 (js)


## 4. jquery

* 选择器
    * 找到元素(定位元素)
    * #id
    * .class
    * 标签名

* 操作
    hide(时间, 动画完成后执行的函数) 隐藏元素
    show(时间, 动画完成后执行的函数) 显示元素
    html 
        不传参数，获取内容，
        传参数，修改内容
    val 获取input的输入值
    on (事件类型，执行的函数)

* input用val
* html标签内容，用html


**script要放在body的最后面**
要先定义的 id  class，后调用script处理 id  class

```
<script src='./js/jquery.js'></script>
    <script>
        $(function(){
            // script 可以写在最前面
            // onload 触发事件，浏览器加载完成，才会执行这段代码
            // js jquery 代码写这里
            $("#submit-button").on('click', function(){
                var input = $("#input-text")
                var val = input.val()
                input.val('')
                // alert(val)
                var content = $('#content').html() + '<br>' + val
                $("#content").html(content)
            })
        })
    </script>
```

exec04
聊天窗口
    input 内容 取出来 ==> 渲染centent 
    content内容存起来，和input输入的内容拼接，再渲染


模态窗
    bootstrap js

ajax
    $.get(url, 处理函数(返回值){
        // 处理函数内容
    })


$ tree
.
├── flask_web.py
├── static
│   └── jquery.js
└── templates
    └── index.html


作业：
上次作业，添加和删除不准刷新页面
(添加成功和删除成功，都不刷新页面)


----
把第六次课的作业，存数从文件，换成数据库，用boostrap简单美化一下table和form



orm


bootstrap布局

栅格系统

    container容器
        row 一行
        col-md-数字 占几列宽度，一行有12份


javascript
    1.基本语法
        变量
            a=1
            global a
            var a = 1   (js)
            a = 1
        函数式编程
    2.dom 浏览器文档元素

        原声js很难写
        100%用jquery取代
    3.bom
        不是课程重点 不能被jquery取代


jquery
    

* 选择器
    * 找到元素
    * #id
    * .class
    * 标签名
* 操作
    show（时间，动画完成后执行的函数）  显示元素
    hide（时间，动画完成后执行的函数） 隐藏元素
    html 不传参，获取内容，传参，修改内容
    val 获取input的输入值
    on(事件类型 执行的函数)


聊天窗
    input的内容 取出=》渲染content
    content内存存起来，和input输入内容拼接，再渲染


ajax
    $.get(url，处理函数（返回值）)

上一次的作业 添加和删除不准刷新页面（添加成功和删除成功，都不刷新页面）