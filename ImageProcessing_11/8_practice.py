# _*_ coding:utf-8_*_
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
img = cv2.imread('paper.jpg')
print(img.shape)  # paper1  (511, 297, 3)  paper  (772, 520, 3)

# 获取图像大小
rows, cols = img.shape[:2]

# 将原图像高斯模糊
img = cv2.GaussianBlur(img, (3, 3), 0)
# 然后进行灰度化处理
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 边缘检测（检测出图像的边缘信息)
# threshold1 表示第一个滞后性阈值 threshold2表示第二个滞后性阈值
# apertureSize 表示应用Sobel算子的孔径大小，其默认值为3
edge = cv2.Canny(gray, 50, 200, apertureSize=3)
# cv2.imshow('canny', edge)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# 通过霍夫变换得到A4纸边缘
# 可以看到A4纸外还有一些线，可以通过霍夫变换去掉这些先
lines = cv2.HoughLinesP(edge, 1, np.pi/180, 30, minLineLength=60, maxLineGap=10)
# 下面输出的四个点分别为四个顶点
for x1, y1, x2, y2 in lines[0]:
    print((x1, y1), (x2, y2))
for x1, y1, x2, y2 in lines[1]:
    print((x1, y1), (x2, y2))
# (9, 564) (140, 254)
# (355, 636) (421, 464)x

# 绘制边缘
for x1, y1, x2, y2 in lines[0]:
    cv2.line(gray, (x1, y1), (x2, y2), (0, 0, 255), 2)

# lines = cv2.HoughLines(edge, 1, np.pi/180, 150)
# # 提取为二维
# lines1 = lines[:, 0, :]
# for rho, theta in lines1[:]:
#     a, b = np.cos(theta), np.sin(theta)
#     x0, y0 = a*rho, b*rho
#     x1, y1 = int(x0 + 1000*(-b)), int(y0 + 1000*(a))
#     x2, y2 = int(x0 - 1000*(-b)), int(y0 - 1000*(a))
#     print(x1, x2, y1, y2)
#     cv2.line(gray, (x1, y1), (x2, y2), (0, 0, 255), 2)


# cv2.imshow('hough', gray)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 根据四个顶点设置图像透视变换矩阵
pos1 = np.float32([[168, 187], [509, 246], [9, 563], [399, 519]])
pos2 = np.float32([[0, 0], [170, 0], [0, 220], [170, 220]])
M = cv2.getPerspectiveTransform(pos1, pos2)

# 图像透视变换
result = cv2.warpPerspective(img, M, (170, 250))
cv2.imshow('result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
