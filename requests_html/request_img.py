import requests
import os
session = requests.session()


# 背景图片地址
url = "http://www.win4000.com/wallpaper_2285_0_10_1.html"
r = session.get(url)

# 新建bg文件夹
if not os.path.exists('bg'):
    os.mkdir('bg')

def save_image(url, title):
    img_response = requests.get(url)
    with open('./bg/'+title+'.jpg', 'wb') as file:
        file.write(img_response.content)

# 查找页面中图片列表，找到链接，
# 点击链接，访问查看大图，并获取大图地址pic-large
items_img = r.html.find('ul.clearfix > li > a')
for img in items_img:
    img_url = img.attrs['href']
    if "/wallpaper_detail" in img_url:
        r = session.get(img_url)          # 解析图片详情
        item_img = r.html.find('img.pic-large', first=True)
        url = item_img.attrs['src']       # 大图图片地址
        title = item_img.attrs['title']   # 图片标题
        print(url+title)
        save_image(url, title)
