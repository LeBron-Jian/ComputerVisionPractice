#_*_coding:utf-8_*_
import cv2
import numpy as np
 
 
def mask_processing(path):
    image = cv2.imread(path)  # 读图
    # cv2.imshow("Oringinal", image) #显示原图
    print(image.shape[:2])  # (458, 558)
 
    # 输入图像是RGB图像，故构造一个三维数组，四个二维数组是mask四个点的坐标，
    site = np.array([[[242, 3], [351, 3], [351, 111], [242, 111]]], dtype=np.int32)
 
    im = np.zeros(image.shape[:2], dtype="uint8")  # 生成image大小的全白图
 
    cv2.polylines(im, site, 1, 255)  # 在im上画site大小的线，1表示线段闭合，255表示线段颜色
    cv2.fillPoly(im, site, 255)  # 在im的site区域，填充颜色为255 白色
 
    mask = im
    cv2.namedWindow('Mask', cv2.WINDOW_NORMAL)  # 可调整窗口大小，不加这句不可调整
    cv2.imshow("Mask", mask)
    masked = cv2.bitwise_and(image, image, mask=mask)  # 在模板mask上，将image和image做“与”操作
    cv2.namedWindow('Mask to Image', cv2.WINDOW_NORMAL)  # 同上
    cv2.imshow("Mask to Image", masked)
    cv2.waitKey(0)  # 图像一直显示，键盘按任意键即可关闭窗口
    cv2.destroyAllWindows()
 
if __name__ == '__main__':
    path = 'irving.jpg'
    mask_processing(path)
