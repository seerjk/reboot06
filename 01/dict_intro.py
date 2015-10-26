# define a dict
user_info = {
        "name":'reboot',
        "age":20,
        "type":'python'
}

user_info['name'] = 'xiaoming'
user_info['adfd'] = 1
print 'name' in user_info
print 'naesss' in user_info

# print user_info['name']
# print user_info['age']
# user_list = ['reboot','xiaoming']

for key in user_info:
    # print key 
    # print '%s is %s ' % (key, user_info[key])
    print '%s is %s.' % (key, user_info[key])

