#_*_coding:utf-8_*_
import cv2  # opencv读取的格式是BGR
import numpy as np
import matplotlib.pyplot as plt  # Matplotlib读取的格式是RGB

img = cv2.imread('cat.jpg', 0)

# 创建 mask
mask = np.zeros(img.shape[:2], np.uint8)
print(mask.shape)  # (414, 500)
mask[100:300, 100:400] = 255

masked_img = cv2.bitwise_and(img, img, mask=mask)  # 与操作

hist_full = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_mask = cv2.calcHist([img], [0], mask, [256], [0, 256])

plt.subplot(221), plt.imshow(img, 'gray'), plt.title('gray image')
plt.subplot(222), plt.imshow(mask, 'gray'), plt.title('mask image')
plt.subplot(223), plt.imshow(masked_img, 'gray'), plt.title('image bitwise and mask')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask), plt.title('hist image')
plt.xlim([0, 256])
plt.show()
