import cv2
import numpy as np
import matplotlib.pyplot as plt
 
 
img = cv2.imread('circle.jpg', cv2.IMREAD_GRAYSCALE)

# 白到黑是正数，黑到白就是负数，所有的负数都会被截断成0，所以要取绝对值
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobelxAbs = cv2.convertScaleAbs(sobelx)

sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobelyAbs = cv2.convertScaleAbs(sobely)

# 分别计算x和y，再求和
slbelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)


# 不建议直接计算，这里尝试直接计算，看看效果
sobelxy1 = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=3)
sobelxy1 = cv2.convertScaleAbs(sobelxy1)



 
result = [img, sobelxAbs, sobelyAbs, slbelxy, sobelxy1]
titles = ['origin img', 'sobel x img', 'sobel y img', 'sobel x-y img', 'sobel xy img']
for i in range(5):
    plt.subplot(2, 3, i+1), plt.imshow(result[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
