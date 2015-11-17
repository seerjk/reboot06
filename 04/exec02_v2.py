# coding:utf-8

# tem.txt存储这日期和气温的数据，求最高温度和平局温度
# 11.12 7
# avg 4.1
# 结果还要存在原来文件的末尾

# 写代码要注意：每句话的影响
# * avg = sum / count 一定要考虑除数为0的情况

# 所有代码放到 try except else 中，偷懒的方法

# 改进：
# [x] 1. 文件为空，出现  0/0 报错，需要处理文件为空的情况
# [x] 2. 文件不存在, try -- catch
# [x] 3. 多天最高温度相同  存入 dict
# [x] 4. 数据记录异常情况需要考虑
#        11.12 7aadf  --  剔除无法转换为float的温度记录
#        11.11 6 00   --  按空格拆分
#        11.13 500    --  温度不合理，地表温度范围：-90 ~ 61
# [x] 5. 温度全负数 清空

# 知道最高温度，就能知道日期了。只需要记住最高温度，然后在list中找


# 2个以上最高温度相同
# 改进1：只记录最高温度，再去dict中查找对应有多少天，需要创建dict，两次for
# 改进2：把所有相同的最高温度的 日期:温度 存入max_dict，
#        如果遍历到更高温度，则清空 max_dict.clear()
max_dict = {}

sum_tem = 0
sum_items = 0

try:
    with open('tem.txt') as f:
        tem_content = f.readlines()
except:
        print "File Error"
else:
    if tem_content == []:
        print "Empty file."
        exit(1)

    # 变量初始化要小心，初始化值会不会影响到计算，最好用第一个值去赋值
    # 避免前几个温度记录都是有错误的记录，放到for 中作为局部变量 初始化
    # 比如 11.12 7aadf 
    # 通过判断 sum_items == 0 来确定是否初始化变量

    # max_tem = float(tem_content[0].strip().split(' ')[1])
    # first_date = tem_content[0].strip().split(' ')[0]

    for line in tem_content:
        # line = line.replace('\n', '')
        # temp_list = line.split(' ')
        # str.strip()  去除 '\n'
        temp_list = line.strip().split(' ')

        # 判断温度是否合法
        try:
            current_temp = float(temp_list[1])
        except:
            continue

        if current_temp > 61 or current_temp < -90:
            continue

        current_date = temp_list[0]

        # Init max_tem, max_dict
        if sum_items == 0:
            max_tem = current_temp
            max_dict = {current_date:current_temp}

        sum_tem += current_temp
        sum_items += 1
        # 计数的好处 11.6 7aaa  异常情况可以剔除

        if current_temp > max_tem:
            max_tem = current_temp
            max_dict.clear()

            max_dict[current_date] = current_temp

        if current_temp == max_tem:
            max_dict[current_date] = current_temp

if sum_items == 0:
    # 文件中所有记录都不合法，防止出现 0/0 情况，直接退出
    print "No legal record in the file."
    exit(1)

for k,v in max_dict.items():
    print "%s %.0f" % (k, v)

# len(tem_content) 可以代替 sum_items，有illegal records时会有问题
print "avg %.1f" %(sum_tem / sum_items)

# 最高温，平均温度 写回文件
temp_content = "\nMax temperature list:\n"

for k,v in max_dict.items():
    temp_content += "%s %.0f\n" % (k, v)

temp_content += "AVG %.1f" %(sum_tem / sum_items)

try:
    with open('tem.txt', 'a+') as f:
        f.writelines(temp_content)
except:
    print "Error!!"
