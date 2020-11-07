# _*_ coding:utf-8 _*_
import cv2
import numpy as np
from matplotlib import pyplot as plt
 
# 读取图像
img = cv2.imread('irving.jpg', )
# 图像进行灰度化处理
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
# 傅里叶变换
# 快速傅里叶变换算法得到频率分布
f = np.fft.fft2(img)
# 默认结果中心点位置是在左上角 调用fftshift()函数转移到中间位置
fshift = np.fft.fftshift(f)
# fft 结果是复数，其绝对值结果是振幅
rimg = np.log(np.abs(fshift))
 
# 傅里叶逆变换
ishift = np.fft.ifftshift(fshift)
iimg = np.fft.ifft2(ishift)
iimg = np.abs(iimg)
 
 
# 展示结果
plt.subplot(131), plt.imshow(img, 'gray'), plt.title('original Fourier')
plt.axis('off')
plt.subplot(132), plt.imshow(rimg, 'gray'), plt.title('fourier Fourier')
plt.axis('off')
plt.subplot(133), plt.imshow(iimg, 'gray'), plt.title('inverse fourier Fourier')
plt.axis('off')
plt.show()
