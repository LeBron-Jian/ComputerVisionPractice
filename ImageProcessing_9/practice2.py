import cv2
import numpy as np
import matplotlib.pyplot as plt
 
 
def LookUpTable(photo_path):
    image = cv2.imread(photo_path, 0)
    # 创建空的查找表
    lut = np.zeros(256, dtype=image.dtype)
    # OpenCV提供了cv.calcHist()函数来获取直方图
    hist = cv2.calcHist([image],  # 计算图像的直方图
                        [0],  # 使用的通道
                        None,  # 没有使用mask
                        [256],  # it is a 2D histogram
                        [0.0, 255.0])
    # print(hist.shape)  # (256, 1)
    minBinNo, maxBinNo = 0, 255
 
    # 计算从左起第一个不为0的直方图位置
    for binNo, binValue in enumerate(hist):
        if binValue != 0:
            minBinNo = binNo
            break
 
    # 计算从右起第一个不为0的直方图位置
    for binNo, binValue in enumerate(reversed(hist)):
        if binValue != 0:
            maxBinNo = 255 - binNo
            break
 
    # 生成查找表
    for i, v in enumerate(lut):
        if i < minBinNo:
            lut[i] = 0
        elif i > maxBinNo:
            lut[i] = 255
        else:
            lut[i] = int(255.0 * (i - minBinNo) / (maxBinNo - minBinNo) + 0.5)
 
    # 计算
    lut = cv2.LUT(image, lut)
    cv2.imwrite('lut.jpg', lut)
    # cv2.imshow('lut', lut)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return lut
 
 
def opencv_equalizeHist(image_path):
    img = cv2.imread(image_path, 0)
    equ = cv2.equalizeHist(img)
    cv2.imwrite('equ.jpg', equ)
    # cv2.imshow('equ', equ)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return equ
 
 
def numpy_equalizeHist(image_path):
    img = cv2.imread(image_path, 0)
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    # 计算累计直方图
    cdf = hist.cumsum()
    # 除以直方图中的0值
    cdf_m = np.ma.masked_equal(cdf, 0)
    # 等同于前面介绍的lut[i] = int(255.0 *p[i])公式
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    # 将掩模处理掉的元素补为0
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')
    # 计算
    numpy_lut = cdf[img]
    cv2.imwrite('numpy_lut.jpg', numpy_lut)
    # cv2.imshow("NumPyLUT", numpy_lut)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return numpy_lut
 
 
def show_allphoto():
    lut = cv2.imread('lut.jpg', 0)
    np_equ = cv2.imread('numpy_lut.jpg', 0)
    opencv_equ = cv2.imread('equ.jpg', 0)
    print(lut.shape,  np_equ.shape, opencv_equ.shape)
 
    lut = cv2.calcHist([lut], [0], None, [256], [0.0, 256.0])
    np_equ = cv2.calcHist([np_equ], [0], None, [256], [0.0, 256.0])
    opencv_equ = cv2.calcHist([opencv_equ], [0], None, [256], [0.0, 256.0])
 
    plt.subplot(311), plt.plot(lut)
    plt.subplot(312), plt.plot(np_equ)
    plt.subplot(313), plt.plot(opencv_equ)
    plt.show()
 
 
 
if __name__ == '__main__':
    photo_path = 'wiki.jpg'
    # lut = LookUpTable(photo_path)
    # np_equ = numpy_equalizeHist(photo_path)
    # opencv_equ = opencv_equalizeHist(photo_path)
    show_allphoto()
