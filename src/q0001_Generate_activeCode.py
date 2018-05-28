# -*- coding: utf-8 -*-
# //todo
# Created 18:05, 2018/5/8 by Yodes Yang
# About charset's history, and above bytes and str in python3: https://blog.csdn.net/lyb3b3b/article/details/74993327
from numpy import random
import hashlib


class ActiveCode(object):

    @staticmethod
    def generate_code():
        size = 200
        ids = random.random_integers(10, 10000, size)
        ids = [str(i) for i in ids]

        var = hashlib.md5()
        hashlib.md5()
        for code in range(0, len(ids)):
            var.update(ids[code].encode("utf8"))
            ids[code] = var.hexdigest()
        return ids


if __name__ == '__main__':
    codes = ActiveCode.generate_code()
    print(codes)
