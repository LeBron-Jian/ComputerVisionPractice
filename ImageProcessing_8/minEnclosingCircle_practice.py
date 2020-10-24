#_*_coding:utf-8_*_
import cv2
import numpy as np
  
img_path = 'contour2.png'
img = cv2.imread(img_path)
img1 = img.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy= cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
 
 
cnt = contours[0]
# 求轮廓的外接圆
(x, y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
img1 = cv2.circle(img1, center, radius, (0, 255, 0), 2)
res = np.hstack((img, img1))
cv2.imshow('img', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
