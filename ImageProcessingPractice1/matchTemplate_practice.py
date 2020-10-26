#_*_coding:utf-8_*_
import cv2
import numpy as np
import matplotlib.pyplot as plt

  
img_path = 'lena.jpg'
img = cv2.imread(img_path, 0)
template = cv2.imread('face.jpg', 0)

template_h, template_w = template.shape[:2]
print(img.shape)   # (263, 263)
print(template.shape)  # (110, 85)

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

res = cv2.matchTemplate(img, template, cv2.TM_SQDIFF)

# 函数返回值就是矩阵的最小值，最大值，最小值的索引，最大值的索引。
min_val, max_val, min_index, max_index = cv2.minMaxLoc(res)
# print(min_val, max_val, min_index, max_index)
# 39168.0  74403584.0 (107, 89) (159, 62)

for meth in methods:
    img2 = img.copy()

    # 匹配方法的真值
    method = eval(meth)
    # print(meth, method)
    '''
        cv2.TM_CCOEFF 4
        cv2.TM_CCOEFF_NORMED 5
        cv2.TM_CCORR 2
        cv2.TM_CCORR_NORMED 3
        cv2.TM_SQDIFF 0
        cv2.TM_SQDIFF_NORMED 1
    '''
    res = cv2.matchTemplate(img, template, method)
    # 函数返回值就是矩阵的最小值，最大值，最小值的索引，最大值的索引。
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # 如果是平方差匹配 TM_SQDIFF 或归一化平方差匹配 TM_SQDIFF_NORMED，取最小值
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + template_w, top_left[1] + template_h)

    # 画矩形
    cv2.rectangle(img2, top_left, bottom_right, 255, 2)

    plt.subplot(121), plt.imshow(res, cmap='gray')
    plt.xticks([]), plt.yticks([])  # 隐藏坐标轴
    plt.subplot(122), plt.imshow(img2, cmap='gray')
    plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()


# cv2.imshow('img', res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
