#_*_coding:utf-8_*_
import cv2  # opencv读取的格式是BGR
import numpy as np
import matplotlib.pyplot as plt  # Matplotlib读取的格式是RGB

img = cv2.imread('cat.jpg')

# img = cv2.imread('cat.jpg', 0)   #0 表示灰度图
# hist = cv2.calcHist([img], [0], None, [256], [0, 256])
# print(hist.shape)  #  (256, 1)
# plt.hist(img.ravel(), 256)
# plt.show()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.show()
