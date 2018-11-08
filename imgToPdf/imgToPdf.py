# -*- coding: UTF-8 -*-
# 需要安装依赖
# pip install reportlab

# 单张图片转pdf，图片不失真。比较清晰

import sys
from reportlab.lib.pagesizes import portrait
from reportlab.pdfgen import canvas
from PIL import Image
 
 
def imgtopdf(input_paths, outputpath):
    (maxw, maxh) = Image.open(input_paths).size
    c = canvas.Canvas(outputpath, pagesize=portrait((maxw, maxh)))
    c.drawImage(input_paths, 0, 0, maxw, maxh)
    c.showPage()
    c.save()
 
# 调用demo:
imgtopdf("test.jpg", "test.pdf")
print('转换成功！')

