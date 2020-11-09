#_*_coding:utf-8_*_
# matplotlib.pyplot 是一个python 的画图工具。下面用这个来可视化
import matplotlib.pyplot as plt
import tensorflow as tf
 
# 读取图像的原始数据
picture_path = 'kd.jpg'
image_raw_data = tf.gfile.FastGFile(picture_path, 'rb').read()
 
with tf.Session() as sess:
    # 将图像使用JPEG的格式解码从而得到图像对应的三维矩阵
    # TensorFlow提供了 tf.image.decode_png 函数对png格式的图像进行解码
    # 解码之后的结果为一个张量，在使用它的取值之前需要明确调用运行的过程
    img_data = tf.image.decode_jpeg(image_raw_data)
 
    # 输出解码之后的三维矩阵
    # print(img_data.eval())
    '''
        # 输出解码之后的三维矩阵如下：
    [[[4   6   5]
      [4   6   5]
     [4   6   5]
    ...
    [35 29  31]
    [26  20  24]
    [25 20 26]]]
    '''
     
 
    # 使用 pyplot工具可视化得到的图像
    plt.imshow(img_data.eval())
    plt.show()
 
    # 将数据的类型转化成实数方便下面的样例程序对图像进行处理
    # img_data = tf.image.convert_image_dtype(img_data, dtype=tf.float32)
    
    # 将表示一张图像的三维矩阵重新按照JPEG格式编码并存入文件中
    # 打开这种图片可以得到和原始图像一样的图像
    encoded_image = tf.image.encode_jpeg(img_data)
    with tf.gfile.GFile('output.jpg', 'wb') as f:
        f.write(encoded_image.eval())
