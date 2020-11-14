#_*_coding:utf-8_*_
import numpy as np
import cv2


def show(image):
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w*r), height)
    else:
        r = width / float(w)
        dim = (width, int(h*r))
    resized = cv2.resize(image, dim, interpolation=inter)
    return resized


def edge_detection(img_path):
    # *********  预处理 ****************
    # 读取输入
    img = cv2.imread(img_path)
    # 坐标也会相同变换
    ratio = img.shape[0] / 500.0
    orig = img.copy()

    image = resize(orig, height=500)
    # 预处理
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 75, 200)
    # show(edged)

    # *************  轮廓检测 ****************
    # 轮廓检测
    contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(contours, key=cv2.contourArea, reverse=True)[:5]
    # print(len(contours))
    max_area = 0
    myscreenCnt = []
    for i in contours:
        temp = cv2.contourArea(i)
        if max_area < temp:
            myscreenCnt = i

    # 计算轮廓近似
    peri = cv2.arcLength(myscreenCnt, True)
    approx = cv2.approxPolyDP(myscreenCnt, 0.02 * peri, True)

    # 4个点的时候就拿出来
    if len(approx) == 4:
        screenCnt = approx
        
    return orig, ratio, screenCnt


def order_points(pts):
    # 一共四个坐标点
    rect = np.zeros((4, 2), dtype='float32')
    
    # 按顺序找到对应的坐标0123 分别是左上，右上，右下，左下
    # 计算左上，由下
    # numpy.argmax(array, axis) 用于返回一个numpy数组中最大值的索引值
    s = pts.sum(axis=1) 
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    # 计算右上和左
    # np.diff()  沿着指定轴计算第N维的离散差值  后者-前者
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    return rect


# 透视变换
def four_point_transform(image, pts):
    # 获取输入坐标点
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    # 计算输入的w和h的值
    widthA = np.sqrt(((br[0] - bl[0])**2) + ((br[1] - bl[1])**2))
    widthB = np.sqrt(((tr[0] - tl[0])**2) + ((tr[1] - tl[1])**2))
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.sqrt(((tr[0] - br[0])**2) + ((tr[1] - br[1])**2))
    heightB = np.sqrt(((tl[0] - bl[0])**2) + ((tl[1] - bl[1])**2))
    maxHeight = max(int(heightA), int(heightB))

    # 变化后对应坐标位置
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]],
        dtype='float32')    

    # 计算变换矩阵
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    # 返回变换后的结果
    return warped


# 对透视变换结果进行处理
def get_image_processingResult():
    img_path = r'test_05.png'
    orig, ratio, screenCnt = edge_detection(img_path)
    # screenCnt 为四个顶点的坐标值，但是我们这里需要将图像还原，即乘以以前的比率
    # 透视变换  这里我们需要将变换后的点还原到原始坐标里面
    warped = four_point_transform(orig, screenCnt.reshape(4, 2)*ratio)
    # 二值处理
    gray = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)[1]

    cv2.imwrite(r'test_05.png', warped)
    return thresh


if __name__ == '__main__':
    # 获取矫正之后的图片
    get_image_processingResult()
