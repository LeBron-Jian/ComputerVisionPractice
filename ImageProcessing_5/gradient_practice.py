import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('circle.jpg')
kernel = np.ones((7, 7), np.uint8)
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))

erosion = cv2.erode(img, kernel, iterations = 5)
dilation = cv2.dilate(img, kernel, iterations = 3)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

result = [img, erosion, dilation, gradient]
titles = ['origin img', 'erosion img', 'dilate img', 'gradient img']
for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(result[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
