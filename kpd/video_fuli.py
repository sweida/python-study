from requests_html import HTMLSession
import requests
import os
session = HTMLSession()
import json
import re



url = "https://www.45kpd.com"
fuli = url + '/fuli/pr/index_4.html'
r = session.get(fuli)

# # 新建data文件夹
# if not os.path.exists('data'):
#     os.mkdir('data')
sendData = []

items_a = r.html.find('ul.panel-list > li > a')
for abox in items_a:
    a_url = abox.attrs['href']
    if '/fuli' in a_url:
        if not abox.search('VIP视频'):
            img_url = url + abox.find('img', first=True).attrs['src']
            # print(img_url)
            # 视频详情页
            video_r = session.get(url + a_url)
            # 图片地址
            title = video_r.html.find('div.video-player-hd > h1', first=True)
            # 创建时间
            creatDate = abox.find('.fa-calendar-check-o', first=True)
            # 视频时长
            longTime = abox.find('.fa-clock-o', first=True)
            # 视频地址
            iframe = video_r.html.find('iframe', first=True)
            iframe_url = iframe.attrs['src']
            video_r = session.get(url + iframe_url)
            video_text = re.findall(r'https.*?\]', video_r.text)
            video_url = video_text[0][0: -2]
            # json
            jsondata = {
                'id':a_url[-10:-5] ,
                'image':abox.find('img', first=True).attrs['src'], 
                'creatDate': creatDate.text,
                'longTime': longTime.text,
                'title':title.text, 
                'video':video_url
            }
            sendData.append(jsondata)
            print(jsondata)

with open('data/fuli.js', 'w') as f:
    json.dump(sendData, f, ensure_ascii=False, sort_keys=True, indent=2)
print('微拍福利输入成功')
        



# url = 'https://www.44kpd.com/e/DownSys/play/?classid=5&id=10315&pathid=0'
# # text = "var video=['https://play.cdmbo.com/20180817/YWxT62BY/index.m3u8'];"
# r = session.get(url)

# # print(r.text)
# url = re.findall(r'https.*?\]', r.text)
# print(url[0][0: -2])
