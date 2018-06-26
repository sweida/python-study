# 操作图片
from PIL import Image, ImageFilter, ImageDraw, ImageFont 

# # 缩小图片
# im = Image.open('duola.jpg')
# # 获得图像尺寸:
# w, h = im.size
# print('Oringinal image size: %s%s' % (w, h))
# # 缩放到50%:
# im.thumbnail((w//2, h//2))
# print('Resize image to: %s%s:' % (w//2, h//2))
# # 把缩放后的图像用jpeg格式保存:
# im.save('thumbnail.jpg', 'jpeg')



# # 模糊图片
# im = Image.open('duola.jpg')
# mohu = im.filter(ImageFilter.BLUR)
# mohu.save('mohu.jpg', 'jpeg')



import random

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 画布颜色
def rndColor():
    return (random.randint(200, 255), random.randint(200, 255), random.randint(200, 255))
# 字体颜色
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建font对象
font = ImageFont.truetype('./UUSUNInchike.ttf', 36)
# 创建draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())

# 输出文字
for t in range(4):
    draw.text((60 * t +10, 10), rndChar(), font=font, fill=rndColor2())

# 模糊
# image = image.filter(ImageFilter.BLUR)

image.save('code.jpg', 'jpeg')






