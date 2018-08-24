from requests_html import HTMLSession
import requests
import os
session = HTMLSession()
import json
import re

# 截取字符串
url = 'https://www.44kpd.com/e/DownSys/play/?classid=5&id=10315&pathid=0'
# text = "var video=['https://play.cdmbo.com/20180817/YWxT62BY/index.m3u8'];"
r = session.get(url)

# print(r.text)
url = re.findall(r'https.*?\]', r.text)
print(url[0][0: -2])
