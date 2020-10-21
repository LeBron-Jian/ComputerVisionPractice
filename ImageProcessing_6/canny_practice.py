# Canny边缘提取
import cv2 as cv
import numpy as np
 
 
def edge_demo(image):
    blurred = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_RGB2GRAY)
    # xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0) #x方向梯度
    # ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1) #y方向梯度
    # edge_output = cv.Canny(xgrad, ygrad, 50, 150)
    edge_output = cv.Canny(gray, 50, 150)
    cv.imshow("Canny Edge", edge_output)
    dst = cv.bitwise_and(image, image, mask=edge_output)
    cv.imshow("Color Edge", dst)
 
 
# src = cv.imread('logo1.jpg')
# # 设置为WINDOW_NORMAL可以任意缩放
# # cv.namedWindow('input_image', cv.WINDOW_NORMAL)
# cv.imshow('input_image', src)
# edge_demo(src)
# cv.waitKey(0)
# cv.destroyAllWindows()

img = cv.imread('lena.jpg', cv.IMREAD_GRAYSCALE)

v1 = cv.Canny(img, 80, 150)
v2 = cv.Canny(img, 50, 100)

res = np.hstack((v1, img, v2))
cv.imshow('img', res)
cv.waitKey(0)
cv.destroyAllWindows()
