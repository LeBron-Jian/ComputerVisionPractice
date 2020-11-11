import cv2
import numpy as np
from PIL import Image
import pytesseract


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
    show(edged)

    # *************  轮廓检测 ****************
    # 轮廓检测
    contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(contours, key=cv2.contourArea, reverse=True)[:5]
    print(len(contours))
    max_area = 0
    myscreenCnt = []
    for i in contours:
        temp = cv2.contourArea(i)
        if max_area < temp:
            myscreenCnt = i

    # 计算轮廓近似
    peri = cv2.arcLength(myscreenCnt, True)
    # C表示输入的点集
    # epsilon表示从原始轮廓到近似轮廓的最大距离，它是一个准确度参数
    # True表示封闭的
    approx = cv2.approxPolyDP(myscreenCnt, 0.02 * peri, True)

    # 4个点的时候就拿出来
    if len(approx) == 4:
        screenCnt = approx
        
    print(approx)

    # res = cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
    # res = cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
    res = cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)
    show(res)


    return orig, ratio, screenCnt


def order_points(pts):
    # 一共四个坐标点
    rect = np.zeros((4, 2), dtype='float32')
    
    # 按顺序找到对应的坐标0123 分别是左上，右上，右下，左下
    # 计算左上，由下
    # numpy.argmax(array, axis) 用于返回一个numpy数组中最大值的索引值
    s = pts.sum(axis=1)  # [2815.2   1224.    2555.712 3902.112]
    # print(s)
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
    img_path = 'images/answersheet.jpg'
    orig, ratio, screenCnt = edge_detection(img_path)
    # screenCnt 为四个顶点的坐标值，但是我们这里需要将图像还原，即乘以以前的比率
    # 透视变换  这里我们需要将变换后的点还原到原始坐标里面
    warped = four_point_transform(orig, screenCnt.reshape(4, 2)*ratio)
    # 二值处理
    gray = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)[1]

    cv2.imwrite('finalanswersheet.jpg', warped)

    thresh_resize = resize(warped, height = 400)
    show(thresh_resize)
    return thresh


def sorted_contours(cnt, model='left-to-right'):
    if model == 'top-to-bottom':
        cnt = sorted(cnt, key=lambda x:cv2.boundingRect(x)[1])

    elif model == 'left-to-right':
        cnt = sorted(cnt, key=lambda x:cv2.boundingRect(x)[0])

    return cnt

# 正确答案
ANSWER_KEY = {0:1, 1:4, 2:0, 3:3, 4:1}

def answersheet_comparison(filename='finalanswersheet.jpg'):
    '''
        对变换后的图像进行操作（wraped），构造mask
        根据有无填涂的特性，进行位置的计算
    '''
    img = cv2.imread(filename)
    # print(img.shape)   # 156*194
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 对图像进行二值化操作
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    # show(thresh)

    # 对图像进行细微处理
    kernele = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, ksize=(3, 3))
    erode = cv2.erode(thresh, kernele)
    kerneld = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, ksize=(3, 3))
    dilate = cv2.dilate(erode, kerneld)
    # show(dilate)

    # 对图像进行轮廓检测
    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    # res = cv2.drawContours(img.copy(), cnts, -1, (0, 255, 0), 2)
    # # show(res)


    questionCnts = []
    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        arc = w/float(h)

        # 根据实际情况找出合适的轮廓
        if  w > 8 and h > 8 and arc >= 0.7 and arc <= 1.3:
            questionCnts.append(c)

    # print(len(questionCnts))  # 这里总共圈出五个轮廓 分别为五个位置的轮廓
    # 第四步，将轮廓进行从上到下的排序
    questionCnts = sorted_contours(questionCnts, model='top-to-bottom')
    # print(len(questionCnts))
    # res = cv2.drawContours(img.copy(), questionCnts[0], -1, (0, 255, 0), 2)
    # show(res)

    # 第五步  对每一行的轮廓进行遍历，构造掩码，对每一行答案的轮廓进行遍历
    xmin, ymin, xmax, ymax = 1000, 1000, 0, 0
    '''
        53 27 17 16     1  (1,0)
        116 52 17 16    4   (4, 1)
        32 76 17 17     0   (0, 2)
        74 101 17 17    2   (2, 3)
        52 126 18 16    1   (1, 4)
    '''
    # for i in questionCnts:
    #     x, y, w, h = cv2.boundingRect(i)
    #     if x<xmin:
    #         xmin = x
    #     if y<ymin:
    #         ymin = y
    #     if x>xmax:
    #         xmax = x
    #     if y>ymax:
    #         ymax = y
    # print(xmin, ymin, xmax, ymax)  # 32 27 116 126   99  84
    # 注意这里加的数据，是长宽w,h，
    # res  = cv2.rectangle(img.copy(), (xmin,ymin), (xmax+16,ymax+16), (0, 255, 0), 2)
    # show(res)
    correct = 0
    all_length = len(questionCnts)
    for i in range(len(questionCnts)):
        x, y, w, h = cv2.boundingRect(questionCnts[i])
        answer = round((x-32)/float(100)*5)
        print(ANSWER_KEY[i])
        if answer == ANSWER_KEY[i]:
            correct += 1
            img = cv2.drawContours(img, questionCnts[i], -1, 0, 2)
    
    score = float(correct)/float(all_length)
    print(correct, all_length, score)

    cv2.putText(img, 'correct_score:%s'%score, (10, 15), cv2.FONT_HERSHEY_SIMPLEX,
        0.4, 0.3)
    show(img)



def ocr_recognition(filename='tes.jpg'):
    img = Image.open(filename)
    text = pytesseract.image_to_string(img)
    print(text)


if __name__ == '__main__':
    # 获取矫正之后的图片
    # get_image_processingResult()
    answersheet_comparison()
