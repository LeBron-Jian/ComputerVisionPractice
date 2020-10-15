#_*_coding:utf-8_*_
import cv2
import numpy as np


def show_element():
    element_cross = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
    print(element_cross)
    element_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    print(element_ellipse)
    element_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    print(element_rect)
    '''
    [[0 0 1 0 0]
     [0 0 1 0 0]
     [1 1 1 1 1]
     [0 0 1 0 0]
     [0 0 1 0 0]]
     
    [[0 0 1 0 0]
     [1 1 1 1 1]
     [1 1 1 1 1]
     [1 1 1 1 1]
     [0 0 1 0 0]]
     
    [[1 1 1 1 1]
     [1 1 1 1 1]
     [1 1 1 1 1]
     [1 1 1 1 1]
     [1 1 1 1 1]]'''


def define_cross_structure():
    NpKernel = np.uint8(np.zeros((5, 5)))
    for i in range(5):
        NpKernel[2, i] = 1
        NpKernel[i, 2] = 1
    print("NpKernel", NpKernel)
    '''
    NpKernel [[0 0 1 0 0]
     [0 0 1 0 0]
     [1 1 1 1 1]
     [0 0 1 0 0]
     [0 0 1 0 0]]
     '''
