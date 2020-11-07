# _*_ coding:utf-8 _*_
import cv2
import numpy as np
import matplotlib.pyplot as plt
 
# 读取图像
img = cv2.imread('lena.jpg', 0)
 
# 傅里叶变换
fimg = np.fft.fft2(img)
fshift = np.fft.fftshift(fimg)
 
# 设置高通滤波器
rows, cols = img.shape
crow, ccol = int(rows/2), int(cols/2)
fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
 
# 傅里叶逆变换
ishift = np.fft.ifftshift(fshift)
iimg = np.fft.ifft2(ishift)
iimg = np.abs(iimg)
 
# 显示原始图像和高通滤波处理图像
plt.subplot(121), plt.imshow(img, 'gray'), plt.title('gray Image')
plt.axis('off')
plt.subplot(122), plt.imshow(iimg, 'gray'), plt.title('Result Image')
plt.axis('off')
plt.show()
