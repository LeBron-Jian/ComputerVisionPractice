# _*_ coding:utf-8 _*_
import cv2
import numpy as np
import matplotlib.pyplot as plt
 
# 读取图像
img = cv2.imread('lena.jpg', 0)
 
# 傅里叶变换
# fimg = np.fft.fft2(img)
fimg = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
fshift = np.fft.fftshift(fimg)
 
# 设置低通滤波器
rows, cols = img.shape
# 中心位置
crow, ccol = int(rows / 2), int(cols / 2)
mask = np.zeros((rows, cols, 2), np.uint8)
mask[crow - 30:crow + 30, ccol - 30:ccol + 30] = 1
 
# 掩膜图像和频谱图像乘积
f = fshift * mask
print(f.shape, fshift.shape, mask.shape)
# (199, 198, 2) (199, 198, 2) (199, 198, 2)
 
 
# 傅里叶逆变换
ishift = np.fft.ifftshift(f)
iimg = cv2.idft(ishift)
iimg = cv2.magnitude(iimg[:, :, 0], iimg[:, :, 1])
 
# 显示原始图像和高通滤波处理图像
plt.subplot(121), plt.imshow(img, 'gray'), plt.title('gray Image')
plt.axis('off')
plt.subplot(122), plt.imshow(iimg, 'gray'), plt.title('Result Image')
plt.axis('off')
plt.show()
