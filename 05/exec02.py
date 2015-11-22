# coding:utf-8

def add_all_1(*nums):
    if len(nums) == 0:
        return 0
    
    result = 0

    for num in nums:
        num = str(num)
        print num
        if num.isdigit():
            result += int(num)
            print result

    return result

# float 1.3 result error

def add_all(*nums):
    # if len(nums) == 0:
    #     return 0
    result = 0
    for num in nums:
        try:
            num = float(num)
        except:
            return -1
            # pass
        else:
            result += num

    return result

print add_all(1,2,'abc')
print add_all('a', 'b')
print add_all()
print "%.3f" % (add_all(1.2, 1.3))

num_list = [1.2, 1.5, -5]
print "%.3f" % (add_all(*num_list))
