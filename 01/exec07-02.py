while True:
    str_input = raw_input('input a year: ')
    if str_input.isdigit() == False:
        print "please input a year."
    else:
        year = int(str_input)
        if year % 4 == 0:
            if year % 100 == 0 and year % 400 == 0:
                print "%d is a leap year." % year
                break
            elif year % 100 != 0:
                print "%d is a leap year." % year
                break
            else:
                print "%d is not" % year
        else:
            print "%d is not a leap year." % year



