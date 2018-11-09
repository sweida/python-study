# -*- coding: UTF-8 -*-
# 需要安装依赖
# pip install reportlab

# 单张图片转pdf，图片不失真。比较清晰

import sys
from reportlab.lib.pagesizes import portrait
from reportlab.pdfgen import canvas
from PIL import Image
 
# 如果有输指定文件则转换参数里的图片，否则转换test.jpg文件
if len(sys.argv) > 1:
    img = sys.argv[1]
    filename = img.split('.')[0]
    f_jpg = filename+'.jpg'
    f_pdf = filename+'.pdf'
    print(f_jpg)

else:
    img = 'test.jpg'
    f_pdf = 'test.pdf'


def imgtopdf():
    (maxw, maxh) = Image.open(img).size
    c = canvas.Canvas(f_pdf, pagesize=(maxw, maxh))
    c.drawImage(img, 0, 0, maxw, maxh)
    c.showPage()
    c.save()
 

imgtopdf()
print('转换成功！')

