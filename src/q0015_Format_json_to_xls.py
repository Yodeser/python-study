# -*- coding: utf-8 -*-
# //todo
# Created 11:04, 2018/7/5 by Yodes Yang
from q0014_Format_data_to_xls import Object
import re


class JsonData(object):
    def __init__(self, data):
        self.data = data

    def format(self):
        # format the input data
        re_data = re.sub("\{\\s+|\\s+\}", "", self.data)
        re_data = re.sub(",\\s+", ", ", re_data)
        re_data = re.sub("\[|\]|\"|\"", "", re_data)
        result = re.split(", ", re_data)

        # get the value of row and column
        r = len(result)
        c = result[0].count(",") + result[0].count(":") + 1
        obj = Object(r, c)

        # extract values into the instance of Object
        for i in range(r):
            result[i] = re.sub(":", ",", result[i])
            obj.values[i] = re.split(" , ", result[i])
        return obj


if __name__ == '__main__':
    f = open("../data/0015/city.txt", 'r', encoding='utf8')
    input_data = str()
    try:
        input_data = f.read()
    except Exception as e:
        print(e)
    finally:
        f.close()
    pass

    jd = JsonData(input_data)
    jd.format().output_xls(r"../data/0015/city.xls")
