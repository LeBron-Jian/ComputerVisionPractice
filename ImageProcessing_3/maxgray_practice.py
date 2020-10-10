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

#图像最大值灰度处理
for i in range(height):
    for j in range(width):
        #获取图像R G B最大值
        gray = max(img[i,j][0], img[i,j][1], img[i,j][2])
        #灰度图像素赋值 gray=max(R,G,B)
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
plt.title('max gray image')
plt.show()
