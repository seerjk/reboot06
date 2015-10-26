num = ''
sum = 0

# while not num:
#     num = raw_input('input a number or end with pc : ')
#     if num == 'pc':
#         print 'Summary is %f' % sum
#         exit(0)
#     elif num != '':
#         sum = sum + float(num)
#         num = ''

while 1:
    num = raw_input('input a number: ')
    if num == 'pc':
        break
    sum = sum + float(num)

print "Summary is %f" % sum
