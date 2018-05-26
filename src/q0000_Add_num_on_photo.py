# -*- coding: utf-8 -*-
# //todo
# Created 12:15, 2018/5/8 by Yodes Yang
# from skimage import io
from cv2 import *

# 文件路径
imgUrl = "../data/0000/favicon.png"
outputUrl = "../data/0000/favicon_notice.png"

img = cv2.imread(imgUrl)
cv2.imshow("img", img)

(height, weight) = img.shape[0:2]

# 需添加文字的相关属性
fontStr = "5"
fontScale = 2
fontSize = 30 * fontScale

cv2.putText(img, fontStr, (weight - fontSize, fontSize), cv2.FONT_HERSHEY_SIMPLEX, fontScale, (0, 0, 255))

cv2.imshow("TextImage", img)
cv2.imwrite(outputUrl, img)

cv2.waitKey(0)
cv2.destroyAllWindows()
