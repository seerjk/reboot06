# conding:utf-8

task_list = []
start_point = 0

while True:
    str_input = raw_input('please input add or do: ')

    if str_input == 'add':
        str_input = raw_input('please input a task: ')
        task_list.append(str_input)

        print task_list[start_point:]

        # continue
        pass

    elif str_input == 'do':
        if start_point < len(task_list):
            print "TO DO: %s" % task_list[start_point]
            start_point += 1
        else:
            print "There is nothing in to-do list."
            break

        # continue
        pass

    else:
        print 'Input error, please input add or do.'
        pass
