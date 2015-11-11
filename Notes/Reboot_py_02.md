# Reboot Python 02
> date: 2015-10-31

## 作业点评
* max list等python关键字不要作为变量名
* 变量命名要有含义
* 避免list中存在负数的情况

宋翔代码 看下


## list
>>> arr = [1,2,3,'name',True,False]
>>> arr
[1, 2, 3, 'name', True, False]
>>> arr[0]
1

>>> arr[15]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> arr[-1]
False

>>> arr[0:-1]
[1, 2, 3, 'name', True]
>>> arr[-1:]
[False]

>>> arr = [1,2,3,['hello','ok']]
>>> arr[3]
['hello', 'ok']
>>> arr[3][0]
'hello'
>>> arr[3][1]
'ok'



>>> list('hello')
['h', 'e', 'l', 'l', 'o']


>>> arr = list('helloreboot')
>>> arr
['h', 'e', 'l', 'l', 'o', 'r', 'e', 'b', 'o', 'o', 't']
>>> del arr[0]
>>> arr
['e', 'l', 'l', 'o', 'r', 'e', 'b', 'o', 'o', 't']
>>> del arr[0]
>>> arr
['l', 'l', 'o', 'r', 'e', 'b', 'o', 'o', 't']


### list 排序
arr = [1,2,3,123,11,123,421,124,2,3,4,5,6]

### 两个变量交换位置
a = 'hello'
b = 'reboot'

tmp = a
a = b
b = tmp

a,b = b,a

冒泡排序舞蹈秀
排序算法舞蹈
一系列的排序算法舞蹈

## list function
append

查看python帮助文档
dir(list) 
help(list.count)


## 引导复习一下list的知识
* 怎么定义一个list
* in，len，max，min，del

> del arr[5]

* 切片

> 切片赋值

* append, count, extend, index, insert, pop, remove, reverse


方法  原List   返回值
append  修改  无   
count   无   返回  
extend  修改  无   
index   修改  无   
insert  修改  无   
pop 修改  返回删除的值  
remove  修改  无   
reverse 修改  无

arr2 = arr[:]


### 作业1:2个数组去重
# way2
```
arr1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]*1000
arr2 = [2,1,3,2,43,234,454,452,234,14,21,14]*1000

arr_union = []
for i in arr1:
    if i not in arr_union and i in arr2:
        arr_union.append(i)

print arr_union
```

### 作业2：实现插入排序
arr = [88,0,1,2,3,123,11,123,421,-124,-2,3,4,5,6]

## 前端
* html 标签
* css  样式
* javascript 操作浏览器

js库
jquery
引用百度的jquery

css库
bootstrap
http://www.bootcss.com/

emmet 工具命令学习