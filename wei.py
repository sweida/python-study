#coding: utf-8

# date: 2015年9月29日01:50:37

# usage: edit steps and ledongli's uid(u need to download this app) .That would be ok .Good luck. ^_^

import requests

import sys

import json

import datetime

import time

import random


def isnum(value):
    try:
        temp = int(value)
    except Exception:
        return False
    else:
        return True

# like 2015-09-25 00:00:00 converts to unix time stamp


def formatDate():
    nowtime = datetime.datetime.now()
    date = time.strftime('%Y-%m-%d')
    strtemp_date = date + ' 00:00:00'
    ledongli_date = time.strptime(strtemp_date, '%Y-%m-%d %H:%M:%S')
    # rusult is 1443456000.0(float type), but still need to format to 1443456000
    finaldate = time.mktime(ledongli_date)
    finaldate = int(finaldate)
    return finaldate

def main(steps, uid):
    if not isnum(steps):
        print('param error. steps must be an integer.')
        exit()
    url = 'http://pl.api.ledongli.cn/xq/io.ashx'
    fake_headers = {
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.0.2; MI 2 MIUI/5.7.16)',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'Accept-Encoding': 'gzip'
    }

    keycontentjson = [
        {
            "date": formatDate(),
            "calories": 0,
            "activeValue": 108,
            "steps": steps,
            "pm2d5": 0,
            "duration": 0,
            "distance": 0,
            "report": "[]"
        }
    ]
    # key is a str type

    # key must be a json data convert to string

    key = json.dumps(keycontentjson)
    param = {
        'action': 'profile',
        'pc':     'uuide516b221b52b017bc48069e186c1763b3722a428',
        'cmd':    'updatedaily',
        'uid':    uid,
        'list':   key
    }

    r = requests.post(url, data=param, headers=fake_headers)
    return json.loads(r.text)["status"]

if __name__ == '__main__':
    print("Powered By 真红酱\n")
    uid = input("请输入乐动力ID-82340962--->")
    steps = input("请输入步数--->")
    while main(steps, uid) != "OK":
        pass
    print("设置完毕:"+str(steps))
