user_dict = {}

def update_data():
    f = open('user.txt')
    for l in f:
        if not l:
            continue

        temp = l.split()
        # print temp
        user_dict[temp[0]] = temp[1]

def update_file():
    f = open('user.txt', 'w')
    temp = []
    for user, pwd in user_dict.items():
        temp.append('%s %s\n' % (user, pwd))

    f.writelines(temp)
    f.close()

def get_form():
    return '''
        <form action="/add">
            Name:
            <input type="text" name="user">
            Password:
            <input type="password" name="pwd">
            <input type="submit" value="add">
        </form>        
    '''

def get_table():
    temp = '''
        <table border="1">
            <tr>
                <td>user</td>
                <td>pwd</td>
                <td>action</td>
            </tr>
    '''

    for user, pwd in user_dict.items():
        temp += '''
            <tr>
                <td>%s</td>
                <td>%s</td>
                <td><a href="/delete?user=%s">delete</a></td>
            </tr>
        ''' % (user, pwd, user)

    temp += '</table>'

    return temp

def get_html():
    return get_form() + get_table()