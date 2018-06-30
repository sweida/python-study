# # requests
# import requests

# # r = requests.get('https://www.douban.com')
# # # r.status_code
# # # r.text
# # print(r.encoding)
# # # with open('./requests.html', 'w') as g:
# # #     g.write(r.content)


# # r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# # print(r.json())

# r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})




# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

from urllib import request
from urllib import parse
from urllib.request import urlopen

import json
from bs4 import BeautifulSoup


# GET
url = 'http://kaoshi.edu.sina.com.cn/college/scorelist?tab=batch&wl=1&local=2&batch=&syear=2013'

request = request.Request(url)
response = urlopen(request, timeout=20)
# .decode("utf-8")乱码转中文, \xa9 报错
result = response.read().decode("utf-8", "ignore").replace(u'\xa9', u'')

print(result)


# # POST
# url = 'https://shuju.wdzj.com/plat-info-target.html'
# value = {'wdzjPlatId': 59,'type': 1, 'target1': 1, 'target2': 0}
# data = parse.urlencode(value).encode('utf-8')  # 提交类型不能为str，需要为byte类型
# request = request.Request(url, data)
# # opener = request.build_opener(urllib.request.HTTPCookieProcessor)
# response = urlopen(request)
# result = response.read().decode()
# # for key in json.loads(result).keys():
# #     print(key)
# print(result)
