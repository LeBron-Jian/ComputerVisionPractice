import cv2
import numpy as np
 
 
def erode_image(img_path):
    origin_img = cv2.imread(img_path)
    gray_img = cv2.cvtColor(origin_img, cv2.COLOR_BGR2GRAY)
    # OpenCV定义的结构元素
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    # 腐蚀图像
    eroded = cv2.erode(gray_img, kernel)
    # 显示腐蚀后的图像
    cv2.imshow('Origin', origin_img)
    cv2.imshow('Erode', eroded)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
 
def dilate_image(img_path):
    origin_img = cv2.imread(img_path)
    gray_img = cv2.cvtColor(origin_img, cv2.COLOR_BGR2GRAY)
    # OpenCV定义的结构元素
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    # 膨胀图像
    dilated = cv2.dilate(gray_img, kernel)
    # 显示腐蚀后的图像
    cv2.imshow('Dilate', dilated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
 
if __name__ == '__main__':
    img_path = 'origin.jpg'
    erode_image(img_path)
    dilate_image(img_path)
