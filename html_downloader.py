# -*- coding:utf-8 -*-
# @Time     : 2017-02-19 12:27
# @Author   : GCK1D6O
# @Site     : 
# @File     : html_downloader.py
# @Software : PyCharm
import requests
import time

class HtmlDown(object):

    def __init__(self):
        self.image_urls = []
        self.heard = {'User-Agent':r'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
                 'Connection': 'keep-alive',
                 'Host':'www.meizitu.com'}
        self.heard2 = {'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
                 'Connection': 'keep-alive',
                 'Host': 'mm.howkuai.com'}

    def html_down(self, url):
        if url is None:
            return
        response = requests.get(url, headers=self.heard, timeout=5)
        response.encoding = 'gbk'
        return response.text

    def image_down(self, url2):
        if url2 is None:
            return
        image = requests.get(url2, headers=self.heard2, stream=True, timeout=5)
        image_name = str(int(time.time())) + '.jpg'
        with open("images\%s" %image_name, 'wb') as f:
            f.write(image.content)
            print("%s is down!" %image_name)