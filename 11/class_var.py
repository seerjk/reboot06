# coding:utf-8
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