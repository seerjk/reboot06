# --coding:utf-8--

arr = [1,2,3]

# append() 后插 -- 修改原数组，没有返回值
print arr.append(4)
print arr

# 切片插入，插入到x的位置
# 切片实现append功能
arr[4:4] = [5]

arr_len = len(arr)
arr[arr_len:arr_len] = [7]

arr[len(arr):] = [7]

arr[-1:] = [arr[len(arr)-1],4]

print arr

# count(x) 统计list中x出现的次数
# 返回值，不修改list
arr = [1,1,1,1,2,3,5]
print arr.count(1)


# extend 合并list
# 无返回，修改原list
a = [1,2,3,4]
b = [5,6,7,8]

print a.extend(b)
print a
print b

# 实现extend
a = [1,2,3,4]
b = [5,6,7,8]
a = a + b
print a


# index
# 从列表中找出某个值，返回第一个匹配项的索引位置
# 不存在的话，会报错，可以先用in检测
arr = [1,2,'a',3,5,1,56,'a',45,234,6,'a',7,234]
print arr.index('a')

if 'b' in arr:
    print arr.index('b')
else:
    print "not exist."

print arr.index('a',3)


# exec06
# index version
arr = [1,2,3,4,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
find_num = 4
start_index = 0

if find_num in arr:
    start_index = arr.index(find_num)
if find_num in arr[start_index+1:]:
    print arr.index(find_num,start_index+1)

# for version
find_num = 4
count_find_num = 0

for i in range(len(arr)):
    if arr[i] == find_num:
        count_find_num += 1
        if count_find_num == 2:
            print "the second %d index is: %d" %(find_num, i)

# exec07
'''
add
    再输入事情
do
    打印一个事情

如果没有
'''

# insert
arr = [1,2,3,4,5]
# 查到2的位置
arr.insert(2,'hello')
arr.insert(2,['hello','reboot'])
print arr


# pop
# 返回值 + 修改list
arr = [1,2,3,4,5]
print arr.pop()
print arr

print arr.pop(2)
print arr

# haha
arr.append(arr.pop())
print arr

# 模拟队列、栈 使用函数 insert, append, pop
# FIFO 吃多了拉
# FILO 吃多了吐

# remove
# 不存在，会报错
arr = list('hello')
print arr
arr.remove('o')
print arr

# del
# 按索引删除
del arr[0]


# reverse
arr = list('hello')
print arr
arr.reverse()
print arr

# 切片 实现 reverse
print arr[::-1]

# append 
