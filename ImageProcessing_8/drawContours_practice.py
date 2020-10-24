#_*_coding:utf-8_*_
import cv2
import numpy as np
 
img_path = 'contour.jpg'
img = cv2.imread(img_path)
img1 = img.copy()
img2 = img.copy()
img3 = img.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy= cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 绘制独立轮廓，如第四个轮廓
img1 = cv2.drawContours(img1, contours, -1, (0, 255, 0), 3)
# 如果指定绘制几个轮廓（确保数量在轮廓总数里面），就会只绘制指定数量的轮廓
img2 = cv2.drawContours(img2, contours, 1, (0, 255, 0), 3)
img3 = cv2.drawContours(img3, contours, 0, (0, 255, 0), 3)

res = np.hstack((img, img1, img2))
cv2.imshow('img', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
