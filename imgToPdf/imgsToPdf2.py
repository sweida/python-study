# -*- coding: UTF-8 -*-
# 需要安装依赖
# pip install reportlab


########## 需要所有图片都是同一尺寸  不失真 ##########


import sys
from reportlab.lib.pagesizes import portrait
from reportlab.pdfgen import canvas
from PIL import Image

imgs = sys.argv[1:]

print(imgs)
f_pdf = 'allImg.pdf'


def imgtopdf():
    # 将第一张图片的大小设置为基本大小
    img1 = sys.argv[1]
    (maxw1, maxh1) = Image.open(img1).size
    c = canvas.Canvas(f_pdf, pagesize=(maxw1, maxh1))

    # 遍历所有图片
    for img in imgs:
        (maxw, maxh) = Image.open(img).size
        c.drawImage(img, 0, 0, maxw, maxh)
        c.showPage()
    c.save()


imgtopdf()
print('转换成功！')
