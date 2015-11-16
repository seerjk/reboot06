# coding:utf-8

'''
1.读取一个文件 lianxi
2.请输出其内容。
3.请去除该文本的换行。
4.请替换其中的字符"reboot"为"hello"。
5.复制这个文件，把第二行内容换为'wd'
'''

f = open('lianxi')

print "---1---"
print "read file"
# 1.
file_content = f.read()

print "---2---"
# 2.
print file_content

print "---3---"
# 3.
# content_str = file_content.replace('\n', ' ')
# 去掉换行，用空来替换，不是空格
content_str = file_content.replace('\n', '')
print content_str
f.close()

print "---4---"
# 4. reboot --> hello
# f = open('lianxi')
# for line in f.readlines():
#     line = line.replace('reboot', 'hello')
#     print line

# f.close()

## 注意下面的情况
'''
aa re
boot bb
'''
print content_str.replace('reboot', 'hello')


print "---5---"
# 5.
# f_read = open('lianxi')
# # 复制文件，用w模式
# # f_write = open('output.dat', 'a')
# f_write = open('output.dat', 'w')
# count_line = 0

# for line in f_read.readlines():
#     count_line += 1
#     if count_line == 2:
#         f_write.write('wd\n')
#     else:
#         f_write.write(line)

# f_write.close()
# f_read.close()

# version2
f_read = open('lianxi')
f_write = open('output.dat', 'w')

# file.readlines() --return a list
content_list = f_read.readlines()
content_list[1] = "wd\n"
f_write.writelines(content_list)

f_write.close()
f_read.close()

# print output.dat
f = open('output.dat')
print f.read()
f.close()




