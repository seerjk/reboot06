Arch_homework.md

http://www.51reboot.com/course/arch/

arch入学作业

入学试题：实现一个简单的资源下载器
实现一个多连接下载工工具,要求如下:
调用用方方式:./downloader.py url 下载线程数
多线程下载,每个线程对应一一个连接
下载可以用用最新版QQ安装包来测试:http://dldir1.qq.com/qqfile/qq/QQ7.1/14522/QQ7.1.exe
完成后发邮件至：pc@51reboot.com



Range: bytes=7300-56654519\r\n

参考

map
http://segmentfault.com/a/1190000000414339

模仿axel
http://smilejay.com/2014/05/python-mult-thread-downloading/

详细注释 pyget
http://www.oschina.net/code/snippet_932755_27634

[http range](http://www.cnblogs.com/Googler/archive/2010/08/19/1803700.html)


多线程下载原理
http://blog.csdn.net/zhuhuiby/article/details/6725951
http://blog.csdn.net/howlaa/article/details/21875991


requests doc
https://media.readthedocs.org/pdf/requests/latest/requests.pdf

http://requests-docs-cn.readthedocs.org/zh_CN/latest/user/quickstart.html#id5


![用Python Requests抓取知乎用户信息 2](http://zihaolucky.github.io/mutilthread-crawler/)


http://docs.python-requests.org/zh_CN/latest/api.html

class requests.Request(method=None, url=None, headers=None, files=None, data={}, params={}, auth=None, cookies=None, hooks=None)

指定headers

## httplib  How to download file using range of bytes?
Pass Range header with bytes=start_offset-end_offset as range specifier.

For example, following code retrieve the first 300 bytes. (0-299):

>>> import httplib
>>> conn = httplib.HTTPConnection('localhost')
>>> conn.request("GET", '/', headers={'Range': 'bytes=0-299'}) # <----
>>> resp = conn.getresponse()
>>> resp.status
206
>>> resp.status == httplib.PARTIAL_CONTENT
True
>>> resp.getheader('content-range')
'bytes 0-299/612'
>>> content = resp.read()
>>> len(content)
300
NOTE Both start_offset, end_offset are inclusive.

UPDATE

If the server does not understand Range header, it will respond with the status code 200 (httplib.OK) instead of 206 (httplib.PARTIAL_CONTENT), and it will send whole content. To make sure the server respond partial content, check the status code.

>>> resp.status == httplib.PARTIAL_CONTENT
True