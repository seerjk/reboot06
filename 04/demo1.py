# coding:utf-8

f = open('hello.py')

print f
f.close()

f = open('hello.py')
lines = f.readlines()

for line in lines:
    print line

f = open('文件.txt')
while f.read():
