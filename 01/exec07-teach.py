#!/usr/bin/python env
while True:
    num = int(raw_input('please input a number: '))
    # if num % 100 == 0 and num % 400 == 0:
    # if num % 400 == 0:
    #     print 'OK'
    #     break
    
    # if num % 100 != 0 and num % 4 == 0:
    if num % 400 == 0 or (num % 100 != 0 and num % 4 == 0):
        print 'OK'
        break

    print 'NOT'
