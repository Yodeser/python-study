# -*- coding: utf-8 -*-
# //todo
# Created 19:02, 2018/7/5 by Yodes Yang
from q0017_output_to_xml import XmlObject

if __name__ == '__main__':
    city = XmlObject("cities", ['城市信息'],
                     ['{', '}'], r"../data/0015/city.xls")
    with open('../data/0015/city.xml', 'w', encoding='utf8') as f:
        f.write(city.new_xml())
        f.close()
