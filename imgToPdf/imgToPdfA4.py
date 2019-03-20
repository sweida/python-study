# python imgToPdfA4.py 002.jpg

import sys
import os
from reportlab.lib.pagesizes import portrait
from reportlab.pdfgen import canvas
from PIL import Image

# 获取输入框的值，第二个参数
img = sys.argv[1]
print(img)
if (img):
    imgPath = img
else:
    imgPath = '001.jpg'

(pdfWidth, pdfHeight) = (1200, 1697)
c = canvas.Canvas('aa.pdf', pagesize=((pdfWidth, pdfHeight)))
bili = pdfWidth / pdfHeight


(imgW, imgH) = Image.open(imgPath).size

if ((imgW > pdfWidth) or (imgH > pdfHeight)):
    h = pdfWidth * imgH / imgW
    w = pdfHeight * imgW / imgH
    marginWidth = (pdfWidth - w) / 2
    marginTop = (pdfHeight - h) / 2
    # 宽图
    if (imgW / imgH) >= bili:
        c.drawImage(imgPath, 0, marginTop, pdfWidth, h)
    # 竖图
    else:
        c.drawImage(imgPath, marginWidth, 0, w, pdfHeight)
else:
    paddingWidth = (pdfWidth - imgW) / 2
    paddingHeight = (pdfHeight - imgH) / 2
    c.drawImage(imgPath, paddingWidth, paddingHeight, imgW, imgH)

c.showPage()
c.save()
print('转换成功')
