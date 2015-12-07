# coding: utf-8

# arr = [2, 7, 11, 15]
# num = 9
# arr[n1] + arr[n2] == num
# 求 n1 和 n2

def twoSum(arr, target):
    # arr = sorted(arr)
    # tmp1 = arr.pop(0)
    # n1 = 0
    # tmp2 = arr.pop(-1)
    # n2 = len(arr) - 1

    # print "n2: %d" % n2

    # while arr != []:
    #     # tmp1 = arr.pop(0)
    #     if tmp2 > target:
    #         tmp2 = arr.pop(-1)
    #         n2 -= 1
    #         continue

    #     if tmp1 + tmp2 < target:
    #         tmp1 = arr.pop(0)
    #         n1 += 1
    #         continue

    #     if tmp1 + tmp2 == target:
    #         break

    # print n1
    # print n2

    # dict 存放  arr[i]:i
    # 结果可以查字典
    # for i in range(len(arr)):
    #     n1 = i
    #     n2 = 
    #     if target


if __name__ == '__main__':
    arr = [2, 7, 11, 15]
    num = 9
    twoSum(arr, num)