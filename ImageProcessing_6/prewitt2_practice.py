import cv2
from pylab import *

saber  = cv2.imread("construction.jpg")
# 首先将原图像进行边界扩展，并将其转换为灰度图。
gray_saber = cv2.cvtColor(saber,cv2.COLOR_RGB2GRAY)
gray_saber = cv2.resize(gray_saber,(200,200))


def PreWittOperator(roi, operator_type):
    if operator_type == "horizontal":
        prewitt_operator = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
    elif operator_type == "vertical":
        prewitt_operator = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    else:
        raise ("type Error")
    result = np.abs(np.sum(roi * prewitt_operator))
    return result


def PreWittAlogrithm(image, operator_type):
    new_image = np.zeros(image.shape)
    image = cv2.copyMakeBorder(image, 1, 1, 1, 1, cv2.BORDER_DEFAULT)
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            new_image[i - 1, j - 1] = PreWittOperator(image[i - 1:i + 2, j - 1:j + 2], operator_type)
    new_image = new_image * (255 / np.max(image))
    return new_image.astype(np.uint8)


plt.subplot(121)
plt.title("horizontal")
plt.imshow(PreWittAlogrithm(gray_saber,"horizontal"),cmap="binary")
plt.axis("off")
plt.subplot(122)
plt.title("vertical")
plt.imshow(PreWittAlogrithm(gray_saber,"vertical"),cmap="binary")
plt.axis("off")
plt.show()
