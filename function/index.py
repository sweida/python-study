import os
import time
from common import getDatalist

# 获取今天年月日
nowdate = time.localtime(time.time())  # 获得指定格式的等地时间
today = time.strftime('%Y-%m-%d', nowdate)  # 获得指定格式的等地时间

# 新建今天的文件夹
if not os.path.exists('data/'+today):
    os.mkdir('data/'+today)
print(today)

url = 'https://www.45kpd.com'

getDatalist(today, url, '/whmm', 'whmm', '网红主播')
getDatalist(today, url, '/gcjp/91porn', '91porn', '91大神')
getDatalist(today, url, '/fuli/pr', 'weipai', '微拍福利')
getDatalist(today, url, '/guochan', 'guochan', '国产精品')
getDatalist(today, url, '/meinvzhubo/kr', 'hanguo', '韩国主播')
getDatalist(today, url, '/fuli/nmxz', 'nenmo', '嫩模写真')
getDatalist(today, url, '/fuli/riji', 'piaoke', '嫖客日记')
getDatalist(today, url, '/sanjipian', 'sanjipian', '三级片')
getDatalist(today, url, '/gcjp/siwa', 'siwa', '丝袜诱惑')
getDatalist(today, url, '/zongyi', 'zongyi', '两性综艺')



