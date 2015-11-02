# --coding:utf-8--

# arr = [1,2,3,4,2,12,3,14,3,2,3,12,14,3,21,2,2,3,4111,22,3333,4]

# # 数据量很大，漏数据后面还会补上。


# for i in arr:
#     # print arr
#     while arr.count(i) > 1:
#         print "%d, %d" % (i, arr.count(i))
#         arr.remove(i)
#         # 会影响list 的 index

#         # del arr[]

# print arr

# way
# 推荐用新的list保存需要的结果，不要改变原来的list


# way2

num_list = [1,2,3,4,2,12,3,14,3,2,3,12,14,3,21,2,2,3,4111,22,3333,4]*10000
unique_list = []

for i in num_list:
    if i not in unique_list:
        unique_list.append(i)

print unique_list

# way3
num_list = [1,2,3,4,2,12,3,14,3,2,3,12,14,3,21,2,2,3,4111,22,3333,4]*10000
unique_dict = {}

for i in num_list:
    unique_dict[i] = 1

for key in unique_dict:
    print key