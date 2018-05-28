# -*- coding: utf-8 -*-
# //todo
# Created 23:47, 2018/5/28 by Yodes Yang


class WordsFilter(object):

    def __init__(self, file_route):
        words = []
        f = open(file_route, 'rt', encoding='utf8')
        try:
            words = f.read().split("\n")
        except Exception as e:
            print(e)
        finally:
            f.close()

        self.words = words

    def judge(self, word):
        if self.words.__contains__(word):
            result = 'Freedom'
        else:
            result = 'Human Rights'

        return result


if __name__ == '__main__':
    wf = WordsFilter("../data/0011/filtered_words.txt")
    print("程序员: ", wf.judge("程序员"))
    print("程序: ", wf.judge("程序"))
