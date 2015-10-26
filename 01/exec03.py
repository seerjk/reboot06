num=0
size=0.0

input_str = raw_input('input a number(end with blank): ')
while input_str:
    if input_str.isdigit():
        size += 1
        num = num + int(input_str)
    else:
        print "%s is not a digit." % input_str

    input_str = raw_input('input a number(end with blank): ')

print "Average: %f" % (num / size)
