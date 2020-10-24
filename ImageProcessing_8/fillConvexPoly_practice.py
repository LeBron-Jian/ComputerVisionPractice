#_*_coding:utf-8_*_
import cv2
import numpy as np

img = np.zeros((500, 500, 3), np.uint8)
triangle = np.array([[50, 50], [50, 400], [400, 450]])
cv2.fillConvexPoly(img, triangle, (0, 255, 0))
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
