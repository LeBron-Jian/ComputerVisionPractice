#_*_coding:utf-8_*_
import cv2
import numpy as np
 
img_path = 'contour2.png'
img = cv2.imread(img_path)
img1 = img.copy()
img2 = img.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy= cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
# 绘制独立轮廓，如第四个轮廓
img1 = cv2.drawContours(img1, [cnt], -1, (0, 255, 0), 3)

epsilon = 0.1*cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)
img2 = cv2.drawContours(img2, [approx], -1, (0, 255, 0), 3)

res = np.hstack((img, img1, img2))
cv2.imshow('img', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
