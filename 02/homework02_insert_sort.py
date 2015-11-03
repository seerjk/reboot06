# coding:utf-8

# author:JiangKun
# Function: Insert sort

# num_list = [88,0,1,2,3,123,11,123,421,-124,-2,3,4,5,6]
# num_list = [88,0,1,2,3,123,11,123,421,-124,-2,3,4,5,6,0,0,0]
# num_list = [1,1,1,1,1,1,1]
num_list = range(10000)[::-1]
# num_list = range(-100, 100, 2)[::-1]
# num_list = [1]

sorted_list = []

for i in range(len(num_list)):
    if len(sorted_list) == 0:
        sorted_list.append(num_list[i])
    else:
        for j in range(len(sorted_list)):
            if num_list[i] <= sorted_list[j]:
                sorted_list.insert(j, num_list[i])
                break
            elif j == len(sorted_list) - 1:
                sorted_list.insert(j+1, num_list[i])
                break

print sorted_list