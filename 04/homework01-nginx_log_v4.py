# coding:utf-8
__author__ = "seerjk"

# v2.0
# 改进：应对超大日志文件，不用`readlines()`，一次性读入内存，改用迭代器读文件

# v3.0
# 增加排序，打印request_times 前十的

# v4.0
# 3 steps of dict

# 简单的nginx日志分析
# 日志文件在/home/shre/www_access_20140823.log
# 61.159.140.123 - - [23/Aug/2014:00:01:42 +0800] "GET /favicon.ico HTTP/1.1" 404 \ "-" "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36 LBBROWSER" "-"
# 期望输出一个list，分别存储这http状态，访问url，ip，访问次数，格式如下

# ip_addr http_status uri request_times
# [http_status, uri, (ip_addr, request_times)]

nginx_log_path = 'www_access_20140823.log'
log_access_dict = {}
# {(ip_addr, http_status, uri): request_times; }

try:
    with open(nginx_log_path) as f:
        count = 0
        for log_line_str in f:
            log_line_list = log_line_str.split(' ')

            ip_addr = log_line_list[0]
            http_status = log_line_list[8]
            uri = log_line_list[6]
            
            # log_access_key = (ip_addr, http_status, uri)

            # if log_access_key in log_access_dict:
            #     log_access_dict[log_access_key] += 1
            # else:
            #     log_access_dict[log_access_key] = 1
            if http_status in log_access_dict:
                http_status_dict = log_access_dict[http_status]
                if uri in http_status_dict:
                    uri_dict = http_status_dict[uri]

                    if ip_addr in uri_dict:
                        uri_dict[ip_addr] += 1
                    else:
                        uri_dict[ip_addr] = 1
                else:
                    # uri not in http_status_dict
                    http_status_dict[uri] = {ip_addr: 1}
            else:
                # http_status no in http_status_dict
                log_access_dict[http_status] = {uri: {ip_addr: 1}}

except:
    print "Error!!"

if log_access_dict == {}:
    print "Empty file!!"
    exit(0)

access_list = []

for http_status, http_status_dict in log_access_dict.items():
    for uri, uri_dict in http_status_dict.items():
        for ip_addr, request_times in uri_dict.items():
            # print [http_status, uri, (ip_addr, request_times)]
            access_list.append([http_status, uri, (ip_addr, request_times)])

def r_times(item_list):
    return item_list[2][1]

# 不要做全部排序，nlog(n)   只取前十个， 10*n
access_sorted_list = sorted(access_list, key = r_times, reverse = True)

# len 小于10 ，要判断
print access_sorted_list[:-10:-1]
for i in xrange(10):
    # print access_sorted_list[i][2], access_sorted_list[i][3]
    print access_sorted_list[i]
