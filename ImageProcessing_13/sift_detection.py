import cv2
import numpy as np
 
img = cv2.imread('test_1.jpg')
print('imgshape', img.shape)
# imgshape (800, 1200, 3)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = np.float32(gray)
 
# 得到特征点
sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray, None)
# kp 是封装好的东西，我们看不见，只能展示
 
img = cv2.drawKeypoints(gray, kp, img)
 
img = cv2.resize(img, None, fx=0.5, fy=0.5)
cv2.imshow('dst', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
 
# 计算特征
kp, des = sift.compute(gray, kp) 
print(np.array(kp).shape)  # (6827,)
print(des.shape)  # (6827, 128)
print(des[0])
 
'''
[  0.   0.   0.   0.   0.   0.   0.   0.  21.   8.   0.   0.   0.   0.
   0.   0. 157.  31.   3.   1.   0.   0.   2.  63.  75.   7.  20.  35.
  31.  74.  23.  66.   0.   0.   1.   3.   4.   1.   0.   0.  76.  15.
  13.  27.   8.   1.   0.   2. 157. 112.  50.  31.   2.   0.   0.   9.
  49.  42. 157. 157.  12.   4.   1.   5.   1.  13.   7.  12.  41.   5.
   0.   0. 104.   8.   5.  19.  53.   5.   1.  21. 157.  55.  35.  90.
  22.   0.   0.  18.   3.   6.  68. 157.  52.   0.   0.   0.   7.  34.
  10.  10.  11.   0.   2.   6.  44.   9.   4.   7.  19.   5.  14.  26.
  37.  28.  32.  92.  16.   2.   3.   4.   0.   0.   6.  92.  23.   0.
   0.   0.]
'''
