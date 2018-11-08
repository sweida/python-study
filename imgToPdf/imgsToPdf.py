#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 将当前文件加下的所有图片合成pdf，
# 图片会压缩一点，有点失真

from PIL import Image
import os


def rea(pdf_name):
    file_list = os.listdir('.')
    pic_name = []
    im_list = []
    for x in file_list:
        if "jpg" in x or 'png' in x or 'jpeg' in x:
            pic_name.append(x)

    pic_name.sort()
    new_pic = []

    for x in pic_name:
        if "jpg" in x:
            new_pic.append(x)

    for x in pic_name:
        if "png" in x:
            new_pic.append(x)

    print("hec", new_pic)

    # 先取出第一张图片生成pdf，再把剩余的图片append到pdf文件中
    im1 = Image.open(new_pic[0])
    new_pic.pop(0)
    for i in new_pic:
        img = Image.open(i)
        # im_list.append(Image.open(i))
        if img.mode == "RGBA":
            img = img.convert('RGB')
            im_list.append(img)
        else:
            im_list.append(img)
    im1.save(pdf_name, "PDF", resolution=100.0,
             save_all=True, append_images=im_list)
    print("输出文件名称：", pdf_name)


if __name__ == '__main__':
    tttt = """

  _____ _____ _____   _______ ____    _____  _____  ______ 
 |  __ \_   _/ ____| |__   __/ __ \  |  __ \|  __ \|  ____|
 | |__) || || |         | | | |  | | | |__) | |  | | |__   
 |  ___/ | || |         | | | |  | | |  ___/| |  | |  __|  
 | |    _| || |____     | | | |__| | | |    | |__| | |     
 |_|   |_____\_____|    |_|  \____/  |_|    |_____/|_|     


"""

    pdf_name = input("请输入合成PDF文件名称：")
    if ".pdf" in pdf_name:
        rea(pdf_name=pdf_name)
    else:
        rea(pdf_name="{}.pdf".format(pdf_name))
    print('pdf文件生成完毕！')

