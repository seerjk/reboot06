# coding:utf-8

input_str = "user1:119,user2:112,user3:113"

s_list = input_str.split(',')
user_list = []

for i in s_list:
    tmp_list = i.split(':')
    tmp_tunple = tuple(tmp_list)
    user_list.append(tmp_tunple)
    # user_list.append(tuple(i.split(':')))

print user_list


'''
练习9:用户输入员工名字和id，名字和id之间用:分隔
多个用户 用逗号分隔
最终输入所有用户对应id的信息
比如用户输入user1:119,user2;112,user3:113
最终输出[('user2', '112'), ('user3', '113'), ('user1', '119')]
'''

user_input = raw_input("input name and id(user1:id1,...): ")
new_list = []
# 不好的习惯，不要在for中做split等操作
# 额外的性能开销
for value in user_input.split(','):
    new_list.append(tuple(value.split(':')))
print new_list