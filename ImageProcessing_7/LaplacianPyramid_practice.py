import cv2
import numpy as np
 
img = cv2.imread('kd2.jpg')
down = cv2.pyrDown(img)
down_up = cv2.pyrUp(down)
 
l_1 = img - down_up
cv2.imshow('laplacian', l_1)
cv2.waitKey(0)
cv2.destroyAllWindows()
