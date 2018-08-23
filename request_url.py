from requests_html import HTMLSession
import requests
import os
session = HTMLSession()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# #打开浏览器
# driver = webdriver.Chrome()
# #最大化浏览器
# driver.maximize_window()

# 无窗口访问
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver', chrome_options=chrome_options)

print(333)

# url = "https://www.44kpd.com/whmm/"
# r = session.get(url)

# items_a = r.html.find('ul.panel-list > li > a')
# for abox in items_a:
#     a_url = abox.attrs['href']
#     if '/whmm' in a_url:
#         r = session.get('https://www.44kpd.com' + a_url)
#         title = r.html.find('div.video-player-hd > h1', first=True)

#         ifarmBox = r.html.find('#pf', first=True)
#         ifarm_url = 'https://www.44kpd.com' + ifarmBox.attrs['src']
#         #打开页面
#         driver.get('https://www.44kpd.com' + a_url)
#         #通过contains函数，提取匹配特定文本的所有元素
#         iframe = driver.find_element_by_tag_name('iframe')[0]
#         driver.switch_to.frame(iframe)
#         ifhtml = driver.page_source
#         # video = session.get(ifarm_url)
#         # video_box = video.html.find('video', first=True)
#         # video_url = video_box.attrs['src']
#         print(title.text, ifhtml)




# 单个页面iframe
# url = 'https://www.44kpd.com/whmm/201808/10315.html'
url = 'https://login.1688.com/member/signin.htm'
# url = 'https://music.163.com/#/artist/album?id=101988&limit=120&offset=0'
driver.get(url)
iframe = driver.find_elements_by_tag_name('iframe')[0]
driver.switch_to.frame(iframe)
ifhtml = driver.page_source
print(ifhtml)
# video_src = ifhtml.html.find('video').sttrs['src']
# print(video_src)





# url = 'https://www.44kpd.com/e/DownSys/play/?classid=5&id=10315&pathid=0'
# r = session.get(url)

# main = r.html.find('video')
# # vsrc = main.attrs['src']
# vsrc = r.text.flashvars
# print(vsrc)



