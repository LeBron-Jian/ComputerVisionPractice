# _*_ coding:utf-8 _*_
import cv2
import numpy as np
from matplotlib import pyplot as plt
 
# 读取图像
img = cv2.imread('irving.jpg', )
# 图像进行灰度化处理
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
# 傅里叶变换
# cv2.DFT_COMPLEX_OUTPUT 执行一维或二维复数阵列的逆变换，结果通常是相同大小的复数数组
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
# 将频谱低频从左上角移动到中心位置
dft_shift = np.fft.fftshift(dft)
# 频谱图像双通道复数转换为0~255区间
result = 10 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
 
# 傅里叶逆变换
ishift = np.fft.ifftshift(dft_shift)
iimg = cv2.idft(ishift)
iresult = cv2.magnitude(iimg[:, :, 0], iimg[:, :, 1])
 
 
# 显示图像
plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Input image')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(result, cmap='gray')
plt.title('Magnitude Spectrum')
plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(iresult, cmap='gray')
plt.title('inverse Magnitude Spectrum')
plt.xticks([]), plt.yticks([])
plt.show()
