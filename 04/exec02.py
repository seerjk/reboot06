# coding:utf-8
# tem.txt存储这日期和气温的数据，求最高温度和平局温度
# max: 11.12 7
# avg 4.1

tem_file = open('tem.txt')
tem_content = tem_file.readlines()
tem_file.close()

max_date = ''
max_tem = 0

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

    if max_date == '':
        max_date = current_date
        max_tem = current_temp
    elif current_temp > max_tem:
        max_date = current_date
        max_tem = current_temp

print "%s %.0f" % (max_date, max_tem)
print "avg: %.1f" %(sum_tem / sum_items)
