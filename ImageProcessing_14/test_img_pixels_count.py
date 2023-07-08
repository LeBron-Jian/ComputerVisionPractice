import cv2
from PIL import Image
import numpy as np
 
"""
测试任务：
    1，使用opencv直接读取png图像
    2，使用opencv读取png图像，以原始的通道顺序读取PNG图像，而不进行任何颜色通道的转换
    3，使用PIL库读取png图像
    4，判断opencv读取的图像是否修改像素值
 
测试方案及结论：
    1，使用语义分割的mask图像，像素只有1，2，3进行测试。
        测试结果如下：
                cv_img shape:  (400, 600)
                cv_origin_img shape:  (400, 600)
                pil_img_np shape:  (400, 600)
                0
                0
                pixel_counts_png_cv1:  {1: 22938, 2: 198766, 3: 18296}
                pixel_counts_png_cv2:  {1: 22938, 2: 198766, 3: 18296}
                pixel_counts_png_pil:  {1: 22938, 2: 198766, 3: 18296}
        测试结论：
            对于像素只有1，2，3的图像，无论用什么读取结果都一样。
             
    2, 测试我截图的那个哥们，我使用的是PNG图片，而且是8bit的深度，但是有些图像会不变，有些会变。
        使用语义分割的mask图像，是彩色图像。
        测试结果如下：
            cv_img shape:  (468, 625)
            cv_origin_img shape:  (468, 625, 3)
            pil_img_np shape:  (468, 625)
            128589
            1
            pixel_counts_png_cv1:  {0: 163911, 15: 16626, 72: 36210, 75: 5261, 95: 12644, 135: 37681, 220: 20167}
            pixel_counts_png_cv2:  {0: 584361, 64: 12644, 128: 133459, 192: 106702, 224: 40334}
            pixel_counts_png_pil:  {0: 163911, 2: 5261, 4: 16626, 13: 36210, 25: 12644, 39: 37681, 255: 20167}
            385767
             
        测试结论：
            对于像素存在多个不同的pixel的话，可以看出opencv读取数据，会修改像素值。
"""
 
 
def count_pixel_values(image):
    count_res = {}
    # 统计像素值数量
    pixel_counts = np.bincount(image.flatten())
    # 显示结果
    for pixel_value, count in enumerate(pixel_counts):
        if count > 0:
            count_res[pixel_value] = count
    return count_res
 
 
# img_path = r"./Abyssinian_1.png"
img_path = r"./000004.png"
 
# opencv 直接读取图像（会默认转换为BGR）
cv_img = cv2.imread(img_path)
# 因为我们知道要对比的是单通道的图像，所以先转换为灰度图
cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
 
# opencv读取原始通道
cv_origin_img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
 
# PIL 库读取image
 
pil_img = Image.open(img_path)
pil_img_np = np.array(pil_img)
print("cv_img shape: ", cv_img.shape)
print("cv_origin_img shape: ", cv_origin_img.shape)
print("pil_img_np shape: ", pil_img_np.shape)
 
print(np.sum(cv_img != pil_img_np))
print(np.sum(cv_origin_img != pil_img_np))
pixel_counts_png_cv1 = count_pixel_values(cv_img)
pixel_counts_png_cv2 = count_pixel_values(cv_origin_img)
pixel_counts_png_pil = count_pixel_values(pil_img_np)
print("pixel_counts_png_cv1: ", pixel_counts_png_cv1)
print("pixel_counts_png_cv2: ", pixel_counts_png_cv2)
print("pixel_counts_png_pil: ", pixel_counts_png_pil)
 
merge_cv = cv2.merge([cv_img, cv_img, cv_img])
merge_pil = cv2.merge([pil_img_np, pil_img_np, pil_img_np])
print(np.sum(merge_cv != merge_pil))
