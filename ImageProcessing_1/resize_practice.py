import cv2
import os
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("cat.jpg")
# resize的插值方法：正常情况下使用默认的双线性插值法
res_img = cv2.resize(img, (200, 100))
res_fx = cv2.resize(img, (0, 0), fx=0.5, fy=1)
res_fy = cv2.resize(img, (0, 0), fx=1, fy=0.5)
print('origin image shape is ',img.shape)
print('resize 200*100 image shape is ',res_img.shape)
print('resize  0.5:1 shape is ',res_fx.shape)
print('resize  1:0.5  image shape is ',res_fy.shape)
'''
origin image shape is  (414, 500, 3)
resize 200*100 image shape is  (100, 200, 3)
resize  0.5:1 shape is  (414, 250, 3)
resize  1:0.5  image shape is  (207, 500, 3)
'''

# 标题
title = ['Origin Image', 'resize200*100', 'resize_fx/2', 'resize_fy/2']
# 对应的图像
image = [img, res_img, res_fx, res_fy]

for i in range(len(image)):
    plt.subplot(2, 2, i+1), plt.imshow(image[i])
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])
plt.show()
