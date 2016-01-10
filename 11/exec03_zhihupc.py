# coding:utf-8
import requests
from pyquery import PyQuery as pq

# import sys
# sys_type = sys.getfilesystemencoding()


# 打印前2页 知乎pc的回答的问题和答案

q_num = 1
for i in range(1, 3):
    url = "https://www.zhihu.com/people/auxten/answers?page=%d" %(i)
    print url
    res = requests.get(url)
    print res.encoding
    # print type(pq(res.content).find('.zm-item'))
    
    for p in pq(res.content).find('.zm-item'):
        print type(p)
        # p.text.encode('utf-8')
        print q_num, pq(p).find('.question_link').text()
        print '-'*4 + pq(p).find('.summary').text()
        # print '-'*4 + pq(p).find('.summary').text.encode('utf-8')
        # AttributeError: 'function' object has no attribute 'encode'

        q_num += 1

