# coding:utf-8

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

def swith(express_input, operations=['+', '-', '*', '/']):
    swith_list = []
    num = ''
    for key in express_input:
        if key not in operations:
            num += key
            # continue
        # if key in operations:
        else:
            swith_list.extend([int(num), key])
            num = ''
            # continue
    swith_list.append(int(num))
    return swith_list

# data =raw_input('please input Expression:')
data = '1+2*3'
new_list = swith(data)
result = new_list[0]

for key in range(1, len(new_list), 2):
    temp = new_list[key]
    # result = cal_dict[temp](result, new_list[key+1])
    result = cal_fn(temp, result, new_list[key+1])
    # if new_list[key] == '+':
    #     result = result + new_list[key + 1]
    # elif new_list[key] == '-':
    #     result = result - new_list[key + 1]
    # elif new_list[key] == '*':
    #     result = result * new_list[key + 1]
    # elif new_list[key] == '/':
    #     result = result / new_list[key + 1]

print result
