# -*- coding: UTF-8 -*-
# 需要安装依赖
# pip install reportlab



import sys
from reportlab.pdfgen import canvas
 

# 生成多张pdf
def texttopdf():
    c = canvas.Canvas('text.pdf')
    c.drawString(100, 100, "Some text in first page.")
    c.showPage()

    c.drawString(100, 100, "Some text in second page.")
    c.showPage()

    c.drawString(100, 100, "Some text in third page")
    c.showPage()

    c.save()
 

texttopdf()
print('转换成功！')

