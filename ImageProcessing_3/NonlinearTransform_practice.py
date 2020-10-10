import cv2
import numpy as np
import matplotlib.pyplot as plt
 
# 读取原始图像
img = cv2.imread('irving.jpg')
 
# 图像灰度转换
grayimage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
# 获取图像高度和宽度
height = grayimage.shape[0]
width = grayimage.shape[1]
 
# 创建一幅图像
result = np.zeros((height, width), np.uint8)
 
# 图像灰度非线性变换  DB = DA * DA / 255
for i in range(height):
    for j in range(width):
        gray = int(grayimage[i, j]) * int(grayimage[i, j]) / 255
        result[i, j] = np.uint8(gray)
 
# 显示图像
cv2.imshow("Gray Image", grayimage)
cv2.imshow("Result", result)
 
# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
