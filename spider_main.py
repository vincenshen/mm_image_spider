# -*- coding:utf-8 -*-
# @Time     : 2017-02-19 12:28
# @Author   : GCK1D6O
# @Site     : 
# @File     : spider_main.py
# @Software : PyCharm
import os
import sys

BASE_DIR = os.path.normcase(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                         os.path.pardir,
                                         ))
sys.path.append(BASE_DIR)

from image_spider import html_downloader
from image_spider  import html_parser


class Imange(object):

    def __init__(self):
        self.urls = []
        self.response = ""
        self.image_urls = html_parser.HtmlParser()
        self.mm_down = html_downloader.HtmlDown()

    def html_down(self, url):
        return self.mm_down.html_down(url)

    def url_parse(self, text):
        return self.image_urls.htmlparse(text)

    def url_parse2(self, text2):
        return self.image_urls.htmlparse2(text2)

    def image_down(self, url):
        self.mm_down.image_down(url)


def download(urls):
    for index_url in urls:
        try:
            html_text = image.html_down(index_url)
            mm_urls = image.url_parse(html_text)

            for mm_url in mm_urls:
                try:
                    print(mm_url)
                    html_text2 = image.html_down(mm_url)
                    image_urls = image.url_parse2(html_text2)

                    for image_url in image_urls:
                        try:
                            image.image_down(image_url)
                        except:
                            print("image download failed!")
                            continue
                except:
                    print("mm_url download failed!")
                    continue
        except:
            print("index_url download failed!")
            continue


if __name__ == '__main__':
    image = Imange()
    index_urls = []
    for i in range(1,12):
        index_urls.append('http://www.meizitu.com/a/xinggan_2_%s.html' %i)
    download(index_urls)

