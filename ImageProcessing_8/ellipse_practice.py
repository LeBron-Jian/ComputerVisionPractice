import cv2
import numpy as np
import matplotlib.pyplot as plt

# 生成一个空灰度图像
img_origin1 = np.zeros((400, 400), np.uint8)
img_origin11 = img_origin1.copy()
# 参数依次是：图像，椭圆圆心坐标，轴的长度，偏转的角度, 圆弧起始角的角度，圆弧终结角的角度，线条的颜色，线条的粗细程度，线条的类型
img1 = cv2.ellipse(img_origin1, (150, 150), (150, 100), 30, 10, 190, 250)
img11 = cv2.ellipse(img_origin11, (150, 150), (150, 100), 30, 10, 190, 250, -1)

# 生成一个空彩色图像
img_origin3 = np.zeros((400, 400, 3), np.uint8)
img_origin33 = img_origin3.copy()
# 注意最后一个参数 -1，表示对图像进行填充，默认是不填充的，如果去掉，只有椭圆轮廓了
img3 = cv2.ellipse(img_origin3, (150, 150), (150, 100), 30, 0, 180, 250)
img33 = cv2.ellipse(img_origin33, (150, 150), (150, 100), 30, 0, 180, 250, -1)

titles = ['gray ellipse image', 'color ellipse image', 'gray ellipse padding', 'color ellipse padding']
res = [img1, img3, img11, img33]

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(res[i]), plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

