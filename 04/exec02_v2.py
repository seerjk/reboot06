# coding:utf-8
# tem.txt存储这日期和气温的数据，求最高温度和平局温度
# 11.12 7
# avg 4.1
# 结果还要存在原来文件的末尾


# 写代码要注意：每句话的影响
# * avg = sum / count 一定要考虑除数为0的情况

# 所有代码放到 try except 中，偷懒的方法

# 改进：
# [ ] 1. 文件为空，出现  0/0 报错，需要处理文件为空的情况
# [x] 2. 文件不存在, try -- catch
# [ ] 3. 多天最高温度相同  存入 dict
# [ ] 4. 11.11 6   00  情况需要考虑
# [x] 5. 温度全负数 清空
# 知道最高温度，就能知道日期了。只需要记住最高温度，然后在list中找

# tem_file = open('tem.txt')
# tem_content = tem_file.readlines()
# tem_file.close()

try:
    with open('tem.txt') as f:
        tem_content = f.readlines()
# except IOError as err:
except:
        print "File Error: %s" % (str(err))

if tem_content == []:
    print "Empty file."
    exit(1)

# 变量初始化要小心，初始化值会不会影响到计算，最好用第一个值去赋值
max_date = ''
max_tem = 0

# 2个以上最高温度相同，存入dict
# 改进  只记录最高温度，再去list中查找对应有多少天
# max_dict = {}

sum_tem = 0
sum_items = 0

for line in tem_content:
    # line = line.replace('\n', '')
    # temp_list = line.split(' ')
    # str.strip()  去除 '\n'
    temp_list = line.strip().split(' ')

    current_temp = float(temp_list[1])
    current_date = temp_list[0]

    sum_tem += current_temp
    sum_items += 1
    # 计数的好处 11.6 7 00101  异常情况可以剔除

    if max_date == '':
        max_date = current_date
        max_tem = current_temp
    elif current_temp > max_tem:
        max_date = current_date
        max_tem = current_temp


print "%s %.0f" % (max_date, max_tem)
print "avg: %.1f" %(sum_tem / sum_items)
