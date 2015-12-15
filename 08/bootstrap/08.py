# coding:utf-8

def hello(fn):
    fn('asd')

def test(name):
    print name


hello(test)

# 匿名
def hello(fn):
    print fn('asd')

hello(lambda x: 'hello '+x )