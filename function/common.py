from requests_html import HTMLSession
import requests
import os
session = HTMLSession()
import json
import re
import io


def getDatalist(date, url, route, filename, name):
    today = date
    href = url + route
    r = session.get(href)
    sendData = []

    # 只爬当天
    items_a = r.html.find('ul.panel-list > li > a')
    for abox in items_a:
        a_url = abox.attrs['href']
        # 创建时间
        creatDate = abox.find('.fa-calendar-check-o', first=True).text
        if route in a_url and creatDate == today:
            if not abox.search('VIP视频'):
                img_url = url + abox.find('img', first=True).attrs['src']
                # print(img_url)
                # 视频详情页
                video_r = session.get(url + a_url)
                # 图片地址
                title = video_r.html.find('div.video-player-hd > h1', first=True)
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
                    'id': a_url[-10:-5],
                    'image': abox.find('img', first=True).attrs['src'],
                    'creatDate': creatDate,
                    'longTime': longTime.text[3:],
                    'title': title.text,
                    'video': video_url
                }
                sendData.append(jsondata)
                print(jsondata)


    if sendData == []:
        print(name+'今天无更新')
    else:
        with io.open('data/'+today + '/'+filename+'.js', 'w', encoding="utf-8") as f:
            json.dump(sendData, f, ensure_ascii=False, sort_keys=True, indent=2)
        print(today, name+'输出成功')
