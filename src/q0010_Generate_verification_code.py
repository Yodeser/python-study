# -*- coding: utf-8 -*-
# //todo
# Created 22:53, 2018/5/28 by Yodes Yang
# Generate a random letter in python: https://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python
# Codes From http://www.cnblogs.com/youmuchen/p/8300027.html
import string
import random
import numpy as np
import cv2


class VerificationCode(object):

    def __init__(self):
        pass

    @staticmethod
    def produce_code(char_num=5):
        str_range = string.ascii_letters + '0123456789'
        codes = "".join(random.choice(str_range) for i in range(char_num) if i < char_num)
        return codes

    @staticmethod
    def random_color():
        return np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)

    @staticmethod
    def random_pos(x_start, x_end, y_start, y_end):
        return (np.random.randint(x_start, x_end),
                np.random.randint(y_start, y_end))

    @staticmethod
    def generate():
        vc = VerificationCode
        x_pos = 0
        y_pos = 25
        line_num = 3
        img_width = 60
        img_height = 240
        codes = VerificationCode.produce_code()
        print(codes)

        img = np.random.randint(100, 200, (img_width, img_height, 3), np.uint8)
        # cv2.imshow("img", img)
        # Write the verification image
        for char in codes:
            cv2.putText(img, char,
                        (np.random.randint(x_pos, x_pos + 50), np.random.randint(y_pos, y_pos + 35)),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.5,
                        vc.random_color(),
                        2,
                        cv2.LINE_AA)
            x_pos += 45

        for i in range(line_num):
            img = cv2.line(img,
                           vc.random_pos(0, img_width, 0, img_height),
                           vc.random_pos(0, img_width, 0, img_height),
                           vc.random_color(),
                           np.random.randint(1, 2))

        cv2.imshow("img", img)
        cv2.waitKey(0)

        pass


if __name__ == '__main__':
    VerificationCode.generate()
