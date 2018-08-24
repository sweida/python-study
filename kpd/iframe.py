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

# 单个页面iframe
url = 'https://www.44kpd.com/whmm/201808/10315.html'
driver.get(url)
iframe = driver.find_elements_by_tag_name('iframe')[0]
driver.switch_to.frame(iframe)
ifhtml = driver.page_source
print(ifhtml)

driver.quit()



