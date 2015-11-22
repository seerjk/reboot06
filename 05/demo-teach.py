# coding:utf-8
def hello(name, age):
    print name
    print age

hello('subin', 20)

hello(20, 'subin')

def hello(name, age):
    print name
    print age

# hello('subin')
# TypeError: hello() takes exactly 2 arguments (1 given)

# hello('subin', 'woniu', 20)
# TypeError: hello() takes exactly 2 arguments (3 given)

hello('subin', 'subin')

a = 'subin'
hello(a, a)


def hello(name, age):
    print name
    print age

hello(age = 20, name = 'subin')
hello('subin', 20)
hello(20, 'subin')


def hello(name = 'subin', age = 20):
    print name
    print age

hello('subin', 30)
hello(30, 'subin')

hello(name = 'subin', age = 30)
hello(age = 30, name = 'subin')
hello()


# def hello(name = 'subin', age):
# SyntaxError: non-default argument follows default argument
#     print name
#     print age

def hello(name, age = 20):
    print name
    print age

# hello()
# TypeError: hello() takes at least 1 argument (0 given)

hello('subin')
hello('subin', 30)

# hello(age = 30)
# TypeError: hello() takes at least 1 argument (1 given)

# hello(age = 30, 'subin')
# SyntaxError: non-keyword arg after keyword arg

hello('subin', age = 30)


# def hello(name, age = 20, sex):
# # SyntaxError: non-default argument follows default argument
#     print name
#     print age
#     print sex

def hello(name, age = 20, sex = 'male'):
    print name
    print age
    print sex

hello('subin')
hello('subin', 30, 'female')
hello('subin', 'female', 30)
hello('subin', sex = 'female', age = 30)
hello('subin', sex = 'female')


## 收集参数
# 收集参数.txt
