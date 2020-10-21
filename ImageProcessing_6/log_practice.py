# coding=utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt
 
img = cv2.imread("durant.jpg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
# 先通过高斯滤波降噪
gaussian = cv2.GaussianBlur(img, (3, 3), 0)
 
# 再通过拉普拉斯算子做边缘检测
dst = cv2.Laplacian(gaussian, cv2.CV_16S, ksize=3)
LOG = cv2.convertScaleAbs(dst)
 
# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
 
# 显示图形
titles = [u'原始图像', u'LOG算子']
images = [rgb_img, LOG]
for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
