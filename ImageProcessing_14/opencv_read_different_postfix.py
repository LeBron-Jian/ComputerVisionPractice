import sys
import os
import numpy as np
 
 
def count_pixel_values(image):
    count_res = {}
    # 统计像素值数量
    pixel_counts = np.bincount(image.flatten())
    # 显示结果
    for pixel_value, count in enumerate(pixel_counts):
        if count > 0:
            count_res[pixel_value] = count
    return count_res
 
 
# 读取一张图像，将其转换为灰度图
image = cv2.imread(r"./Abyssinian_1.png", 0)
 
# 创建二值图像
binary_image = np.zeros_like(image, dtype=np.uint8)
binary_image[image == 1] = 0  # 像素值1对应0像素
binary_image[image == 2] = 125  # 像素值2对应125像素
binary_image[image == 3] = 255  # 像素值3对应255像素
 
# 1, 我将二值图结果保存为jpg 和png，我们分别看看
# cv2.imwrite(r"./cat.png", binary_image)
# cv2.imwrite(r"./cat.jpg", binary_image)
 
# 2, 我分别打开png 和 jpg 的图像
 
png_mask = cv2.imread(r"./cat.png", 0)
jpg_mask = cv2.imread(r"./cat.jpg", 0)
print(np.array_equal(png_mask, binary_image), np.sum(png_mask != binary_image))
pixel_counts_png = count_pixel_values(png_mask)
print(pixel_counts_png)
print(np.array_equal(jpg_mask, binary_image), np.sum(jpg_mask != binary_image))
pixel_counts_jpg = count_pixel_values(jpg_mask)
print(pixel_counts_jpg)
 
# 使用sys.getsizeof()函数来获取图像对象的大小
# 使用os.path.getsize()函数来获取图像文件的大小
binary_image_memory_size = sys.getsizeof(binary_image)
png_mask_memory_size = sys.getsizeof(png_mask)
jpg_mask_memory_size = sys.getsizeof(jpg_mask)
print("二值图图像内存大小: {} 字节".format(binary_image_memory_size))
print("jpg二值图图像内存大小: {} 字节".format(png_mask_memory_size))
print("png二值图图像内存大小: {} 字节".format(jpg_mask_memory_size))
binary_image_file_size = os.path.getsize(r"./Abyssinian_1.png")
png_mask_file_size = os.path.getsize(r"./cat.png")
jpg_mask_file_size = os.path.getsize(r"./cat.jpg")
print("二值图图像文件大小: {} 字节".format(binary_image_file_size))
print("jpg二值图图像文件大小: {} 字节".format(png_mask_file_size))
print("png二值图图像文件大小: {} 字节".format(jpg_mask_file_size))
