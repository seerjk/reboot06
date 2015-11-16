# coding:utf-8
'''
对 hello world    的list
先用：去拼接 为str
然后 替换: 为 空格
然后 查找o出现的次数
然后再以空格拆分  为list
'''

tmp_list = ['hello', 'world']

out1_str = ':'.join(tmp_list)
print out1_str

out2_str = out1_str.replace(':', ' ')
print out2_str

count_o = out2_str.count('o')
print "'o' appears %d times." % (count_o)

out3_list = out2_str.split(' ')
print out3_list
