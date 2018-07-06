# -*- coding: utf-8 -*-
# //todo
# Created 10:21, 2018/5/26 by Yodes Yang
# Basic image operation in python3 using open-cv2: https://www.jianshu.com/p/40206f0a6658
import os
import cv2


class ResizeImage(object):
    def __init__(self):
        pass

    @staticmethod
    def load(weight=640, height=1135):
        original_path = "../data/0005/original/"
        modified_path = "../data/0005/modified/"

        files = os.listdir(original_path)
        for file in files:
            img = cv2.imread(original_path + file)
            output_path = modified_path + file
            (h, w, c) = img.shape

            # get the zoom size
            if w > weight:
                n = weight / float(w)
                new_size = (weight, int(n * h))
            elif h > height:
                n = height / float(h)
                new_size = (int(n * w), height)
            else:
                new_size = (w, h)

            res = cv2.resize(img, new_size, interpolation=cv2.INTER_AREA)
            cv2.imwrite(output_path, res)
            cv2.waitKey(0)


if __name__ == '__main__':
    ResizeImage.load()
