# r+ a+ 下seek的不同

>>> f = open('hello.py', 'r+')
>>> print f.read()
hello
subin
haha

>>> f.tell()
17
>>> f.read()
''
>>> f.seek(0)
>>> f.read()
'hello\nsubin\nhaha\n'
>>> f.seek(0)
>>> f.read(1)
'h'
>>> f.tell()
1
>>> f.read(1)
'e'
>>> f.seek(5)
>>> f.read(1)
'\n'
>>> f = open('hello.py', 'a+')
>>> f.read()
'hello\nsubin\nhaha\n'
>>> f.write('\nhaha')
>>> f.read()
''
>>> f.seek(0)
>>> f.read()
'hello\nsubin\nhaha\n\nhaha'
>>> f.read()
''
>>> f.seek(5)
>>> f.read()
'\nsubin\nhaha\n\nhaha'
>>> f = open('hello.py', 'r+')
>>> f.seek(5)
>>> f.read()
'\nsubin\nhaha\n\nhaha'
>>> f.seek(5)
>>> f.seek(6)
>>> f.seek(0)
>>> f.read()
'hello\nsubin\nhaha\n\nhaha'
>>> f.seek(6)
>>> f.write('woniu')
>>> f.tell()
11
>>> f.read()
'\nhaha\n\nhaha'
>>> f.seek(0)
>>> print f.read()
hello
woniu
haha

haha
>>> f.tell()
22
>>> 
>>> 
>>> f = open('hello.py', 'a+')
>>> 
>>> 
>>> f.tell()
0
>>> f.read()
'hello\nwoniu\nhaha\n\nhaha'
>>> f.tell()
22
>>> f.seek(5)
>>> f.read()
'\nwoniu\nhaha\n\nhaha'
>>> 
>>> 
>>> 
>>> f.tell()
22
>>> f.seek(5)
>>> f.seek(6)
>>> f.write('subin')
>>> f.read()
''
>>> f.seek(0)
>>> f.read()
'hello\nwoniu\nhaha\n\nhahasubin'
>>> f.seek(6)
>>> f.tell()
6
>>> f.read()
'woniu\nhaha\n\nhahasubin
```