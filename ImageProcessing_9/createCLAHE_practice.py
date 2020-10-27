#_*_coding:utf-8_*_
import cv2  # opencv读取的格式是BGR
import numpy as np
import matplotlib.pyplot as plt  # Matplotlib读取的格式是RGB

img = cv2.imread('cat.jpg', 0)

equ = cv2.equalizeHist(img)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

res_clahe = clahe.apply(img)


res = np.hstack((img, equ, res_clahe)) 
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
