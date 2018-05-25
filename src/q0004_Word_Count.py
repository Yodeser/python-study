# -*- coding: utf-8 -*-
# //todo
# Created 22:03, 2018/5/25 by Yodes Yang
# Basic data type in python3: https://blog.csdn.net/xiaokang123456kao/article/details/72904851
# python3 reg expressions: http://www.runoob.com/python3/python3-reg-expressions.html
import re


class WordCount(object):
    def __init__(self, text):
        self.text = str(text)
        # self.text = re.sub("[^a-z0-9A-Z\\s]+", " ", str(text).replace("\\r", " ").replace("\\n", " "))

    def count(self):
        word_dict = {}

        words = re.split("\\s+", self.text)
        for word in words:
            if word == '':
                break
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1

        word_dict = sorted(word_dict.items(), key=lambda d: d[1], reverse=True)
        print(word_dict)


f = test_str = "Hello World"
try:
    f = open("../data/0004/Pride and Prejudice .txt", "rt")
    test_str = f.buffer.read()
except Exception as e:
    print(e)
finally:
    f.close()

word_count = WordCount(test_str)
word_count.count()
