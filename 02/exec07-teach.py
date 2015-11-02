# conding:utf-8

todo_list = []

while True:
    action = raw_input('please input add or do: ')

    if action == 'add':
        work = raw_input('input you want to do: ')
        todo_list.append(work)
    elif action == 'do':
        print todo_list
        del todo_list[0]
        if len(todo_list) == 0:
            print 'end'
            break
