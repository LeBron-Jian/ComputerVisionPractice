#_*_coding:utf-8_*_
import cv2 as cv
import numpy as np
import math
import matplotlib.pyplot as plt

 
# 灰度化处理
def rgb2gray(img):
    h=img.shape[0]
    w=img.shape[1]
    img1=np.zeros((h,w),np.uint8)
    for i in range(h):
        for j in range(w):
            img1[i,j]=0.144*img[i,j,0]+0.587*img[i,j,1]+0.299*img[i,j,1]
    return img1
 
# 计算高斯卷积核
def gausskernel(size):
    sigma=1.0
    gausskernel=np.zeros((size,size),np.float32)
    for i in range (size):
        for j in range (size):
            norm=math.pow(i-1,2)+pow(j-1,2)
            gausskernel[i,j]=math.exp(-norm/(2*math.pow(sigma,2)))   # 求高斯卷积
    sum=np.sum(gausskernel)   # 求和
    kernel=gausskernel/sum   # 归一化
    return kernel
 
# 高斯滤波
def gauss(img):
    h=img.shape[0]
    w=img.shape[1]
    img1=np.zeros((h,w),np.uint8)
    kernel=gausskernel(3)   # 计算高斯卷积核
    for i in range (1,h-1):
        for j in range (1,w-1):
            sum=0
            for k in range(-1,2):
                for l in range(-1,2):
                    sum+=img[i+k,j+l]*kernel[k+1,l+1]   # 高斯滤波
            img1[i,j]=sum
    return img1
 
image = cv.imread("lenaNoise.png")
grayimage=rgb2gray(image)
gaussimage = gauss(grayimage)
cv.imshow("image",image)
cv.imshow("grayimage",grayimage)
cv.imshow("gaussimage",gaussimage)
cv.waitKey(0)
cv.destroyAllWindows()
