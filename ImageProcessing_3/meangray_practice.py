#_*_coding:utf-8_*_
import cv2 
import numpy as np 
import matplotlib.pyplot as plt
 
#读取原始图像
img = cv2.imread('irving.jpg')
 
src = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
 
#获取图像高度和宽度
height = img.shape[0]
width = img.shape[1]
 
#创建一幅图像
grayimg = np.zeros((height, width, 3), np.uint8)
 
#图像平均灰度处理方法
for i in range(height):
    for j in range(width):
        #灰度值为RGB三个分量的平均值
        gray = (int(img[i,j][0]) + int(img[i,j][1]) + int(img[i,j][2]))  /  3
        grayimg[i,j] = np.uint8(gray)
 
# #显示图像
# cv2.imshow("src", img)
# cv2.imshow("gray", grayimg)
 
# #等待显示
# cv2.waitKey(0)
# cv2.destroyAllWindows()
 
plt.subplot(1,3,1), plt.imshow(img)
plt.xticks([]), plt.yticks([])
plt.title('origin image BGR')
plt.subplot(1,3,2), plt.imshow(src)
plt.xticks([]), plt.yticks([])
plt.title('origin image RGB')
plt.subplot(1,3,3), plt.imshow(grayimg)
plt.xticks([]), plt.yticks([])
plt.title('mean gray image')
plt.show()
