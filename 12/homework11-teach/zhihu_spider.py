# coding:utf-8
import requests
from pyquery import PyQuery as pq

import os,sys

reload(sys)
sys.setdefaultencoding('utf-8')

class ZhihuSpider():
    def __init__(self):
        self.url='http://www.zhihu.com/topic/19776749/top-answers?page=%s'
        self.answer_prefix = 'http://www.zhihu.com'
        self.new_urls = range(1, 3)
        self.result = []
        self.failed_urls = []

    def htmlParser(self, content):
        for main in pq(content).find('.feed-main'):
            t = pq(main).find('.question_link')
            tmp = {
                'title': t.html(),
                'url': self.answer_prefix + t.attr('href'),
                'vote': pq(main).find('.zm-item-vote-count').attr('data-votecount'),
                'content': pq(main).find('textarea.content').html()
            }
            self.result.append(tmp)
            # title
            
            # print t.html()
            # # question link
            # print self.answer_prefix + t.attr('href')
            # # question vote
            # print pq(main).find('.zm-item-vote-count').attr('data-votecount')

    def formatOutput(self):
        # 打印前10的
        for r in sorted(self.result, key=lambda x:-int(x['vote']))[:10]:
            print 'title is %s vote is %s url is %s content is %s' %(r['title'], r['vote'], r['url'], r['content'])

    def scrap_urls(self, urls_list):
        for u in urls_list:
            print self.url %(u)
            try:
                res = requests.get(self.url %(u))
                self.htmlParser(res.content)
            except:
                print 'page error %s please reconnect' %(u)
                self.failed_urls.append(u)

    def download(self):
        self.scrap_urls(self.new_urls)

        # 重试抓取失败的页面
        self.scrap_urls(self.failed_urls)

        # for u in self.new_urls:
        #     try:
        #         res = requests.get(self.url %(u))
        #         self.htmlParser(res.content)
        #     except:
        #         print 'page error %s please reconnect' %(u)
        #         self.failed_urls.append(u)
                # 重试
                # res = requests.get(self.url %(u))
                # self.htmlParser(res.content)
            # print self.url %(u)
    # def redownload_failed():
    #     # 重试抓取失败的页面
    #     for u in self.failed_urls:
    #         try:
    #             res = requests.get(self.url %(u))
    #             self.htmlParser(res.content)
    #         except:
    #             print 'page error %s' %(u)
    #         else:
    #             pass

    # class入口
    def init(self):
        self.download()
        self.formatOutput()


sp = ZhihuSpider()
sp.init()


