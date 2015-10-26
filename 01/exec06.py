num_list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
# max_num = 0
max_num = num_list[0]

for n in num_list:
    if n > max_num:
        max_num = n

print "The max number is %d." % max_num
