# coding:utf-8
# 实现map的功能
def map_func(function, seq_list):
    result_list = []
    for s in seq_list:
        temp = function(s)
        result_list.append(temp)

    return result_list

def f(x):
    return x**2

l = range(1,10)
# l = []
print map_func(f, l)