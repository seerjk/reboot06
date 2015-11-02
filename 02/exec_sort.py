# conding:utf-8

arr = [88,0,1,2,3,123,11,123,421,-124,-2,3,4,5,6]
tmp = 0

# Bubble sort
# put the least to botom
# from small to big
for i in range(len(arr)):
    # print arr
    for j in range(i+1, len(arr)):
        if arr[j] < arr[i]:
            # tmp = arr[j]
            # arr[j] = arr[i]
            # arr[i] = tmp
            arr[i], arr[j] = arr[j], arr[i]

# print arr

# Bubble sort 2
# Best
# arr = [88,0,1,2,3,123,11,123,421,-124,-2,3,4,5,6]
arr = range(3000)[::-1]
# count = 0

#  attention: -1
for i in range(len(arr)-1):
    # print arr
    # if arr[i] > arr[i+1]:
    #     arr[i], arr[i+1] = arr[i+1], arr[i]
    # attention: -1-i
    for j in range(len(arr)-1-i):
        # count += 1
        if arr[j] > arr[j+1]:
            # exchange variables:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print arr
# print count

# imroved Bubble sort
arr = [2,1,2,3,4,5,7,8]
flag = True

for i in range(len(arr)-1):
    flag = False
    
    print arr
    # if arr[i] > arr[i+1]:
    #     arr[i], arr[i+1] = arr[i+1], arr[i]
    for j in range(len(arr)-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            flag = True

    if flag == False:
        break


# Bubble sort
# from big to small
arr = [88,0,1,2,3,123,11,123,421,-124,-2,3,4,5,6]
tmp = 0
# print arr_index

for i in range(len(arr)):
    # print arr
    for j in range(i+1, len(arr)):
        if arr[j] > arr[i]:
            tmp = arr[j]
            arr[j] = arr[i]
            arr[i] = tmp

# print arr

#####################################
# insert sort



#####################################
# Quick sort
def partition(sq_list, low, high):
    pivotkey = sq_list[low]

    while low < high:
        while low < high and sq_list[high] >= pivotkey:
            high -= 1
            pass
        pass

        sq_list[low], sq_list[high] = sq_list[high], sq_list[low]

        while low < high and sq_list[low] <= pivotkey:
            low += 1
            pass

        sq_list[low], sq_list[high] = sq_list[high], sq_list[low]

    return low
