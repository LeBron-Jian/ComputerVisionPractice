import cv2
from pylab import *
 
saber  = cv2.imread("construction.jpg")
# 首先将原图像进行边界扩展，并将其转换为灰度图。
gray_saber = cv2.cvtColor(saber,cv2.COLOR_RGB2GRAY)
gray_saber = cv2.resize(gray_saber,(200,200))
 
def RobertsOperator(roi):
    operator_first = np.array([[-1,0],[0,1]])
    operator_second = np.array([[0,-1],[1,0]])
    return np.abs(np.sum(roi[1:,1:]*operator_first))+np.abs(np.sum(roi[1:,1:]*operator_second))
 
def RobertsAlogrithm(image):
    image = cv2.copyMakeBorder(image,1,1,1,1,cv2.BORDER_DEFAULT)
    for i in range(1,image.shape[0]):
        for j in range(1,image.shape[1]):
            image[i,j] = RobertsOperator(image[i-1:i+2,j-1:j+2])
    return image[1:image.shape[0],1:image.shape[1]]
 
Robert_saber = RobertsAlogrithm(gray_saber)
plt.imshow(Robert_saber,cmap="binary")
plt.axis("off")
plt.show()
