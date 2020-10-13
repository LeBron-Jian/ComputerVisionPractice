import random
import cv2
from numpy import random
 
 
def GaussianNoise(src, means, sigma, percetage):
    NoiseImg = src
    NoiseNum = int(percetage * src.shape[0] * src.shape[1])
    for i in range(NoiseNum):
        randX = random.randint(0, src.shape[0] - 1)
        randY = random.randint(0, src.shape[1] - 1)
        # NoiseImg[randX, randY] = NoiseImg[randX, randY] + random.gauss(means, sigma)
        NoiseImg[randX, randY] = NoiseImg[randX, randY] + random.normal(means, sigma)
        if NoiseImg[randX, randY] < 0:
            NoiseImg[randX, randY] = 0
        elif NoiseImg[randX, randY] > 255:
            NoiseImg[randX, randY] = 255
    return NoiseImg
 
 
def PepperandSalt(src, percetage):
    NoiseImg = src
    NoiseNum = int(percetage * src.shape[0] * src.shape[1])
    for i in range(NoiseNum):
        #椒盐噪声图片边缘不处理，故-1
        randX = random.random_integers(0, src.shape[0] - 1)
        randY = random.random_integers(0, src.shape[1] - 1)
        if random.random_integers(0, 1) <= 0.5:
            NoiseImg[randX, randY] = 0
        else:
            NoiseImg[randX, randY] = 255
    return NoiseImg
 
 
def imageSumPepperandSalt(origin_path, save_path):
    img = cv2.imread(origin_path, 0)
    img1 = PepperandSalt(img, 0.2)
    cv2.imwrite(save_path, img1)
    cv2.imshow('PepperandSalt', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
 
def imageSumGaussianNoise(origin_path, save_path):
    img = cv2.imread(origin_path, 0)
    img1 = GaussianNoise(img, 2, 4, 0.8)
    cv2.imwrite(save_path, img1)
    cv2.imshow('GaussianNoise', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
def origin_show(origin_path):
    img = cv2.imread(origin_path, )
    # 灰度化
    # img = cv2.imread(origin_path, 0)
    cv2.imshow('origin', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
if __name__ == '__main__':
    origin_path = 'butterfly.jpg'
    save_path1 = 'butterfly_Gaussian.jpg'
    save_path2 = 'butterfly_Salt.jpg'
    origin_show(origin_path)
    imageSumGaussianNoise(origin_path, save_path1)
    imageSumPepperandSalt(origin_path, save_path2)
