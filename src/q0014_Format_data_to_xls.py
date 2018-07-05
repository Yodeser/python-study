# -*- coding: utf-8 -*-
# //todo
# Created 23:34, 2018/5/31 by Yodes Yang
# Read and write xml in Python3: https://blog.csdn.net/atfuies/article/details/78227510
import re
# 读写2003 excel
import xlrd
import xlwt


class Object(object):
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.values = [[0 for col in range(column)] for row in range(row)]

    def output_xls(self, name):
        wb = xlwt.Workbook()
        sheet = wb.add_sheet("SheetName")

        for i in range(self.row):
            for j in range(self.column):
                sheet.write(i, j, self.values[i][j])
        wb.save(name)


class Student(object):
    def __init__(self, input_data):
        self.input_data = input_data
        pass

    def format(self):
        # format the input data
        re_data = re.sub("\{\\s+|\\s+\}", "", self.input_data)
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
            obj.values[i] = re.split(",", result[i])

        return obj


if __name__ == '__main__':
    f = open("../data/0014/student.txt", 'r', encoding='utf8')
    data = str()
    try:
        data = f.read()
    except Exception as e:
        print(e)
    finally:
        f.close()
    pass

    stu = Student(data)
    stu.format().output_xls(r"../data/0014/student.xls")
