# -*- coding: utf-8 -*-
# //todo
# Created 0:26, 2018/5/29 by Yodes Yang
import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
import urllib3


class GirlPhoto(object):
    def __init__(self, url):
        self.url = url
        self.request = requests.get(url)
        self.document = BeautifulSoup(self.request.content, 'html.parser')
        pass

    def images(self):
        output_url = "../data/0013/"

        count = 0
        # 提取img标签中的src属性——即图片url
        images = list(img.get('src') for img in self.document.find_all('img'))
        for image in images:
            if str(image).startswith("//"):
                image = "http:" + image

            # 格式化图片存储格式
            if image.endswith("jpg") or image.endswith("jpeg") or image.endswith("png") or image.endswith("gif"):
                img_uri = output_url + str(count) + image[image.rfind("."):]
            else:
                img_uri = output_url + str(count) + ".png"

            # print(image)
            urllib3.PoolManager().request('GET', image, preload_content=False)

            with open(img_uri, 'wb') as f:
                f.write(requests.get(image, verify=True).content)
                invalid = False
                global img
                try:
                    img = Image.open(img_uri)
                    # 针对尺寸进行限制
                    if img.size[0] <= 80 or img.size[1] <= 80:
                        invalid = True
                except OSError as err:
                    invalid = True
                finally:
                    f.close()
                    img.close()

                # 图片尺寸或格式不满足要求则删除
                if invalid:
                    os.remove(img_uri)

            count += 1
        return images

    def girls(self):

        pass


if __name__ == '__main__':
    gp = GirlPhoto("http://tieba.baidu.com/p/2166231880")
    print(gp.images())
    pass
