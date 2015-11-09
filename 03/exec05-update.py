# coding:utf-8

# function dict.update()
a_dict = {'subin': None, 'wd': 3, 'woniu': None, 'xuegao': 10}
b_dict = {'subin': 1, 'ada': 2}

for k in b_dict:
    a_dict[k] = b_dict[k]

print a_dict
