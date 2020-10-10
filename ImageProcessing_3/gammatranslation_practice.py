import cv2
import numpy as np
import matplotlib.pyplot as plt
 
 
# 绘制曲线
def gamma_plot(c, gamma):
    x = np.arange(0, 256, 0.01)
    # y = c * x ** gamma
    y = c * np.power(x, gamma)
    plt.plot(x, y, 'r', linewidth=1)
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文标签
    plt.title(u'伽马变换函数')
    plt.xlim([0, 255]), plt.ylim([0, 255])
    plt.show()
 
 
# 伽玛变换
def gamma(img, c, gamma):
    # 映射表必须为0~255(改成其他会报错）
    gamma_table = c * [np.power(x/255.0, gamma) * 255.0 for x in range(256)]
    # Numpy数组默认数据类型为 int32，需要将数据类型转换为opencv图像适合使用的无符号八位整形
    # round() 方法返回浮点数x的四舍五入值。
    gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)
    output_img = cv2.LUT(img, gamma_table)
    return output_img
 
def gamma_1(img, c, gamma):
    # 映射表必须为0~255(改成其他会报错）
    output_img = c * np.power(img / float(np.max(img)), gamma) * 255.0
    output_img = np.uint8(output_img)
    return output_img
 
 
# 读取原始图像
img = cv2.imread('irving.jpg')
 
# 将图像转换为灰度，我们需要使用灰度图做gamma矫正
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
# 绘制伽玛变换曲线
gamma_plot(1, 4.0)
 
# 图像灰度伽玛变换
result = gamma(gray, 1, 0.4)
result1 = gamma_1(gray, 1, 0.4)
 
# 显示图像
cv2.imshow("Image", img)
cv2.imshow("Result", result)
cv2.imshow("Result 1", result1)
 
# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
