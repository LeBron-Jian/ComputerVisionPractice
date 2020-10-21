import cv2
from pylab import *

saber  = cv2.imread("construction.jpg")
# 首先将原图像进行边界扩展，并将其转换为灰度图。
gray_saber = cv2.cvtColor(saber,cv2.COLOR_RGB2GRAY)
gray_saber = cv2.resize(gray_saber,(200,200))


def GaussianOperator(roi):
    GaussianKernel = np.array([[1,2,1],[2,4,2],[1,2,1]])
    result = np.sum(roi*GaussianKernel/16)
    return result

def GaussianSmooth(image):
    new_image = np.zeros(image.shape)
    image = cv2.copyMakeBorder(image,1,1,1,1,cv2.BORDER_DEFAULT)
    for i in range(1,image.shape[0]-1):
        for j in range(1,image.shape[1]-1):
            new_image[i-1,j-1] =GaussianOperator(image[i-1:i+2,j-1:j+2])
    return new_image.astype(np.uint8)

smooth_saber = GaussianSmooth(gray_saber)
plt.subplot(121)
plt.title("Origin Image")
plt.axis("off")
plt.imshow(gray_saber,cmap="gray")
plt.subplot(122)
plt.title("GaussianSmooth Image")
plt.axis("off")
plt.imshow(smooth_saber,cmap="gray")
plt.show()
