# -*- coding:utf-8 -*-
# @Time     : 2017-02-19 12:34
# @Author   : GCK1D6O
# @Site     : 
# @File     : html_parser.py
# @Software : PyCharm
from bs4 import BeautifulSoup

class HtmlParser(object):

    def __init__(self):
        self.mm_urls = []
        self.image_urls = []

    def htmlparse(self, text):
        if text is None:
            return
        soup = BeautifulSoup(text, 'html.parser')
        mm_urls_html = soup.find_all(class_="tit")
        for mm_url in mm_urls_html:
            urls= mm_url.find('a')
            self.mm_urls.append(urls.get('href'))
        return self.mm_urls

    def htmlparse2(self, text2):
        if text2 is None:
            return
        soup = BeautifulSoup(text2, 'html.parser')
        urls = soup.find_all(id='picture')
        soup2 = BeautifulSoup(str(urls)[1:-1], 'html.parser')
        urls2 = soup2.find_all('img')
        for url in urls2:
            self.image_urls.append(url.get('src'))
        return self.image_urls