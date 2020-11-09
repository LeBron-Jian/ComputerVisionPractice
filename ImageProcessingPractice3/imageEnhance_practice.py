from PIL import Image
from PIL import ImageEnhance
# 原始图像
image = Image.open('deal_with/A1.jpg')
image.show()
 
#亮度增强
enh_bri = ImageEnhance.Brightness(image)
brightness = 1.5
image_brightened = enh_bri.enhance(brightness)
image_brightened.show()
image_brightened.save("image_brightened.jpg")
 
#色度增强
enh_col = ImageEnhance.Color(image)
color = 1.5
image_colored = enh_col.enhance(color)
image_colored.show()
image_colored.save("image_colored.jpg")
 
#对比度增强
enh_con = ImageEnhance.Contrast(image)
contrast = 1.5
image_contrasted = enh_con.enhance(contrast)
image_contrasted.show()
image_contrasted.save("image_contrasted.jpg")
 
#锐度增强
enh_sha = ImageEnhance.Sharpness(image)
sharpness = 3.0
image_sharped = enh_sha.enhance(sharpness)
image_sharped.show()
image_sharped.save("image_sharped.jpg")
