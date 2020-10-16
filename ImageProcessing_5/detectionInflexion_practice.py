# coding=utf-8
import cv2
import numpy


def detection_inflexion(img_path):
    image = cv2.imread(img_path, 0)
    origin = cv2.imread(img_path)
    # 构造5×5的结构元素，分别为十字形、菱形、方形和X型
    cross = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
    # 菱形结构元素的定义稍麻烦一些
    diamond = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    diamond[0, 0] = 0
    diamond[0, 1] = 0
    diamond[1, 0] = 0
    diamond[4, 4] = 0
    diamond[4, 3] = 0
    diamond[3, 4] = 0
    diamond[4, 0] = 0
    diamond[4, 1] = 0
    diamond[3, 0] = 0
    diamond[0, 3] = 0
    diamond[0, 4] = 0
    diamond[1, 4] = 0
    square = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    x = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
    # 使用cross膨胀图像
    dilate_cross_img = cv2.dilate(image, cross)
    # 使用菱形腐蚀图像
    erode_diamond_img = cv2.erode(dilate_cross_img, diamond)

    # 使用X膨胀原图像
    dilate_x_img = cv2.dilate(image, x)
    # 使用方形腐蚀图像
    erode_square_img = cv2.erode(dilate_x_img, square)

    # result = result1.copy()
    # 将两幅闭运算的图像相减获得角
    result = cv2.absdiff(erode_square_img, erode_diamond_img)
    # 使用阈值获得二值图
    retval, result = cv2.threshold(result, 40, 255, cv2.THRESH_BINARY)

    # 在原图上用半径为5的圆圈将点标出。
    for j in range(result.size):
        y = int(j / result.shape[0])
        x = int(j % result.shape[0])

        if result[x, y] == 255:
            cv2.circle(image, (y, x), 5, (255, 0, 0))

    cv2.imshow("Result", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    img_path = "building.jpg"
    detection_inflexion(img_path)
