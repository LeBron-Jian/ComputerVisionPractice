#_*_coding:utf-8_*_
import cv2
import numpy as np
 
img_path = 'contour2.png'
img = cv2.imread(img_path)
img1 = img.copy()
img2 = img.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy= cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print('轮廓的总数为', len(contours))
# 轮廓的总数为 2

cnt = contours[0]
x, y, w, h = cv2.boundingRect(cnt)
img1 = cv2.rectangle(img1, (x,y), (x+w,y+h), (0, 255, 0), 2)

cv2.imshow('img', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
