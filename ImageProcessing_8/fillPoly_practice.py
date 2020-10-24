#_*_coding:utf-8_*_
import cv2
import numpy as np

img = np.zeros((500, 500, 3), np.uint8)
area1 = np.array([[50, 50], [50, 400], [100, 450]])
area2 = np.array([[300, 300],[450, 300], [450, 450], [300, 450]])
cv2.fillPoly(img, [area1, area2], (255, 0, 0))
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
