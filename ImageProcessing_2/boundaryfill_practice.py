import cv2
import matplotlib.pyplot as plt

img = cv2.imread('lena.jpg')
print(img.shape)
# (263, 263, 3)

# 为了展示效果，这里填充的大一些
top_size, bottom_size, left_size, right_size = (50, 50, 50, 50)

# 重复边界，填充  即复制最边缘像素
replicate = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size,
                               borderType=cv2.BORDER_REPLICATE)

# 反射边界，填充 即对感兴趣的图像中的像素在两边进行复制，例如 fedcba|abcdefgh|hgfedcb
reflect = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size,
                             borderType=cv2.BORDER_REFLECT)

# 反射101边界，填充 这个是以最边缘为轴，对称 ，例如 gfedcb|abcdefg|gfedcba
reflect_101 = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size,
                               borderType=cv2.BORDER_REFLECT_101)

# 外包装 填充  例如  cdefgh|abcdefgh|abcdegf
wrap = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size,
                               borderType=cv2.BORDER_WRAP)

# 常量填充，常量值可以自己设定
constant = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size,
                               borderType=cv2.BORDER_CONSTANT, value=0)

plt.subplot(231), plt.imshow(img, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect_101), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant), plt.title('CONSTANT')

plt.imshow(img)
plt.show()

# def show(image):
#     cv2.imshow('image', image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# show(img)
