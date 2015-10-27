#!/usr/bin/env python
#coding=utf-8

num_list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]

max2 = max1 = num_list[0]
# print max1, max2
# max1 bigger than max2
"""
if n > max2:
    if  n > max1:
        xxxxx
    elif n < max1:
        xxxxx
else:
    do nothing
"""

for n in num_list:
    if n > max2:
        if n > max1:
            max2 = max1
            max1 = n
        elif n < max1:
            max2 = n

print "Two large numbers are: %d, %d" % (max1, max2)

