# -*- coding: utf-8 -*-
# //todo
# Created 14:42, 2018/5/26 by Yodes Yang
# Tf-idf algorithm: http://blog.yodes.cn/post/631f.html
import math
import os
from q0004_Word_Count import WordCount


class WordsImportance(object):
    idf = {}
    tf_idf = {}

    def __init__(self, path_name):
        self.file_path = str(path_name)
        self.files = os.listdir(self.file_path)
        pass

    def cal_idf(self, word):
        count = 0
        for file in self.files:
            f = open(self.file_path + file, 'r', encoding='utf8')
            text = ""
            try:
                text = f.read().encode("utf8")
            except ValueError as err:
                print(err)
                pass
            finally:
                f.close()

            text = WordCount.format_str(text)
            if word in text:
                count += 1
            else:
                # print("原文中不包含：", word)
                # print("原文为：", text)
                pass

        val = count / float(self.files.__len__())

        if count != 0:
            self.idf[str(word)] = math.log10(val)
        else:
            print("word:", word)
            self.idf[str(word)] = 0
            pass

        return self.idf[word]

    def cal_tf_idf(self):
        text = str("")
        for file in self.files:
            f = open(self.file_path + file)
            try:
                bytes_str = f.read().encode("utf8")
                text += WordCount.format_str(bytes_str)
            except ValueError as err:
                print(err)
            finally:
                f.close()

        tf = WordCount(text).count_tf()
        # print(tf)
        for word in tf:
            self.cal_idf(word)
            # print(self.idf[word])
            # print(tf[word])
            self.tf_idf[word] = self.idf[word] * tf[word]

    def word2vec(self):
        pass


if __name__ == '__main__':
    diary_path = "../data/0006/"

    wi = WordsImportance(diary_path)
    wi.cal_tf_idf()
    results = sorted(wi.tf_idf.items(), key=lambda d: d[1], reverse=False)
    for item in results:
        print(item[0], item[1])
    pass
