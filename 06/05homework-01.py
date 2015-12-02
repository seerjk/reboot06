# coding: utf-8
mylist = [(1,4),(5,1),(2,3)]
print sorted(mylist, key=lambda (x,y): x*(x>y)+y*(x<=y))

a = [1,2,3]
b = [4,5,6]
c = ['hello']
# c.append(a)
# c.append(b)
c.extend([a, b])

print c