import cv2
import matplotlib.pyplot as plt


def bgr2yuv(img):
    yuv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    y, u, v = cv2.split(yuv_img)

    return y, u, v


def yuv2bgr(y, u, v):
    yuv_img = cv2.merge([y, u, v])
    bgr_img = cv2.cvtColor(yuv_img, cv2.COLOR_YUV2BGR)

    return bgr_img


def main():
    orig_img = cv2.imread('durant.jpg')
    gray = cv2.cvtColor(orig_img, cv2.COLOR_BGR2GRAY)
    y, u, v = bgr2yuv(orig_img)

    bgr_img = yuv2bgr(y, u, v)

    titles = ['orig_img', 'gray', 'Y channel','U channel','V channel','bgr_img']
    images = [orig_img, gray, y, u, v, bgr_img]
    for i in range(len(titles)):
        plt.subplot(2, 3, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == '__main__':
    main()
