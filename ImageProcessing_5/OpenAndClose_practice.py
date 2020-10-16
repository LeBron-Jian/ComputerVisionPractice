import cv2
import numpy as np
 
 
def Open_operation(img_path):
    origin_img = cv2.imread(img_path)
    gray_img = cv2.cvtColor(origin_img, cv2.COLOR_BGR2GRAY)
    # OpenCV定义的结构元素
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    # 开运算
    open = cv2.morphologyEx(gray_img, cv2.MORPH_OPEN, kernel)
    # 显示腐蚀后的图像
    cv2.imshow('Open', open)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
 
def Closed_operation(img_path):
    origin_img = cv2.imread(img_path)
    gray_img = cv2.cvtColor(origin_img, cv2.COLOR_BGR2GRAY)
    # OpenCV定义的结构元素
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    # 闭运算
    closed = cv2.morphologyEx(gray_img, cv2.MORPH_CLOSE, kernel)
    # 显示腐蚀后的图像
    cv2.imshow('Closed', closed)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
 
def show_origin(origin_path):
    # img = cv2.imread(origin_path, )
    # 灰度化
    img = cv2.imread(origin_path, 0)
    cv2.imshow('origin', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
if __name__ == '__main__':
    # 此图为加了高斯噪声的图片
    img_path = 'butterfly_Gaussian.jpg'
    show_origin(img_path)
    Closed_operation(img_path)
    Open_operation(img_path)
