# 用来转化图像格式的
img = cv2.cvtColor(src,
   COLOR_BGR2HSV # BGR---->HSV
   COLOR_HSV2BGR # HSV---->BGR
   ...)
# For HSV, Hue range is [0,179], Saturation range is [0,255] and Value range is [0,255]
 
 
# 返回一个阈值，和二值化图像，第一个阈值是用来otsu方法时候用的
# 不过现在不用了，因为可以通过mahotas直接实现
T = ret = mahotas.threshold(blurred)
ret, thresh_img = cv2.threshold(src, # 一般是灰度图像
   num1, # 图像阈值
   num2, # 如果大于或者num1, 像素值将会变成 num2
# 最后一个二值化参数
   cv2.THRESH_BINARY      # 将大于阈值的灰度值设为最大灰度值，小于阈值的值设为0
   cv2.THRESH_BINARY_INV  # 将大于阈值的灰度值设为0，大于阈值的值设为最大灰度值
   cv2.THRESH_TRUNC       # 将大于阈值的灰度值设为阈值，小于阈值的值保持不变
   cv2.THRESH_TOZERO      # 将小于阈值的灰度值设为0，大于阈值的值保持不变
   cv2.THRESH_TOZERO_INV  # 将大于阈值的灰度值设为0，小于阈值的值保持不变
)
thresh = cv2.AdaptiveThreshold(src,
   dst,
   maxValue,
   # adaptive_method
   ADAPTIVE_THRESH_MEAN_C,     
   ADAPTIVE_THRESH_GAUSSIAN_C,     
   # thresholdType
   THRESH_BINARY,
   THRESH_BINARY_INV,
   blockSize=3,
   param1=5
)
 
 
# 一般是在黑色背景中找白色物体，所以原始图像背景最好是黑色
# 在执行找边缘的时候，一般是threshold 或者是canny 边缘检测后进行的。
# warning:此函数会修改原始图像、
# 返回：坐标位置（x,y）,
(_, cnts, _) = cv2.findContours(mask.copy(),
   # cv2.RETR_EXTERNAL,             #表示只检测外轮廓
   # cv2.RETR_CCOMP,                #建立两个等级的轮廓,上一层是边界
   cv2.RETR_LIST,                 #检测的轮廓不建立等级关系
   # cv2.RETR_TREE,                   #建立一个等级树结构的轮廓
   # cv2.CHAIN_APPROX_NONE,           #存储所有的轮廓点，相邻的两个点的像素位置差不超过1
   cv2.CHAIN_APPROX_SIMPLE,       #例如一个矩形轮廓只需4个点来保存轮廓信息
   # cv2.CHAIN_APPROX_TC89_L1,
   # cv2.CHAIN_APPROX_TC89_KCOS
  )
img = cv2.drawContours(src, cnts, whichToDraw(-1), color, line)
 
 
img = cv2.imwrite(filename, dst,  # 文件路径，和目标图像文件矩阵
    
   # 对于JPEG，其表示的是图像的质量，用0-100的整数表示，默认为95
   # 注意，cv2.IMWRITE_JPEG_QUALITY类型为Long，必须转换成int
   [int(cv2.IMWRITE_JPEG_QUALITY), 5]
   [int(cv2.IMWRITE_JPEG_QUALITY), 95]
   # 从0到9,压缩级别越高，图像尺寸越小。默认级别为3
   [int(cv2.IMWRITE_PNG_COMPRESSION), 5])
   [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
 
# 如果你不知道用哪个flags，毕竟太多了哪能全记住，直接找找。
寻找某个函数或者变量
events = [i for i in dir(cv2) if 'PNG' in i]
print( events )
 
寻找某个变量开头的flags
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print flags
 
批量读取文件名字
import os
filename_rgb = r'C:\Users\aixin\Desktop\all_my_learning\colony\20170629'
for filename in os.listdir(filename_rgb):              #listdir的参数是文件夹的路径
   print (filename)
