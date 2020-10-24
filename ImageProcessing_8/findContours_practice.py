import cv2

img = cv2.imread('contour.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print (type(contours))
print (type(contours[0]))
print (len(contours))
'''
结果如下：
    <class 'list'>
    <class 'numpy.ndarray'>
    2
'''
print(len(contours[0]))
print(len(contours[1]))
'''
结果如下：
        4
        368
'''
print (type(hierarchy))
print (hierarchy.ndim)
print (hierarchy[0].ndim)
print (hierarchy.shape)
'''
结果如下：
        <class 'numpy.ndarray'>
        3
        2
        (1, 2, 4)
'''

# cv2.imshow('thresh', thresh)
# cv2.waitKey(0)
# cv2.destroyWindow('thresh')
