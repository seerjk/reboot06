import time

s = "abcde"*1024*1024*30

# while True:
#     start_time = int(time.time())
for i in s:
    for j in s:
        s.count(j)