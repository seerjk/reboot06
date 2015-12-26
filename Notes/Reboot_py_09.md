# Note 08

## 1. 作业讲解
第七次作业基础上，不刷新页面


同步刷新：
        sql                    >render_template,return字符串>>>
数据库------------Flask，web后端---------------------------------前端
            Flask数据访问数据 <<<表单,button submit,input(name),input(pwd)

异步

          sql                    
数据库------------Flask，web后端---------------------------------前端
            1.渲染页面 渲染简单的数据                       1.展现(jinja2)
                render_template()                             1.bootstrap
            2.数据接口，供AJAX调用                          2.ajax调数据
                json                                            jquery
                1.list    ---------------------------------     1.list
                2.add     ---------------------------------     2.add
                3.del     ---------------------------------     3.del

首次渲染快，logo,边栏，图片等不用等数据库查询就能渲染

引入静态文件

* jinja2
    - python渲染，替换数据，生成html，再给浏览器
    - python速度比js快
    - 同步加载，获取数据要刷新页面
    - 不能异步加载，因为python处理的
* ajax
    - js渲染
    - 异步加载，局部刷新
    - 交互好，web2.0 (gmail--->ajax第一代)

线上一般二者结合：

* 首屏加载 jinja2
* 异步数据 ajax


jinja2  过滤器
http://docs.jinkan.org/docs/jinja2/


不刷新页面，使用ajax完成

提示，如果一个按钮是异步生成的，一开始绑定的时间就失效了，需要改一下写法

```
$('.test').on('click',function(){
    console.log(1)    
})
```

上面的代码，如果.test按钮不是页面初始化存在的，而是ajax异步渲染的，上面写法就会失效，需要用下面的代码

```
$(document).on('click','.test',function(){
    console.log(1)
})
```

用$(document).on，.test是第二个参数即可


jquery 序列化表单的函数
name="name"
name="passwd"

$('#server-id').serialize()


flask jsonify

## 2.jQuery UI
https://jqueryui.com/

### 2.1 滑块 slider
https://jqueryui.com/slider/

获取值
http://api.jqueryui.com/slider/#method-value

view source

第三方组件
    option 初始化配置
    method 外部控制组件
    events 组件内部通知外部


### 2.2 datepicker
https://jqueryui.com/datepicker/
日期要求：前端加入一个日期输入，点击按钮获取值，在下方显示
格式要求：2015-12-19


静态文件统一管理

static
    lib
        jqueryui
        jquery
    page
    widget  通用组件自己写的

前端静态资源管理工具 -- bower


## 3.sweetalert 各种弹出窗
http://www.dglives.com/demo/sweetalert-master/example/

完善作业：
删除前有 提示框 warning
添加成功 有提示框 success

jsformat  -- ctrl+alt+f

区别：
$.
$(document)

$两个用法：
* $作为函数用
    操作页面元素的
    $('#id').html
    $(按钮).show()  $(this)
* 当做工具函数库
    和操作元素无关的
    http://www.cnblogs.com/kissdodog/archive/2012/12/27/2835561.html
```js
// 函数
function R(args){
    var obj = {
        'hide':function(){
            console.log(args + ' hide!')
        },
        'show':function(){
            console.log(args + ' show!')
        }
    }
    return obj
}

R('wd').hide()
R('pc').show()

// 工具函数
R.ajax = function(args){
    console.log(args + ' is ajaxed.')
}
R.ajax('reboot')
```

## 4. 其他好玩库

### 4.1 animate.css 动画
https://daneden.github.io/animate.css/

一个css，各种动画

首屏加载，左右分别滑入。

### 4.2 Hover.css  各种动画效果
http://ianlunn.github.io/Hover/


## 5. bootstrap 
### 5.1 模态窗 -- 弹窗
弹窗 2个div
http://v3.bootcss.com/javascript/#modals

.modal('show')

手动打开模态框。在模态框显示之前返回到主调函数中 （也就是，在触发 shown.bs.modal 事件之前）。

$('#myModal').modal('show')
.modal('hide')

手动隐藏模态框。在模态框隐藏之前返回到主调函数中 （也就是，在触发 hidden.bs.modal 事件之前）。

$('#myModal').modal('hide')






### 
form如果没有写action，其中有button，点击button的时候也会刷新页面，如果不想刷新，是不是把form改为div？@狂奔的~蜗牛~~  蜗牛大
蜗牛-51reboot(316783812)  17:15:35
form可以绑定submit时间
里面return false即可
不会提交了
不绑定button的事件
或者你的button type设置为button
就不会提交 




## 7. 作业
ajax操作
机器: 机器名name，机器memory，到期时间

功能：添加、删除、展示列表，和更新(在弹窗中更新)
admin.51reboot.com/page/   弹窗更新

登陆：同步，或者异步
    如果想做异步的，下面代码是提示：
    前端的跳转
    location.href="www.baidu.com"
    location.href="/"
