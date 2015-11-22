# coding:utf-8

# 计算阶乘的函数
# 一个正整数的阶乘（英语：factorial）是所有小于及等于该数的正整数的积，并且有0的阶乘为1。自然数n的阶乘写作n!。

# 1. 增加浮点数的判断，
# 2. 判断边界 不能大于65535

# return 返回的要保持类型一直，特定类型，实现单一类型。

def factorial(num):
    if not isinstance(num, int):
        # num is not a int
        return -2
    
    if num < 0:
        # num is less than 0
        return -1

    if num == 0:
        return 1

    # num > 0
    result = 1
    for i in xrange(1, num + 1):
        result *= i

    return result

print type(factorial(1000))
print factorial(0)
print factorial(-5)
print factorial(30)

def factorialRecursion(num):
    if num < 0:
        return 'Error, num must bigger than 0'
    elif num == 0:
        return 1
    else:
        return num * factorialRecursion(num - 1)

print factorialRecursion(0)
print factorialRecursion(-1)
print factorialRecursion(30)
