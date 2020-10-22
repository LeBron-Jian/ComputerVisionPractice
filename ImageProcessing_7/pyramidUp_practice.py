# _*_coding:utf-8 _*_
import cv2
import numpy as np
import matplotlib.pyplot as plt
 
# 读取原始图片
img = cv2.imread('kd2.jpg')
 
# 图像向下取样
r1 = cv2.pyrUp(img)
 
# 显示图形
cv2.imshow('origin image', img)
cv2.imshow('processing image1', r1)
cv2.waitKey(0)
cv2.destroyAllWindows()
