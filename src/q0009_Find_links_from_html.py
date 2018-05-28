# -*- coding: utf-8 -*-
# //todo
# Created 19:13, 2018/5/28 by Yodes Yang
# Extract links from html in python3: https://www.zybuluo.com/bergus/note/232331
from q0008_Analyze_html_structure import HtmlParser


class HtmlAnalyze(HtmlParser):
    def __init__(self, target):
        HtmlParser.__init__(self, target)

    def urls(self):
        url_list = []
        tags = self.html.find_all("a")
        for tag in tags:
            u = tag.attrs['href']
            if str(u).startswith('#') or str(u).startswith("/"):
                u = self.request.url + u
            elif str(u).strip().__len__() == 0:
                continue
            else:
                pass

            url_list.append(u)

        return url_list


if __name__ == '__main__':
    urls = HtmlAnalyze("https://www.yodes.cn").urls()
    for url in urls:
        print(url)
