#_*_coding:utf-8_*_
import cv2
import matplotlib.pyplot as plt


def box_blur_filter_func(filename):
    img = cv2.imread(filename)
    rgbimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    blur = cv2.blur(img, (3, 3))
    # 方框滤波: 基本和均值滤波一样，可以选择归一化，如果选择归一化，则和均值滤波一样
    # 如果不选择归一化，则方框滤波容易越界，越界的话，超过255则用255表示
    result_normal = cv2.boxFilter(img, -1, (3, 3), normalize=True)
    result_nonormal = cv2.boxFilter(img, -1, (3, 3), normalize=False)
    # 显示图像
    titles = ['origin image', 'boxFilter image no normalize', 'boxFilter image normalize', 'blut filter image']
    images = [rgbimg, result_nonormal, result_normal, blur]
    for i in range(4):
        plt.subplot(2, 2, i+1), plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == '__main__':
    filename = 'lenaNoise.png'
    box_blur_filter_func(filename)
