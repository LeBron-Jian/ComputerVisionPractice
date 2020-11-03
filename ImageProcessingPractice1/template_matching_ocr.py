#_*_coding:utf-8_*_
import cv2
import numpy as np

# 指定信用卡类型
FIRST_NUMBER = {
    '3': "Amerian Express",
    '4': "Visa",
    '5': 'MasterCard',
    '6': 'Discover Card'
}


def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def sort_contours(cnts, method='left-to-right'):
    reverse = False
    i = 0

    if method == 'right-to-left' or method == 'bottom-to-top':
        reverse = True
    if method == 'top-to-bottom' or method == ' bottom-to-top':
        i = 1

    # 用一个最小的矩形，把找到的形状包起来 x, y, h, w
    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
    # #zip(*)相当于解压，是zip的逆过程
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
        key=lambda b: b[1][i], reverse=reverse))

    return cnts, boundingBoxes


def myresize(image, width=None, height=None, inter=cv2.INTER_AREA):
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


def trmplate_processing(template_image):
    # 读取模板图像
    template_img = cv2.imread(template_image)
    # cv_show('template_img', template_img)
    gray = cv2.cvtColor(template_img, cv2.COLOR_BGR2GRAY)
    # cv_show('gray', gray)
    # 二值图像
    ref = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY_INV)[1]
    # cv_show('ref', ref)

    # 计算轮廓
    # cv2.findContours() 函数接受的参数为二值图，即黑白的（不是灰度图）
    # cv2.RETR_EXTERNAL 只检测外轮廓  cv2.CHAIN_APPROX_SIMPLE 只保留终点坐标
    # 返回的list中每个元素都是图像中的一个轮廓
    refCnts, hierarchy = cv2.findContours(ref.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    drawimg = template_img.copy()
    cv2.drawContours(drawimg, refCnts, -1, (0, 0, 255), 3)
    # cv_show('drawimg', drawimg)
    # print(np.array(refCnts).shape)   # (10,)
    # 排序，从左到右，从上到下
    refCnts1 = sort_contours(refCnts, method='left-to-right')[0]  
    digits = {}
    # 遍历每一个轮廓
    for (i, c) in enumerate(refCnts1):
        # 计算外接矩阵并且resize成合适大小
        (x, y, w, h) = cv2.boundingRect(c)
        roi = ref[y:y+h, x:x+w]
        roi = cv2.resize(roi, (57, 88))

        # 每一个数字对应每个模板
        digits[i] = roi

    # print(digits)
    return digits

def origin_img_processing(origin_image, digits):
    # 读入输入图像，并进行预处理
    img = cv2.imread(origin_image)
    # cv_show('img', img)
    # print(img.shape)  # (368, 583, 3)
    img = myresize(img, width=300)
    # print(img.shape)  # (189, 300, 3)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv_show('gray', gray)

    # 初始化卷积核
    rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 3))
    sqKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    # 礼帽操作，突出更明显的区域
    tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)
    # cv_show('tophat', tophat)

    # ksize = -1 相当于用 3*3 的 ksize=-1
    gradX = cv2.Sobel(tophat, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
    # 下面np函数等价于  cv2.convertScaleAbs(gradX)
    gradX = np.absolute(gradX)
    # cv_show('gradX', gradX)
    (minVal, maxVal) = (np.min(gradX), np.max(gradX))
    gradX = (255*((gradX - minVal) / (maxVal - minVal)))
    gradX = gradX.astype('uint8')
    # print(np.array(gradX).shape)  # (189, 300)
    # cv_show('gradX', gradX)

    # 通过闭操作（先膨胀，再腐蚀）将数字连在一起
    gradX = cv2.morphologyEx(gradX, cv2.MORPH_CLOSE, rectKernel)
    # cv_show('gradX', gradX)
    # THRESH_OTSU 会自动寻找合适的阈值，适合双峰，需把阈值参数设置为0
    thresh = cv2.threshold(gradX, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # cv_show('thresh', thresh)

    # 再来一个闭操作  先膨胀后腐蚀
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, sqKernel)
    # cv_show('thresh_again', thresh)

    #计算轮廓
    threshCnts, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cur_img = img.copy()
    cv2.drawContours(cur_img, threshCnts, -1, (0, 0, 255), 3)
    # cv_show('cur_image', cur_img)

    locs = []
    # 遍历轮廓
    for (i, c) in enumerate(threshCnts):
        # 计算矩形
        (x, y, w, h) = cv2.boundingRect(c)
        ar = w / float(h)

        # 选择合适的区域，根据实际任务来，这里的基本都是四个数字一组
        if ar > 2.5 and ar<4.0:
            if (w > 40 and w < 55) and (h > 10 and h < 20):
                # 符合的留下来
                locs.append((x, y, w, h))

    # 将符合的轮廓从左到右排序
    locs = sorted(locs, key=lambda x:x[0])

    output = []
    # 遍历轮廓中每一个数字
    for (i, (gX, gY, gW, gH)) in enumerate(locs):
        # initialize the list of group digits
        groupOutput = []
        # 根据坐标提取每一个组
        group = gray[gY - 5: gY + gH + 6, gX - 5:gX + gW + 5]
        # cv_show('group', group)

        # 预处理
        group1 = cv2.threshold(group, 0, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)[1]
        # cv_show('group', group)
        # res = np.hstack((group, group1))
        # cv_show('group & threshold', res)

        # 计算每一组的轮廓
        digitCnts, hierarchy = cv2.findContours(group1.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        digitCnts = sort_contours(digitCnts, method='left-to-right')[0]

        # 计算每一组中的每一个数值
        for c in digitCnts:
            # 找到当前数值的轮廓，resize成合适的大小
            (x, y, w, h) = cv2.boundingRect(c)
            roi = group1[y:y+h, x:x+w]
            roi = cv2.resize(roi, (57, 88))
            # cv_show('roi', roi)

            # 计算匹配得分
            scores = []

            # 在模板中计算每一个得分
            for (digit, digitROI) in digits.items():
                # 模板匹配
                result = cv2.matchTemplate(roi, digitROI, cv2.TM_CCOEFF)
                (_, score, _, _) = cv2.minMaxLoc(result)
                scores.append(score)

            # 得到最合适的数字
            groupOutput.append(str(np.argmax(scores)))

        # 画出来
        cv2.rectangle(img, (gX-5, gY-5), (gX+gW+5, gY+gH+5), (0, 0, 255), 1)
        cv2.putText(img, "".join(groupOutput), (gX, gY-15), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 255), 2)

        # 得到结果
        output.extend(groupOutput)

    # 打印结果
    print('Credit Card Type: {}'.format(FIRST_NUMBER[output[0]]))
    print("Credit Card #: {}".format("".join(output)))
    cv_show('Image', img)



if __name__ == '__main__':
    origin_image = r'images/credit_card_01.png'
    template_image = r'images/ocr_a_reference.png'
    digits = trmplate_processing(template_image)
    origin_img_processing(origin_image, digits)
