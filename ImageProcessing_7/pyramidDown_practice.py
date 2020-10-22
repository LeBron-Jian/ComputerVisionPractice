# _*_coding:utf-8 _*_
import cv2
import numpy as np
import matplotlib.pyplot as plt
 
# 读取原始图片
img = cv2.imread('kd2.jpg')
 
# 图像向下取样
r1 = cv2.pyrDown(img)
r2 = cv2.pyrDown(r1)
r3 = cv2.pyrDown(r2)
 
# 为了方便将两张图对比，我们使用matplotlib
titles = ['origin', 'pyrDown1', 'pyrDown2', 'pyrDown3']
images = [img, r1, r2, r3]
for i in np.arange(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
