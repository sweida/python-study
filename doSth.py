#coding:utf8
# python 每天如何定时启动爬虫任务

import datetime
import time
 
def doSth():
    # 把爬虫程序放在这个类里
    print(u'这个程序要开始疯狂的运转啦')
 
# 一般网站都是1:00点更新数据，所以每天凌晨一点启动
def main(h=1,m=0):
    while True:
        now = datetime.datetime.now()
        # print(now.hour, now.minute)
        if now.hour == h and now.minute == m:
            break
        # 每隔60秒检测一次
        time.sleep(60)
    doSth()
 
main()
