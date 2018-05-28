# -*- coding: utf-8 -*-
# //todo
# Created 22:03, 2018/5/25 by Yodes Yang
# Basic data type in python3: https://blog.csdn.net/xiaokang123456kao/article/details/72904851
# python3 reg expressions: http://www.runoob.com/python3/python3-reg-expressions.html
import re


class WordCount(object):
    def __init__(self, text):
        self.text = self.format_str(text)

    # print(self.text)

    @staticmethod
    def format_str(text):
        if isinstance(text, bytes):
            text = text.decode("utf8")
        elif isinstance(text, str):
            pass
        else:
            print("格式有误，请调整")

        result = text.strip().replace("\r", " ").replace("\n", " ").lower()
        return re.sub("[^a-z0-9A-Z]+", " ", result)

    def count_tf(self):
        word_dict = {}

        words = re.split("\\s+", self.text)
        for word in words:
            if word == '':
                break
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1

        return word_dict

    def sorted_tf(self):
        word_dict = self.count_tf()
        word_dict = sorted(word_dict.items(), key=lambda d: d[1], reverse=True)
        return word_dict


if __name__ == '__main__':
    f = test_str = "Hello World"
    try:
        f = open("../data/0004/Pride and Prejudice .txt", "rt")
        test_str = f.read()
    except Exception as e:
        print(e)
    finally:
        f.close()

    word_count = WordCount(test_str.encode("utf8"))
    tf = word_count.count_tf()
    # tf = word_count.sorted_tf()
    print(tf)
