#_*_coding:utf-8_*_
from PIL import Image
from PIL import ImageEnhance
from numpy import *
from pylab import *
from scipy.ndimage import filters

image1 = Image.open('construction.jpg').convert('L')
im = array(image1)
#soble 导数滤波器  使用 Sobel 滤波器来计算 x 和 y 的方向导数，
imx = zeros(im.shape)
# print(imx)
filters.sobel(im,1,imx)

imy = zeros(im.shape)
filters.sobel(im,0,imy)

magnitude = sqrt(imx**2 + imy**2)
# print(magnitude)
def deal_with(a):
    for i in range(len(a)):
        if a[i] <50:
            a[i] =0
        elif a[i] >200:
            a[i] =255
        # else:
        #     a[i] = 155
    return a
a = np.apply_along_axis(deal_with,1,magnitude)
result =  contour(magnitude, origin='image')
axis('equal')
axis('off')
figure()
hist(magnitude.flatten(),128)
show()
