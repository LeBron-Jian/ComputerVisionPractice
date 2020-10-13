#_*_coding:utf-8_*_
import cv2
import matplotlib.pyplot as plt
import numpy as np


########     五个不同的滤波器    #########
img = cv2.imread('lenaNoise.png')
 
# 均值滤波
img_mean = cv2.blur(img, (3,3))

# 方框滤波
img_box = cv2.boxFilter(img, -1, (3, 3), normalize=False)
 
# 高斯滤波
img_Guassian = cv2.GaussianBlur(img,(3,3),0)
 
# 中值滤波
img_median = cv2.medianBlur(img, 3)
 
# 双边滤波
img_bilater = cv2.bilateralFilter(img,9,75,75)
 
# 展示不同的图片
titles = ['srcImg', 'mean', 'box', 'Gaussian', 'median', 'bilateral']
imgs = [img, img_mean, img_box, img_Guassian, img_median, img_bilater]
 
for i in range(6):
    plt.subplot(2,3,i+1)#注意，这和matlab中类似，没有0，数组下标从1开始
    plt.imshow(imgs[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()

# # 或者这样展示，可以看到其真实效果（解决了显示图像因为通道转换问题颜色偏蓝的问题）
# res1 = np.hstack((img, img_mean, img_box))
# res2 = np.hstack((img_Guassian, img_median, img_bilater))
# res = np.vstack((res1, res2))
# cv2.imshow('median vs average', res)
# cv2.waitKey(0)
# cv2.destoryAllWindows()
