#_*_coding:utf-8_*_
import cv2
import matplotlib.pyplot as plt


def median_blur_filter_func(filename):
    img = cv2.imread(filename)
    rgbimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 中值滤波: 相当于用中值代替
    median = cv2.medianBlur(img, 5)
    # 显示图像
    titles = ['origin image', 'blut filter image']
    images = [rgbimg, median]
    for i in range(2):
        plt.subplot(1, 2, i+1), plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == '__main__':
    filename = 'lenaNoise.png'
    median_blur_filter_func(filename)
