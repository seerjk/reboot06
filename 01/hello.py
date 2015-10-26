#!/usr/bin/env python

# name = raw_input('input your name: ')
# print 'hello ' + name 

# 
# if name=='reboot':
#     print 'hello reboot'
# else:
#     print 'hehe'
#     print 'hello xxx'
# print '123'

x =raw_input('please enter your name: ')
if x=='WD':
    print 'you are a nice boy'
elif x=='PC':
    print 'you are a nice boy too'
else:
    print 'nice to meet you'

# print 'hello world'
# print 4+5
# 
# name = "jiangk"
# print name

# string
# print 'hello world'
# print "hello world"
# print 'hello' + 'python'
# print '*' * 30

# ' " '''
# #print 'I'm a person'
# print "I'm a person"
# print '''
# "adf ' adf'adf'adf
# adf;''
# '''

name = raw_input('input your name: ')
#print 'hello ' + name 
age=20
# print name+' is '+age+'years old.'
# TypeError: cannot concatenate 'str' and 'int' objects
# print name+' is '+str(age)+' years old.'

# print '%s is %s years old.' % (name, age)
print '%s is %d years old.' % (name, age)
