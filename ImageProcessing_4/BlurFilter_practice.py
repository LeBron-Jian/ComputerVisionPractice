#_*_coding:utf-8_*_
import cv2
import matplotlib.pyplot as plt


def blur_filter_func(filename):
    img = cv2.imread(filename)
    rgbimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 均值滤波: 简单的平均卷积操作
    result = cv2.blur(rgbimg, (5, 5))
    # 显示图像
    titles = ['origin image', 'blur image']
    images = [rgbimg, result]
    for i in range(2):
        plt.subplot(1, 2, i+1), plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == '__main__':
    filename = 'lenaNoise.png'
    blur_filter_func(filename)
