# coding:utf-8
__author__ = "seerjk"

# 简单的nginx日志分析
# 日志文件在/home/shre/www_access_20140823.log
# 61.159.140.123 - - [23/Aug/2014:00:01:42 +0800] "GET /favicon.ico HTTP/1.1" 404 \ "-" "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36 LBBROWSER" "-"
# 期望输出一个list，分别存储这http状态，访问url，ip，访问次数，格式如下

# ip_addr http_status request_url request_times
# [http_status, request_url, (ip_addr, request_times)]

nginx_log_path = 'www_access_20140823.log'

try:
    with open(nginx_log_path) as f:
        log_list = f.readlines()
        # log_list = f.xreadlines()
except:
    print "Error!!"
else:
    # main process
    if log_list == []:
        print "Empty file!!"
        exit(0)

    log_access_dict = {}
    # {[ip_addr, http_status, request_url]: request_times; }

    # for count
    for log_line_str in log_list:
        log_line_list = log_line_str.split(' ')
        ip_addr = log_line_list[0]
        http_status = log_line_list[8]
        request_url = log_line_list[6]
        log_access_key = (ip_addr, http_status, request_url)

        if log_access_key in log_access_dict:
            log_access_dict[log_access_key] += 1
        else:
            log_access_dict[log_access_key] = 1

    # for output access list
    for k,v in log_access_dict.items():
        output_list = [k[1], k[2], (k[0], v)]
        print output_list

# [Finished in 6.6s]