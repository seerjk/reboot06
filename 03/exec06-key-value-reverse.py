# coding:utf-8

'''
练习6：把一个dict的key和value反转
（如果value有重复的，把多个key，放在list）
提示：判断是否list
print isinstance([1,2,3],list)
print type([1,2]) == type([])
比如{'teach':'pc','waihao':'pc','name':'pc','age':12,'job':'IT'}
期望输出 {'pc': ['teach', 'waihao', 'name'], 12: 'age', 'IT': 'job'}

补充：需要还能反转回来
'''

a_dict = {'teach':'pc','waihao':'pc','name':'pc','age':12,'job':'IT'}

rev_dict = {}

# reverse dict

for k in a_dict:
    rev_k = a_dict[k]
    rev_v = k

    if rev_dict.has_key(rev_k):
        if type(rev_dict[rev_k]) == type([]):
        # if type(rev_dict[rev_k]) == type(list): #Error
            # append to list
            rev_dict[rev_k].append(rev_v)
        else:
            # str --> list
            tmp_str = rev_dict[rev_k]
            rev_dict[rev_k] = []
            rev_dict[rev_k].append(tmp_str)
            rev_dict[rev_k].append(rev_v)
    else:
        rev_dict[rev_k] = rev_v

print rev_dict


# revser rev_dict to normal

nor_dict = {}

for k in rev_dict:
    nor_k = rev_dict[k]
    nor_v = k
    
    if isinstance(nor_k, list):
        for sub_k in nor_k:
            nor_dict[sub_k] = nor_v
    else:
        nor_dict[nor_k] = nor_v

print nor_dict
    