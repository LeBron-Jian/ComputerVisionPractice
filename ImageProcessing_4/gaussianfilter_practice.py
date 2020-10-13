#_*_coding:utf-8_*_
import cv2
import matplotlib.pyplot as plt


def gaussian_blur_func(filename):
    img = cv2.imread(filename)
    rgbimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 高斯滤波：高斯模糊的卷积核的数值是满足高斯分布的，相当于更重视中间的
    # 标准差取0时，OpenCV会根据高斯矩阵的尺度自己计算
    result1 = cv2.GaussianBlur(img, (5, 5), 0)
    result2 = cv2.GaussianBlur(img, (5, 5), 1)
    # 显示图像
    titles = ['origin image', 'gaussian blur image stu 0', 'gaussian blur image stu 1']
    images = [rgbimg, result1, result2]
    for i in range(3):
        plt.subplot(1, 3, i+1), plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == '__main__':
    filename = 'lenaNoise.png'
    gaussian_blur_func(filename)
