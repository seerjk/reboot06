# coding:utf-8

# author:JiangKun
# Function: Insert sort

num_list = [88,0,1,2,3,123,11,123,421,-124,-2,3,4,5,6]
# num_list = range(3000)[::-1]

sorted_list = []

for i in num_list:
    if len(sorted_list) == 0:
        sorted_list.append(i)
    else:
        for j in sorted_list:
            if i <= j:
                pass
            elif i > j and 

