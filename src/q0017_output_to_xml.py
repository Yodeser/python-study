# -*- coding: utf-8 -*-
# //todo
# Created 11:53, 2018/7/5 by Yodes Yang
import xlrd


class XmlObject(object):

    def __init__(self, node_name, notes, brackets, file_route):
        self.node_name = node_name
        self.notes = notes
        self.brackets = brackets
        self.file_route = file_route
        self.data = str()

    def new_xml(self):
        data = str()
        data += "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<root>\n" \
                + "<" + self.node_name + ">\n"

        # 增加-备注
        data += "<!--\n"
        for i in range(len(self.notes)):
            data += "\t" + self.notes[i] + "\n"
        data += "-->\n"

        data += self.brackets[0] + "\n"
        data += self.extract_data()
        data += self.brackets[1] + "\n"

        # 补充-节点闭合标签
        data += "</" + self.node_name + ">" + "\n</root>"

        return data

    @staticmethod
    def is_number(char):
        try:
            float(char)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(char)
            return True
        except (TypeError, ValueError):
            pass

        return False

    # 区分字符串与数字
    def val(self, char):
        if XmlObject.is_number(char):
            return str(char)
        else:
            return "\"" + str(char) + "\""

    # 提取数据并格式化
    def extract_data(self):
        workbook = xlrd.open_workbook(self.file_route)
        sheet = workbook.sheet_by_index(0)

        row = sheet.nrows
        col = sheet.ncols

        # 是否包含索引
        has_index = True
        content = [[0 for c in range(col)] for r in range(row)]
        for i in range(row):
            for j in range(col):
                content[i][j] = sheet.cell_value(i, j)
                if content[i][0] != str(i + 1):
                    has_index = False

        # 是否单列
        is_single = has_index & (col == 2)

        result = str("")
        start = 0
        for i in range(row):
            if has_index:
                result = result + "\t\"" + str(content[i][0]) + "\" : "
                start = 1
            else:
                result = result + "\t"

            if not is_single:
                result = result + "["
            for j in range(start, col):
                result = result + self.val(content[i][j])
                if j != col - 1:
                    result = result + ", "
                else:
                    if not is_single:
                        result = result + "]"

            if i != row - 1:
                result += ",\n"
            else:
                result += "\n"

        return result


if __name__ == '__main__':
    student = XmlObject("students", ['学生信息表', '"id" : [名字, 数学, 语文, 英文]'],
                        ['{', '}'], r"../data/0014/student.xls")
    with open('../data/0014/student.xml', 'w', encoding='utf8') as f:
        f.write(student.new_xml())
        f.close()
