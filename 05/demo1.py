# coding:utf-8

# def hello(i):
#     if i < 2:
#         return 'haha'
#     else:
#         return 'hohoho %s' %i

# print hello(3)


# def empty():
#     return

# print empty()


# def hello(text):
#     print 'hello %s' % text

# hello('jiangkun')


# def print_params(**params):
#     print params

# print_params()
# print_params(name='jiangkun', job='coder')

a = 'subin'
def changeName(name):
    name = 'woniu'
    print name

print a
changeName(a)
print a

b = ['subin', 'wd']
def changeName(name_list):
    name_list[0] = 'woniu'
    print name_list

print b
changeName(b)
print b


def hello(name, age):
    print name
    print age

# hello('subin', 20)
# hello(20, 'subin')
# hello('subin')
# hello('subin', 20, 'woniu')
# hello('subin', 'subin')

a = 'subin'
hello(a, a)

def hello_world(name, word):
    print "%s, %s" % (name, word)

hello_world('wd', 'hello')

def hello_world(word, name):
    print "%s, %s" % (name, word)

hello_world('wd', 'hello')

## 关键字参数
def hello(name, age):
    print name
    print age

hello(age = 2, name = 'subin')
hello(name = 'subin', age = 2)

## 形参的默认值
def hello(name = 'subin', age = 20):
    print name
    print age

hello('subin', 30)
hello(30, 'subin')
hello('wd')

hello(name = 'wd')
hello(age = 20, name = 'subin')
hello()

###
# def hello(name = 'subin', age):
#     print name
#     print age
# SyntaxError: non-default argument follows default argument

def hello(name , age = 20):
    print name
    print age

# hello()
hello('subin')
# hello(age = 20)
# hello(age = 30, 'subin')
# hello('subin', age = 30)


# def hello(name , age = 20, sex):
# SyntaxError: non-default argument follows default argument
def hello(name , age = 20, sex = 'male'):
    print name
    print age
    print sex

hello('subin', 20, 'mail')
hello('subin', 'mail', 20)
hello('subin', sex = 'mail', age = 20)


def hello(name = 'subin'):
    print name

# 调用
hello2 = hello()
print type(hello2)
# 赋值
hello2 = hello
print type(hello2)
# <type 'function'>
hello2
# <function hello at 0x1c63c80>

hello2('wd')
hello2(name = 'woniu')

def hello():
    print 'hello'

def hello2():
    hello()
    print 'subin'

hello()
hello2()

def hello3():
    hello4()

# hello3()
# NameError: global name 'hello4' is not defined

# 函数作为参数
# 1. arg: function name
def hello3():
    return 'subinggg'

def hello(function):
    return function()

print hello(hello3)
# subinggg

# 2. arg: function name
def hello3():
    return 'subinggg'

def hello(function):
    return function

print hello(hello3)
# <function hello3 at 0x02434370>

# 3. arg function
def hello3(name = 'subin'):
    return name

def hello(function):
    return function()

def hello2(name):
    return name

# print hello(hello2('subin'))
# TypeError: 'str' object is not callable

# print hello(hello2)
# TypeError: hello2() takes exactly 1 argument (0 given)

# 1. 所有参数都加默认值
# 2. 或者函数无参数

print hello(hello3)

## 4. 
# def hello(fucntion):
#     return function(name)

# print hello(hello2)
def hello2(name):
    return name

def hello(function):
    return function(name = 'subinggg')

print hello(hello2)

## 5.
def hello2(name):
    return name

def hello(function, name):
    return function(name)

print hello(hello2, 'jiangk')


## * 收集参数
def hello(*names):
    print names

hello()
# ()  空tuple

hello('subin')
# ('subin',)
hello('subin', 'wd')
# ('subin', 'wd')
# hello(name = 'subin', 'wd', 'woniu')
# SyntaxError: non-keyword arg after keyword arg

# 收集参数，不能这么做
# hello('wd', 'woniu', name = 'subin')
# TypeError: hello() got an unexpected keyword argument 'name'

def hello(*name):
    print name[0]
    print name[2]

# hello()
# IndexError: tuple index out of range

hello('hello', 'subin', 20, 23)
# hello
# 20

# 收集参数 带来很多不确定性
# 收集参数 不能和 关键字参数混用
# 收集参数 可以和位置参数混用

def hello(name, *params):
    print name
    print params

hello('subin', 1, 2, 3)

# * 的收集参数，本质是位置参数

# ** 收集参数
# ** 的收集参数，本质是关键字参数，k-v对传入
# ** 的用于接收命令行参数，很多，且不确定

def hello(**names):
    print names

hello()
# {}

hello(name = 'subin', age = 20, sex = 'male', techang = 'runnig')
# {'age': 20, 'techang': 'runnig', 'name': 'subin', 'sex': 'male'}

# 忽略没定义，或者没用的参数
def hello(**names):
    print names['name']
    print names['age']

hello(name = 'subin', age = 20, sex = 'male', techang = 'runnig')

a_dict = {'age': 20, 'techang': 'runnig', 'name': 'subin', 'sex': 'male'}
# hello(a_dict)
# 报错，和定义不符合
# 传入一个dict
hello(**a_dict)


## 
def hello2(a_dict):
    print a_dict['name']
    print a_dict['age']

a_dict = {'age': 20, 'techang': 'runnig', 'name': 'subin', 'sex': 'male'}
hello2(a_dict)


# 参数作用域
# 
a = 2
def hello():
    print a

hello()

# 
def hello():
    ab = 2
    print ab

# print ab
# NameError: name 'ab' is not defined

aa = 2
def hello():
    aa = 3
    print aa
    # 局部的优先

hello()

# 
print "****"
a = 2  # 全局变量
def hello(a):   # 形参， 不影响实参的是
    print a      # 传入的
    a = 3        # 局部变量
    print a      # 局部变量,局部的优先

hello(a)
print a

# 
print "*****"
a = 2
def hello():
    global a  # a 被重新声明，全局变量
    a = 3
    print a

print a   # 2  
hello()   # 3
print a   # 3 

# 
print "*****" 
def hello():
    global b
    b = 1
    print b

# print b
# b no defined
hello()
print b
# 全局变量 局部变量 内存位置不同


#
print "*****" 
def hello():
    a = 2

def hello2():
    a = 2
    print 'hello2: %s' % a
    hello()

a = 2
def hello():
    global a
    a = 3

hello()   # 影响全局a，不对 hello2() 中的局部a产生影响
print a

hello2()

# 作用域保护了变量重名问题

#
print "*****" 
# def hello(a):
#     global a
#     print a
# SyntaxError: name 'a' is local and global
# 形式参数只能是局部变量，
# 对和函数的参数同名的传入参数，如果声明了全局变量，则会报错

l = range(1,10)

def f2(x, y):
    return x + y

print reduce(f2, l)