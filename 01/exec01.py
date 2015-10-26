#!/usr/bin/env python

# print '2'+'4'
# # print 2+'4'
# # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print 2+int('4')

num1 = raw_input('input a number: ')
# num1 = float(num1)
num1 = int(num1)
num2 = raw_input('input a number: ')
# num2 = float(num2)
num2 = int(num2)

avg = (num1 + num2) / 2.0
print 'avgerage is %f' % (avg)
