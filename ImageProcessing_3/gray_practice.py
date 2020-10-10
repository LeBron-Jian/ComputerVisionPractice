#_*_coding:utf-8_*_
import cv2 
import numpy as np 
import matplotlib.pyplot as plt
 
#读取原始图片
src1 = cv2.imread('irving.jpg')
src2 = cv2.cvtColor(src1, cv2.COLOR_BGR2RGB)
 
#图像灰度化处理
grayImage = cv2.cvtColor(src1, cv2.COLOR_RGB2GRAY)
grayImage1 = cv2.imread('irving.jpg', 0)
# #显示图像
# cv2.imshow("src", src)
# cv2.imshow("result", grayImage)
 
# #等待显示
# cv2.waitKey(0)
# cv2.destroyAllWindows()

plt.subplot(2,2,1), plt.imshow(src1)
plt.xticks([]), plt.yticks([])
plt.title('origin image BGR')
plt.subplot(2,2,2), plt.imshow(src2)
plt.xticks([]), plt.yticks([])
plt.title('origin image RGB')
plt.subplot(2,2,3), plt.imshow(grayImage)
plt.xticks([]), plt.yticks([])
plt.title('BGR2gray image')
plt.subplot(2,2,4), plt.imshow(grayImage1)
plt.xticks([]), plt.yticks([])
plt.title('gray image')
plt.show()
