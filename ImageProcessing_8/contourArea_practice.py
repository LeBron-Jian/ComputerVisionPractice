#_*_coding:utf-8_*_
import cv2
import numpy as np
 
img_path = 'contour2.png'
img = cv2.imread(img_path)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy= cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


cnt = contours[0]
# 求轮廓的面积
area = cv2.contourArea(cnt)
print(img.shape)  # (306, 453, 3)
print(area)  # 57436.5
