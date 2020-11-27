# _*_coding:utf-8_*_
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
img = cv2.imread('kd2.jpg')

# 获取图像的高度和宽度
height, width = img.shape[0], img.shape[1]
# print(img.shape)  # (352, 642, 3)
# 采样转换成 16*16 区域
numHeight, numWidth = height / 16, width / 16

# 创建一幅图像，内容使用零填充
new_img1 = np.zeros((height, width, 3), np.uint8)

# 图像循环采样 16*16 区域
for i in range(16):
    # 获取Y坐标
    y = int(i * numHeight)
    for j in range(16):
        # 获取 X 坐标
        x = int(j * numWidth)
        # 获取填充颜色，左上角像素点
        b = img[y, x][0]
        g = img[y, x][1]
        r = img[y, x][2]

        # 循环设置小区域采样
        for n in range(int(numHeight)):
            for m in range(int(numWidth)):
                new_img1[y+n, x+m][0] = np.uint8(b)
                new_img1[y+n, x+m][1] = np.uint8(g)
                new_img1[y+n, x+m][2] = np.uint8(r)

# 显示图像
cv2.imshow('src', img)
cv2.imshow('new src', new_img1)
# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
