# coding:utf-8
import requests
from pyquery import PyQuery as pq

# 练习1 获取豆瓣电影top250的前的100电影的名称
# url = "https://movie.douban.com/top250"
# https://movie.douban.com/top250?start=0
# https://movie.douban.com/top250?start=25

for i in xrange(0, 99, 25):
    url = "https://movie.douban.com/top250?start=%d" %(i)
    # print url
    res = requests.get(url)
    j = i + 1
    for p in pq(res.content).find('.hd .title:first'):
        print str(j) + " " + p.text.encode('utf-8')
        j += 1


# res = requests.get(url)
# print res.content


# for p in pq(res.content).find('.title'):
# div .hd
#     div .title:first
# :first 伪类选择器

