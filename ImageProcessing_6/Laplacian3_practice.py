import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import scipy.signal as signal     # 导入sicpy的signal模块

# Laplace算子
suanzi1 = np.array([[0, 1, 0],
                    [1,-4, 1],
                    [0, 1, 0]])

# Laplace扩展算子
suanzi2 = np.array([[1, 1, 1],
                    [1,-8, 1],
                    [1, 1, 1]])

# 打开图像并转化成灰度图像
image = Image.open("construction.jpg").convert("L")
image_array = np.array(image)

# 利用signal的convolve计算卷积
image_suanzi1 = signal.convolve2d(image_array,suanzi1,mode="same")
image_suanzi2 = signal.convolve2d(image_array,suanzi2,mode="same")

# 将卷积结果转化成0~255
image_suanzi1 = (image_suanzi1/float(image_suanzi1.max()))*255
image_suanzi2 = (image_suanzi2/float(image_suanzi2.max()))*255

# 为了使看清边缘检测结果，将大于灰度平均值的灰度变成255(白色)
image_suanzi1[image_suanzi1>image_suanzi1.mean()] = 255
image_suanzi2[image_suanzi2>image_suanzi2.mean()] = 255

# 显示图像
plt.subplot(2,1,1)
plt.imshow(image_array,cmap=cm.gray)
plt.axis("off")
plt.subplot(2,2,3)
plt.imshow(image_suanzi1,cmap=cm.gray)
plt.axis("off")
plt.subplot(2,2,4)
plt.imshow(image_suanzi2,cmap=cm.gray)
plt.axis("off")
plt.show()
