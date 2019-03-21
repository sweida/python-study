# coding：utf-8
# 数据储存MySQL
import pymysql
import json
import requests

conn = pymysql.connect(host='localhost', port=3307, user='root',
                       password='usbw', db='toutiao', charset='utf8')
cursor = conn.cursor()

url = 'http://www.toutiao.com/api/pc/focus/'
wbdata = requests.get(url).text

data = json.loads(wbdata)
news = data['data']['pc_feed_focus']
for n in news:
    title = n['title']
    img_url = n['image_url']
    url = n['media_url']
    print(url, title, img_url)
    cursor.execute("INSERT INTO data(title,img_url,url)VALUES('{0}','{1}','{2}');".format(
        title, img_url, url))
    conn.commit()

cursor.close()
conn.close()
