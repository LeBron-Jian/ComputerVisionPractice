import cv2
import numpy as np
 
img = cv2.imread('test_1.jpg')
print('imgshape', img.shape)
# imgshape (800, 1200, 3)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
print('dst.shape', dst.shape)
# dst.shape (800, 1200)
 
img[dst>0.01*dst.max()] = [0, 0, 255]
cv2.imshow('dst', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
