# 保持登录状态

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

#浏览器登录后得到的cookie，也就是刚才复制的字符串
cookie_str = r'_myFavMv=%5B%5D; td_cookie=3034830472; laravel_session=eyJpdiI6Ik4wSjFSUU1wcFo1SndYRFliNWZZeXc9PSIsInZhbHVlIjoiMHJWZzM1WmpGRXp6NWVLYk9OaUdHOVVzcWRNK25lQ21lMFhIcmk4eUxKcEFMSnhwSDBMbTFyM3duUllqT3IycGRIc3V2TGhzWEdWaytWRkpzT3hNelE9PSIsIm1hYyI6ImNiMjRhMGFiYTIxYWJhMjUwZDJlNGI2ODgzY2ZiYzY4ZGY4NzI0MDQ4OGZkN2RiNGIwZGM2M2I2YmExYmY3OGIifQ%3D%3D'

#把cookie字符串处理成字典，以便接下来使用
cookies = {}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value


def comment():
    url = 'http://119.29.27.100/apis/message/add'
    data = {
        'content': '再试一条cookie请求',
        'ykname': ''
    }
    response = requests.post(url, data=data, headers=headers, cookies=cookies)

    responseData = response.json()

    if responseData['status'] == 1:
        print('留言成功')
    else:
        print('留言失败', '失败原因：', responseData['msg'])


comment()

