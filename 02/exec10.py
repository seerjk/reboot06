# --coding:utf-8--
# 求两个数组共同的值（去重）

# 1. 求共同的值
# 2. 去重

# way1
# set
arr1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
arr2 = [2,1,3,2,43,234,454,452,234,14,21,14]

arr1 = set(arr1)
arr2 = set(arr2)

arr_union = arr1 & arr2

arr_union = [i for i in arr_union]

print arr_union

# way2
arr1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]*1000
arr2 = [2,1,3,2,43,234,454,452,234,14,21,14]*1000

arr_union = []
for i in arr1:
    if i not in arr_union and i in arr2:
        arr_union.append(i)

print arr_union