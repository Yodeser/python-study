# -*- coding: utf-8 -*-
# //todo
# Created 18:24, 2018/5/28 by Yodes Yang
import requests
from bs4 import BeautifulSoup


class HtmlParser(object):

    def __init__(self, target):
        self.html = BeautifulSoup(requests.get(url=target).content, 'html.parser')
        pass

    def body(self):
        b = self.html.find('body')
        return b


if __name__ == '__main__':
    body = HtmlParser("https://www.yodes.cn/").body()
    print(body)
