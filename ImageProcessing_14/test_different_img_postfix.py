from PIL import Image
 
"""
使用PIL库保存不同格式的图像（常见的转换，比如jpg转png， png转jpg）
这里验证的是：
    1，将 jpg 转换为 png，并保存
    2，将保存的png 读取出来再保存为 jpg
    3，对于保存的jpg 和原始的jpg 看结果是否相等
     
结论：
    False
    原因：
    JPEG格式对图像进行压缩时，会丢失一些细节和像素信息，因此还原回去的图像与原始的PNG图像可能存在一些差异。
    将PNG图像保存为JPEG格式会引起一定程度的图像压缩损失，因为JPEG是一种有损压缩格式。因此，还原回去的图像和原始的img不会完全相等。
 
"""
 
# step1: 将 jpg 格式保存为png
img_jpg = Image.open("./test/cat.jpg")
# save()有两个参数，第一个是保存转换后文件的文件路径，第二个参数是要转换的文件格式。
img_jpg.save("./test/cat_jpg2png.png", "PNG")
 
#
img_png = Image.open("./test/cat_jpg2png.png")
img_png.save("./test/cat_jpg2png2jpg.jpg", "JPEG")
 
img_origin_jpg = Image.open("./test/cat.jpg")
img_convert_jpg = Image.open("./test/cat_jpg2png2jpg.jpg")
print(img_origin_jpg.getdata(), type(img_convert_jpg.getdata()))
# <ImagingCore object at 0x000001D5E4197590> <class 'ImagingCore'>
pixels1 = list(img_origin_jpg.getdata())
pixels2 = list(img_convert_jpg.getdata())
print(pixels1 == pixels2)
# False
