import os
import requests
from requests_html import HTMLSession


# https://log.mmstat.com/member.2.1.2?ok = 1
# https://log.mmstat.com/member.2.1.4
# 保持登录状态

session = HTMLSession()

headers = {
    'Host': 'login.taobao.com',
    'Referer': 'https://login.taobao.com/member/login.jhtml',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Connection': 'Keep-Alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}


def slideCode():
    requests.get('https://log.mmstat.com/member.2.1.2?ok=1')
    requests.get('https://log.mmstat.com/member.2.1.4')

def login():
    slideCode()

    url = 'https://login.taobao.com/member/login.jhtml'
    data = {
        'TPL_username': '13798661922',
        'TPL_password': '',
        'ncoSig': '',
        'ncoSessionid': '',
        'ncoToken': '485fb26dd8baf198e615410ed7d6aaece738b4e9',
        'slideCodeShow': 'false',
        'useMobile': 'false',
        'lang': 'zh_CN',
        'loginsite': 0,
        'newlogin': 0,
        'TPL_redirect_url': 'https://www.taobao.com/',
        'from': 'tb',
        'fc': 'default',
        'style': 'default',
        'css_style': '',
        'keyLogin': 'false',
        'qrLogin': 'true',
        'newMini': 'false',
        'newMini2': 'false',
        'tid': '',
        'loginType': 3,
        'minititle': '',
        'minipara': '',
        'pstrong': '',
        'sign': '',
        'need_sign': '',
        'isIgnore': '',
        'full_redirect': '',
        'sub_jump': '',
        'popid': '',
        'callback': '',
        'guf': '',
        'not_duplite_str': '',
        'need_user_id': '',
        'poy': '',
        'gvfdcname': 10,
        'gvfdcre': '68747470733A2F2F6C6F67696E2E74616F62616F2E636F6D2F6D656D6265722F6C6F676F75742E6A68746D6C3F73706D3D613231626F2E323031372E3735343839343433372E372E35616639313164393458446C4E6126663D746F70266F75743D7472756526726564697265637455524C3D68747470732533412532462532467777772E74616F62616F2E636F6D253246',
        'from_encoding': '',
        'sub': '',
        'TPL_password_2': '61c1a33f828495562ce1fff06f52bd114cba1af8b5a97273691ffad2ae69ea4586aa442d64169bc75d2de3335cce097ed3b6ccca1831ef936b3b03f936c9d75cf96bc6d61616441374831869e8148d6c679e9dbbd13b14a28be2f80c07d220e19712d69c16cb3a330fbb4414c2344ac5ff5b8d8008e6096ccdd4c3e83d24ae07',
        'loginASR': 1,
        'loginASRSuc': 1,
        'allp': '',
        'oslanguage': 'zh-CN',
        'sr': 1600*900,
        'osVer': 'windows|6.1',
        'naviVer': 'chrome|72.03626121',
        'osACN': 'Mozilla',
        'osAV': '5.0 (Windows NT 6.1 Win64 x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'osPF': 'Win32',
        'miserHardInfo': '',
        'appkey': 00000000,
        'nickLoginLink': '',
        'mobileLoginLink': 'https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/&useMobile=true',
        'showAssistantLink': '',
        'um_token': 'HV02PAAZ0b0b1973ca6929c45c93553c0019daba999999',
        'ua': '115#1VSsZf1O1TNX+3qhT1iE1CsoE51NBJA11g2mOdXN01CcAlk1LRPi1C6VG3/81TAHfsiWCUU4BMNca0X2wE/JGSfyeKT8z8CHi9k+haF19HNVaLBXuzEQ9I5lrkYX/MNQi/W5Hrz4OkdDGkGEOZPQAylPetT8zkNQi/JRY4U4AWNcaLpXr4EQASAyF+v/CEm5rjcdTs1cB5QDhpaMSB76FVEXq2H5MJCQ37/CZh8dP3eWjW4qSujj3dJ//EtK4ZdgNtFVfu3rgJpxIPqxinMKX+1HZt+sWY0Yh3uNdMX1r1aVl14Qpm441IWZyDEIHugGIDm53jMNQ9wJsJHYCFS5/QeYK8woonvHyh110wm7HoOIzA2jsGNI9IwhwFCsWwRAuxHaCKV2rvg1ET4XhMIF/f7RqNX/j6ZnX+kx0evnnVa+ZFuvPBc1CQUx6ronaCQ3b/NuK/lY5UWmNJMOudl3tNM7DZu5D2QS8t4jFbVywqT5diu42bkQbYrxPvrtzM//ZAdgJqoSob9ojvICQLn4KnrgBJVlY6S5yo6OZJ3KaoH8ZY5RKC5f0nybvpoINJHGXcLoC2JiBfbnceVeyDa/ijb8uYz1/v595pXgeVLUjVOManvZD6hRTsOVR2Bm2923USlmYEGfG4OQI+s8MkS2fYewU6AS9dWQgL1/h/DFx9dLAs4ZPUSN+BirTq0+5iGzLoKLI+X4Npn+zvtO2DfN43uuvANHxcRn+t7ZnEFzg/+a0A+kmbR0M23wNXGQQ5eM9wT6uMpy/redTXGjtdbRjjK0WD3Xe9lTrsdFiKpeJnqZDWoQdKpccw6Xjsn/42lQ/104MNPV0i8xkRAiDeWvkw4Uuh0d4Bt4oxOUe+dsAVMAgokm0mgROdPv1XBLR7569wm5MrvQMoawLxV53dCixi/UhhxpWhaEt0HyFZI6soYKbdc05pDL/puIa2FZovVoFK7M50UUjoc='
    }
    response = session.post(url, data=data, headers=headers)

    responseData = response.text
    print(responseData)
    # index()



def index():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    url = 'https://buyertrade.taobao.com/trade/itemlist/list_bought_items.htm'
    response = session.get(url, headers=headers)
    responseData = response.text
    print('首页', responseData)
    


# slideCode()
login()
