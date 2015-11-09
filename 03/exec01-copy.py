# coding:utf-8

# copy function
src_dict = {'wd': 123, 'subin': 145, 'woniu': 114}
dst_dict = {}

for k in src_dict:
    dst_dict[k] = src_dict[k]

print dst_dict
print "id of src_dict: ", id(src_dict)
print "id of dst_dict: ", id(dst_dict)


