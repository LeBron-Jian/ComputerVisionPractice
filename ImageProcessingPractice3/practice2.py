#_*_coding:utf-8_*_
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
 
# 读取图像的原始数据
picture_path = 'kd.jpg'
image_raw_data = tf.gfile.FastGFile(picture_path, 'rb').read()
 
with tf.Session() as sess:
    # 将图像使用JPEG的格式解码从而得到图像对应的三维矩阵
    # TensorFlow提供了 tf.image.decode_png 函数对png格式的图像进行解码
    # 解码之后的结果为一个张量，在使用它的取值之前需要明确调用运行的过程
    img_data = tf.image.decode_jpeg(image_raw_data)
 
    img_data.set_shape([300, 300, 3])
    print(img_data.get_shape())   # (300, 300, 3)
 
    # 重新调整图片的大小
    resized = tf.image.resize_images(img_data, [260, 260], method=0)
 
    # TensorFlow的函数处理图片后存储的数据是float32格式的，
    # 需要转换成uint8才能正确打印图片。
    resized_photo = np.asarray(resized.eval(), dtype='uint8')
    # tf.image.convert_image_dtype(rgb_image, tf.float32)
    plt.imshow(resized_photo)
    plt.show()
