# coding:utf-8

# function dict.fromkeys
'''
fromkeys(...)
    dict.fromkeys(S[,v]) -> New dict with keys from S and values equal to v.
    v defaults to None.
'''

keys_list = ['name', 'age']
value = ''
value = None
# value = ['aa', 'bb']

#  ''  or  None 是不同的


dict1 = {}

for k in keys_list:
    dict1[k] = value

print dict1