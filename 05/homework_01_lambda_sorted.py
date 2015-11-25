# coding:utf-8

__author__ = "seerjk"

# 一个list[(1,4),(5,1),(2,3)],根据每个元组中的较大值进行排序
# 期待结果：[(2,3),(1,4),(5,1)]
# 要求：用sorted和lambda完成
# 级别1：用lambda中用max
# 级别2：lambda中不用max
# 提示：True乘以4 ==4 Fale乘以2 == 0sbbb
# print True*4
# print False*4

# level 1
num_list = [(1,4),(5,1),(2,3)]

max_func1 = lambda (x, y): max(x, y)

sorted_num_list = sorted(num_list, key=max_func1)
print sorted_num_list

# level 2
max_func2 = lambda (x, y): (x > y) * x or (x <= y) * y

sorted_num_list = sorted(num_list, key=max_func2)
print sorted_num_list


#######################
# >>> f4 = lambda x,y: max(x,y)
# >>> f4(2,3)
# 3
# >>> f5 = lambda x,y: (x > y)*x or (x <= y)*y
# >>> f5(4,5)
# 5
# >>> f5(5,4)
# 5
# >>> f5(5,5)
# 5