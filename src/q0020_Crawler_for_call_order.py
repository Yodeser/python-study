# -*- coding: utf-8 -*-
# //todo
# Created 19:19, 2018/7/5 by Yodes Yang
# Draw a histogram, pie chart, and dynamic map using matplotlib in python 3
import requests
import matplotlib.pyplot as plt
import xlrd
from pylab import mpl
import time


class CallOrder(object):
    def __init__(self):
        pass

    def download_order(self):
        request_url = "http://iservice.10010.com/e3/static/query/callDetail?_=1530853583856&accessURL=http://iservice.10010.com/e4/query/bill/call_dan-iframe.html?menuCode=000100030001&1530853549373&menuid=000100030001"
        headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                   'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                   'Cookie': '_n3fa_cid=676b0d8fca4a4b6cf4b519ed95e8001c; _n3fa_ext=ft=1530789709; _n3fa_lvt_a9e72dfe4a54a20c3d6e671b3bad01d9=1530789709; Hm_lvt_9208c8c641bfb0560ce7884c36938d9d=1530789710; _ga=GA1.3.408201538.1530789710; _gid=GA1.3.365870661.1530789710; piw=%7B%22login_name%22%3A%22156****2971%22%2C%22nickName%22%3A%22%E6%9D%A8%E5%85%B4%E5%9F%BA%22%2C%22rme%22%3A%7B%22ac%22%3A%22%22%2C%22at%22%3A%22%22%2C%22pt%22%3A%2201%22%2C%22u%22%3A%2215616112971%22%7D%2C%22verifyState%22%3A%22%22%7D; mallflag=null; clientid=51|510; SHOP_PROV_CITY=; mallcity=85|850; userprocode=085; citycode=850; WT_FPC=id=2ad59555a1c93cc2cde1530328637698:lv=1530845681508:ss=1530845673373; _uop_id=c63fecd047315a90ad4e9afbfbb2d520; cien=; route=43570585a4ad57ccc6b66755a006d276; e3=pbkSb2fLQQtljPbcBhlLg8tWlvHmS2v4YfntYxSrkDJJPjMv4pXt!-1921969814; loginflag=true; MII=000100030001; JUT=sjjKfbAUpN8bWO91I6xQu0CHzIRmD9fkJZdjO038VDUoECg46tRXrQE7Ls2I3in4ntzEQG0CqFTVjTs9csH307NE5UBOXUg1xlItQ+V0Dg36kTVEP8ZMhSBRdqQ7B/gJEsIeCf6YdgBmrte5P5KPKiVLVc3X5e+CFpkLvIFgiP4IUjO95ifU4z1wUbzL4Ei009qOMxzO9TnhA4jNfP+zwnIjdyml/S6OmMXMeiKGuZ2W++q2zYdH0UVErEcTPxE0t5w+1eBN8QVAAdG2bD/G9fOZzgjn2yUGWBnwxuFWiCFk2KRyfkDOvliE+XD2ob0yGWHTOC9QZyA8Et7t3v13kPDbLReaUQRq1lbt6QIxt+RAx8p5txvRod4NJa6Hsq6SY5ARD6CaJCtNcV1de+WujWuM9Uwifr2KoY9rxuvVLQrkvl/hCyJ/PuMDY4RTREVjFjguvB1u7i82M2modpI2Ab++7L1gtmPwd0V99QUjStrYPiOjDFsQLy+IS487fokz0XK83Bgnfmu0unCyS/KejhRIRomu4EdRH/0neoVyb2q8w23pZjzK4A==',
                   'Host': 'iservice.10010.com',
                   'Origin': 'http://iservice.10010.com',
                   'Referer': 'http://iservice.10010.com/e4/query/bill/call_dan-iframe.html?menuCode=000100030001',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
                   'X-Requested-With': 'XMLHttpRequest'}
        datas = {'pageNo': 1, 'pageSize': 20, 'beginDate': '20180601', 'endDate': '20180630'}
        result = requests.post(request_url, data=datas, headers=headers)
        print(result.status_code)
        pass

    @staticmethod
    def statistics(list_data):
        list_data = list(list_data)
        print(list_data)
        dict_data = dict()
        for i in range(len(list_data)):
            if dict_data.keys().__contains__(list_data[i]):
                dict_data[list_data[i]] += 1
            else:
                dict_data[list_data[i]] = 1

        return dict_data

    def analyze(self, file_route, sheet_name, focus_item):
        workbook = xlrd.open_workbook(file_route)
        sheet = workbook.sheet_by_name(sheet_name)

        index = 7
        for i in range(sheet.ncols):
            if str(focus_item).__eq__(sheet.cell_value(0, i)):
                index = i
                break

        # 设置原始数据
        source_data = CallOrder.statistics(sheet.col_values(index, 1, sheet.nrows))
        print(source_data)

        mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
        mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

        labels = list(source_data.keys())  # 设置标签
        fracs = [x for x in source_data.values()]
        explode = [x * 0.03 for x in range(len(source_data))]  # 与labels一一对应，数值越大离中心区越远
        plt.axes(aspect=1)  # 设置X轴 Y轴比例

        # labeldistance标签离中心距离  pctdistance百分百数据离中心区距离 autopct 百分比的格式 shadow阴影
        plt.pie(x=fracs, labels=labels, explode=explode, autopct='%3.1f %%',
                shadow=False, labeldistance=1.1, startangle=0, pctdistance=0.8, center=(-1, 0))

        # 控制位置：bbox_to_anchor数组中，前者控制左右移动，后者控制上下。ncol控制 图例所列的列数。默认值为1。
        plt.legend(loc=7, bbox_to_anchor=(1.2, 0.80), ncol=3, fancybox=True, shadow=True, fontsize=8)
        plt.show()


if __name__ == '__main__':
    CallOrder().analyze('../data/0020/2018年06月语音通信.xls', '2018年06月语音通信', '对方归属地')
