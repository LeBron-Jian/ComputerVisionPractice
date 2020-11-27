# _*_coding:utf-8_*_
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
img = cv2.imread('kd2.jpg')
# 获取图像的高度和宽度
height, width = img.shape[0], img.shape[1]

# 创建一幅图像，内容使用零填充
new_img1 = np.zeros((height, width, 3), np.uint8)
new_img2 = np.zeros((height, width, 3), np.uint8)
new_img3 = np.zeros((height, width, 3), np.uint8)

# 图像量化操作，量化等级为2
for i in range(height):
    for j in range(width):
        for k in range(3):  # 对应BGR三通道
            if img[i, j][k] < 128:
                gray = 0
            else:
                gray = 129
            new_img1[i, j][k] = np.uint8(gray)

# 图像量化操作，量化等级为4
for i in range(height):
    for j in range(width):
        for k in range(3):  # 对应BGR三通道
            if img[i, j][k] < 64:
                gray = 0
            elif img[i, j][k] < 128:
                gray = 64
            elif img[i, j][k] < 192:
                gray = 128
            else:
                gray = 192
            new_img2[i, j][k] = np.uint8(gray)

# 图像量化操作，量化等级为8
for i in range(height):
    for j in range(width):
        for k in range(3):  # 对应BGR三通道
            if img[i, j][k] < 32:
                gray = 0
            elif img[i, j][k] < 64:
                gray = 32
            elif img[i, j][k] < 96:
                gray = 64
            elif img[i, j][k] < 128:
                gray = 96
            elif img[i, j][k] < 160:
                gray = 128
            elif img[i, j][k] < 192:
                gray = 160
            elif img[i, j][k] < 224:
                gray = 192
            else:
                gray = 224
            new_img3[i, j][k] = np.uint8(gray)

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']

# 显示图像
titles = [u'(a)原始图像', u'(b)量化L2', u'(c)量化L4', u'(d)量化L8', ]
images = [img, new_img1, new_img2, new_img3]
for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
