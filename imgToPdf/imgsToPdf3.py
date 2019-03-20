import sys
import os
from reportlab.lib.pagesizes import portrait
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from PIL import Image


(pdfWidth, pdfHeight) = (1200, 1697)
c = canvas.Canvas('aa.pdf', pagesize=((pdfWidth, pdfHeight)))
bili = pdfWidth / pdfHeight

imgPath = '000.png'
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

# c.drawString(100, 100, "Some text in first page.")
c.showPage()
c.save()
# print(c)

# f_pdf = 'zai/allImg.pdf'


# def imgsToPdf():
#     file_list = os.listdir('zai')
#     pic_name = []

#     for x in file_list:
#         if "jpg" in x or 'png' in x or 'jpeg' in x:
#             pic_name.append(x)

#     pic_name.sort()

#     # 将第一张图片的大小设置为基本大小
#     defaultImg = pic_name[0]
#     imgPath = os.path.join('zai', defaultImg)
#     # print(imgPath)
#     (maxw1, maxh1) = Image.open(imgPath).size
#     c = canvas.Canvas(f_pdf, pagesize=(maxw1, maxh1))
#     # (w, h) = landscape(A4)
#     # c = canvas.Canvas(f_pdf, pagesize=landscape(A4))

#     # 遍历所有图片
#     for imgName in pic_name:
#         imgPath = os.path.join('zai', imgName)
#         # print(imgPath)
#         img = Image.open(imgPath)
#         (imgw, imgh) = img.size
#         marginTop = (h - imgh) / 2
#         marginWidth = (w - imgw) / 2
#         c.drawImage(imgPath, marginWidth, marginTop, imgw, imgh)
#         c.showPage()
#     c.save()


# imgsToPdf()
# print('转换成功！')
