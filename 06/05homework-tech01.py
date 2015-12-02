# coding: utf-8

# 扩展为操作函数
def cal_fn(operator, x, y):
    x = float(x)
    y = float(y)
    cal_dict = {
        '+': lambda x,y: x+y,
        '-': lambda x,y: x-y,
        '*': lambda x,y: x*y,
        '/': lambda x,y: x/y
    }

    return cal_dict[operator](x, y)

def swith(express_input):