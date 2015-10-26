str_list = ['C','js','python','js','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node']

str_dict = {}

for s in str_list:
    if s in str_dict.keys():
    # if s in str_dict:
        str_dict[s] += 1
    else:
        str_dict[s] = 1

for key in str_dict:
    print '%s : %d' % (key, str_dict[key])
