# -*- coding: utf-8 -*-
# //todo
# Created 19:16, 2018/7/5 by Yodes Yang
from q0017_output_to_xml import XmlObject

if __name__ == '__main__':
    numbers = XmlObject("numbers", ['数字信息'],
                     ['[', ']'], r"../data/0016/numbers.xls")
    with open('../data/0016/numbers.xml', 'w', encoding='utf8') as f:
        f.write(numbers.new_xml())
        f.close()
