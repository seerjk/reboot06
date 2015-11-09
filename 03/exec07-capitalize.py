# coding:utf-8

# 练习7：实现首字母大写的功能 其他字母小写
# function: capitalize

# way 1st:
a_str = 'fadfILILafLIk'
a_list = list(a_str)

for i in xrange(len(a_list)):
    if i == 0:
        a_list[i] = a_list[i].upper()
    else:
        a_list[i] = a_list[i].lower()

cap_str = ''.join(a_list)

print cap_str

# way 2nd:
a = 'fadfILILafLIk'
b = ''
b = a[0].upper() + a[1:].lower()
print b

# Wrong way
# 'IaaaIaaaIaaa' 和首字母相同的都会转变为大写
# a='index'
# str_list = []
# for i in a:
#   if a.index(i) == 0:
#     str_list.append(i.upper())else:
#     str_list.append(i.lower())
# print ''.join(str_list)
