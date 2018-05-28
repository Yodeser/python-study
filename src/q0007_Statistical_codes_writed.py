# -*- coding: utf-8 -*-
# //todo
# Created 15:19, 2018/5/28 by Yodes Yang
# The '__pycache__' folder in python3: https://blog.csdn.net/index20001/article/details/73501375
import os


class CodesCount(object):
    lines_code, lines_remark, lines_blank = 0, 0, 0

    def __init__(self, input_dir):
        self.file_dir = input_dir
        self.files = os.listdir(input_dir)

    # 开始统计
    def statistics(self):
        global f
        for filename in self.files:
            # python runtime-cache needs to ignore
            if filename.__eq__('__pycache__'):
                continue
            try:
                f = open(self.file_dir + filename, 'rt', encoding='utf8')
                for line in f:
                    self.distinguish(line)
            except Exception as e:
                print(e)
            finally:
                f.close()

    # 识别代码行的性质
    def distinguish(self, text):
        text = text.strip()
        if text.startswith("#"):
            self.lines_remark += 1
        elif text.__len__() == 0:
            self.lines_blank += 1
        else:
            self.lines_code += 1


if __name__ == '__main__':
    cc = CodesCount("../src/")
    cc.statistics()
    c, r, b = cc.lines_code, cc.lines_remark, cc.lines_blank
    a = c + r + b
    print("总行数：", a)
    print("代码行数：", c, "\t比例为：", c / a)
    print("注释行数：", r, "\t比例为：", r / a)
    print("空行数：", b, "\t比例为：", b / a)
