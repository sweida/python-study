# 保持登录状态


import requests
# 存用户名和密码
import config
session = requests.session()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

def login():
    url = 'http://119.29.27.100/apis/login'
    data = {
        'username': config.username,
        'password': config.password
    }
    response = session.post(url, data=data, headers=headers)

    responseData = response.json()
    if responseData['status']==1:
        print('登录成功')
        comment()
    else:
        print('登录失败', '失败原因：', responseData['msg'])


def comment():
    url = 'http://119.29.27.100/apis/message/add'
    data = {
        'content': '我就是来搞事情的',
        'ykname': ''
    }
    response = session.post(url, data=data, headers=headers)

    responseData = response.json()
    if responseData['status'] == 1:
        print('留言成功')
    else:
        print('留言失败', '失败原因：', responseData['msg'])

login()

