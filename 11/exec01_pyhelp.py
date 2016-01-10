# coding:utf-8

a={}
help_list = dir(a)

for i in help_list:
    if not i[:2] == '__':
        print i

# print help_list