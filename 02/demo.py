# --coding:utf-8--

arr = ['C','python','js','css','html','node']


print arr

# 切片
# print arr[1:4]
# print arr[:3]
# print arr[2:]
# print arr[:]
# print arr[-2:]
# print arr[-3:-1]

arr = [1,2,3,4,5]
print arr[4:2]
# print [4:2:1]  默认 从左到右
print arr[4:2:-1]
# -1 从右向左
print arr[-1:-5]
print arr[-1:-5:-1]
print arr[-5:-1]


arr = list('helso')

# # arr[start:end:step]
# print arr[1:5:2]
# print arr[::-1]
# print arr[4:0:-2]
# print arr[1:5:-1]
# # 没有取到值

# # 奇数index
# print arr[1::2]
# # 偶数index
# print arr[::2]

# # 切片可以赋值
# # arr[1:4] = '1'
# # print arr

# # 插入值
# arr[1:1] = ['hello']
# # arr[0:0] = list('adf')
# arr[0:0] = ['a','d','e']
# print arr

# # 删除值
# arr[1:4] = []
# print arr

arr[0:2] = [55,22]
print arr

arr[1:1] = ['555']
print arr

arr = range(10)
print arr[10::-1]


