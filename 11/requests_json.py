# coding:utf-8
import requests

def get_data():
    # post 获取数据
    url = "http://10.1.1.71:9092/"
    # res = requests.get(url)
    res = requests.post(url)

    # print res.content
    print res.json()
    for r in res.json():
        print "|%s|%s|%s|%s|" % (r[0], r[1], r[2], r[3])

get_data()

# 手动添加
# name = raw_input('input sever name: ')
# mem = raw_input('input sever mem size: ')
# end_date = raw_input('input sever end_date: ')

# url = 'http://10.1.1.71:9092/addhost?name=%s&mem=%s&end_date=%s' % (name, mem, end_date)

# res = requests.get(url)
# print res.content

# 手动删除
server_id = raw_input('input the server id to delete: ')
url = 'http://10.1.1.71:9092/delhost?id=%s' % (server_id)

res = requests.post(url)
print res.content

get_data()