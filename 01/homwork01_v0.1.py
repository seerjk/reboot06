#!/usr/bin/env python
#coding=utf-8

num_list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]

max2 = max1 = num_list[0]
# print max1, max2
# max1 bigger than max2
# 1. n>max1 and n>max2
# 2. n<=max1 and n>max2
# 3. n<max1 and n<=max2

for n in num_list:
    if n > max1 and n > max2:
        max2 = max1
        max1 = n
    if n < max1 and n > max2:
        max2 = n

print "Two large numbers are: %d, %d" % (max1, max2)""

