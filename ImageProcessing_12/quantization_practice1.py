#_*_coding:utf-8_*_
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
img = cv2.imread('kd2.jpg')
# 获取图像的高度和宽度
height, width = img.shape[0], img.shape[1]

# 创建一幅图像，内容使用零填充
new_img = np.zeros((height, width, 3), np.uint8)

# 图像量化操作，量化等级为2
for i in range(height):
    for j in range(width):
        for k in range(3):  # 对应BGR三通道
            if img[i, j][k] < 128:
                gray = 0
            else:
                gray = 129
            new_img[i, j][k] = np.uint8(gray)

# 显示图像
cv2.imshow('src', img)
cv2.imshow('new', new_img)
# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
