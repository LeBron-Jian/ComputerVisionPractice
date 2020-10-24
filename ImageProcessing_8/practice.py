import cv2
import numpy as np
import matplotlib.pyplot as plt


def show_image(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def image_processing(filename):
    img = cv2.imread(filename)
    img = cv2.resize(img, dsize=(100, 100))
    data = img.reshape((-1, 3))
    data = np.float32(data)
    # 定义中心（tyep, max_iter, epsilon)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    # 设置标签
    flags = cv2.KMEANS_RANDOM_CENTERS
    # K-means 聚类，聚集成2类
    compactness, labels2, centers2 = cv2.kmeans(data, 2, None, criteria, 10, flags)

    # 2 类 图像转换回 uint8 二维类型
    centers2 = np.uint8(centers2)
    res2 = centers2[labels2.flatten()]
    dst2 = res2.reshape(img.shape)

    gray = cv2.cvtColor(dst2, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # 第一个参数是指明在哪副图像上绘制轮廓，第二个参数是轮廓本身，在Python中是list
    # 第三个参数指定绘制轮廓list中那条轮廓，如果是-1，则绘制其中的所有轮廓。。
    # dst3 = cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

    # show_image(dst3)
    for ind, contour in enumerate(contours):
        print('总共有几个轮廓：%s' % len(contours))

        # 其中x,y,w,h分布表示外接矩阵的x轴和y轴的坐标，以及矩阵的宽和高，contour表示输入的轮廓值
        x, y, w, h = cv2.boundingRect(contour)
        print(x, y, w, h)
        if w > 80 or h > 80:
            print(contours[ind])
            print(type(contours[ind]), contours[ind].shape)
            # cv2.fillConvexPoly()函数可以用来填充凸多边形,只需要提供凸多边形的顶点即可。
            cv2.fillConvexPoly(img, contours[ind], (255, 255, 255))
    show_image(img)

    # # 用来正常显示中文标签
    # plt.rcParams['font.sans-serif'] = ['SimHei']
    #
    # # 显示图形
    # titles = [u'原图', u'聚类图像 K=2']
    # images = [img,  dst2]
    # for i in range(len(images)):
    #     plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    #     plt.title(titles[i])
    #     plt.xticks([]), plt.yticks([])
    # plt.show()


if __name__ == '__main__':
    filename1 = 'test.png'
    image_processing(filename)
