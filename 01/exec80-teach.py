arr_list = ['C','js','python','js','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node']

res = {}

for name in arr_list:
    if name in res:
        res[name] += 1
    else:
        res[name] = 1

for r in res:
    print '%s count is %s times.' %(r, res[r])
print res

'''
{
    'js':20
    'python':2
}
'''
