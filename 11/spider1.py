# coding:utf-8
import requests
from pyquery import PyQuery as pq

# url = "https://www.zhihu.com/people/auxten/answers"
url = "https://movie.douban.com/top250"


res = requests.get(url)
# print res.content

i = 1
# for p in pq(res.content).find('.title'):
# div .hd
#     div .title:first
# :first 伪类选择器
for p in pq(res.content).find('.hd .title:first'):
    # print p
    # print dir(p)
    # print p.text
    # print p.text.encode('utf-8')
    # if i % 2 == 0:
    print str(i) + " " + p.text.encode('utf-8')
    i += 1
