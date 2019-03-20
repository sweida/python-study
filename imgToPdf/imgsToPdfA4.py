# -*- coding: UTF-8 -*-
# 需要安装依赖
# pip install reportlab

# 需求：
# 当有的图比较大时，
#  1、当宽比较大时
#     让宽缩为默认宽度，上下留白
#  2、当高比较大时
#     让高缩小为默认宽度，左右留白

# 当图片比一般图片小时
#  1、一种方案是不拉伸，
#  2、一种方案是拉伸到普通图片大小


########## 按照第一张图为基准，将后面的图都按照它的比例放缩 ##########
import sys
import os
from reportlab.lib.pagesizes import portrait
from reportlab.pdfgen import canvas
from PIL import Image


files = input('请输入图片所在文件夹名：')
f_pdf = files + '/perfer.pdf'

def imgsToPdf():
    file_list = os.listdir(files)
    pic_name = []

    for x in file_list:
        if "jpg" in x or 'png' in x or 'jpeg' in x:
            pic_name.append(x)

    pic_name.sort()

    # 将第一张图片的大小设置为基本大小 拼接路径
    defaultImg = pic_name[0]
    imgPath = os.path.join(files, defaultImg)
    (firstW, firstH) = Image.open(imgPath).size
    c = canvas.Canvas(f_pdf, pagesize=(firstW, firstH))

    # (firstW, firstH) = (800, 1132)
    # c = canvas.Canvas(f_pdf, pagesize=((firstW, firstH)))

    # 遍历所有图片
    for imgName in pic_name:
        imgPath = os.path.join(files, imgName)

        img = Image.open(imgPath)
        (imgW, imgH) = img.size                 # 图片大小

        bili = firstW / firstH                  # 第一张图比例

        h = firstW * imgH / imgW                # 压缩后的高度
        w = firstH * imgW / imgH                # 压缩后的宽度

        marginTop = (firstH - h) / 2         # 上下留白大小
        marginWidth = (firstW - w) / 2       # 左右留白大小

        # 宽图
        if (imgW / imgH) >= bili:
            c.drawImage(imgPath, 0, marginTop, firstW, h)
        # 竖图
        else:
            c.drawImage(imgPath, marginWidth, 0, w, firstH)

        c.showPage()
    c.save()

print('图片转换pdf中...请稍等')

imgsToPdf()
print('转换成功！')
