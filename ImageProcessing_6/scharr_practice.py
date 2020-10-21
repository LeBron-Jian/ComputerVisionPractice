# coding=utf-8
import cv2
import numpy as np
 
img = cv2.imread("durant.jpg", 0)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
 
sobel_x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
sobel_y = cv2.Sobel(img, cv2.CV_16S, 0, 1)
scharr_x = cv2.Scharr(img, cv2.CV_16S, 1, 0)
scharr_y = cv2.Scharr(img, cv2.CV_16S, 0, 1)
 
sobel_absX = cv2.convertScaleAbs(sobel_x)  # 转回uint8
sobel_absY = cv2.convertScaleAbs(sobel_y)
scharr_absX = cv2.convertScaleAbs(scharr_x)  # 转回uint8
scharr_absY = cv2.convertScaleAbs(scharr_y)
 
Sobel_dst = cv2.addWeighted(sobel_absX, 0.5, sobel_absY, 0.5, 0)
Scharr_dst = cv2.addWeighted(scharr_absX, 0.5, scharr_absY, 0.5, 0)
 
# cv2.imshow("absX", scharr_absX)
# cv2.imshow("absY", scharr_absY)
# cv2.imshow("Result", dst)
 
sobel_image = np.hstack((sobel_absX, sobel_absY, Sobel_dst))
scharr_image = np.hstack((scharr_absX, scharr_absY, Scharr_dst))
all_image = np.vstack((sobel_image, scharr_image))
cv2.imshow("Result", all_image)
 
 
cv2.waitKey(0)
cv2.destroyAllWindows()
