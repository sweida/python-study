from requests_html import HTMLSession
session = HTMLSession()
import os

# GET请求
url = "https://www.sweida.me"

# if not os.path.exists('html'):
#     os.mkdir('html')

r = session.get(url)
r.encoding='utf-8'  # 解决中文乱码问题
# print(r.text)
# 获取的网页的内容存储到本地
with open('test.html','wb') as f:
    f.write(r.content)
