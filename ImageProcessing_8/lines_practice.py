import cv2
import numpy as np
import matplotlib.pyplot as plt

# 生成一个空灰度图像
img1 = np.zeros((400, 400), np.uint8)
img1 = cv2.line(img1, (0, 0), (400, 400), 255, 5)

# 生成一个空彩色图像
img3 = np.zeros((400, 400, 3), np.uint8)
img3 = cv2.line(img3, (0, 0), (400, 400), (0, 255, 0), 5)

titles = ['gray line image', 'color line image']
res = [img1, img3]

for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(res[i]), plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
