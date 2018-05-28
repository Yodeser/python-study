# -*- coding: utf-8 -*-
# //todo
# Created 0:06, 2018/5/29 by Yodes Yang
from q0011_Filter_words import WordsFilter


class FilterText(WordsFilter):
    def __init__(self, file_route):
        WordsFilter.__init__(self, file_route)
        pass

    def replace(self, text):
        text = str(text)
        for word in self.words:
            if text.__contains__(word):
                text = text.replace(word, "*" * word.__len__())

        return text


if __name__ == '__main__':
    ft = FilterText("../data/0011/filtered_words.txt")
    print(ft.words)
    print(ft.replace("程序员的天堂，真心牛逼"))
    pass
