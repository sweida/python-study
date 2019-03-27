# 保持登录状态，面对对象方向写
# 获取个人信息api

import requests


class GetMSG:
    def __init__(self):

        self.cookie_str = r'_zap=661a71df-e82f-47df-88df-6cb7bfe0b9d9; d_c0="AFBj_nHjIQ-PTgF80MMxa87XdDmsGpR2rPg=|1552752253"; q_c1=4c48aecd555749bfa1d46fc7763dd6a8|1552752254000|1552752254000; _xsrf=lBtIfr0dIh0iPzxjLEkztj082Bhlti4a; capsion_ticket="2|1:0|10:1553351587|14:capsion_ticket|44:MjQ3ZTFjMzE4ZGQ4NGY2ZTk0ZGUyNDc3N2MzN2FkNzE=|8ef84dcb39efc96666c34957d3b21392d1e985e52d4c6e563ad09fa05431c0a3"; z_c0="2|1:0|10:1553351590|4:z_c0|92:Mi4xLV9lakF3QUFBQUFBVUdQLWNlTWhEeVlBQUFCZ0FsVk5wcEdEWFFDT1pUOHRGVFQ5TC0zVElpSHNJS1l6dTFMbUVB|10c3c17c05c99fc8b06e5489faf5a3661a155fb4bd70ab14a48b4d245a9f38d6"; tst=r; __utma=51854390.459575028.1553432648.1553432648.1553432648.1; __utmc=51854390; __utmz=51854390.1553432648.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100--|2=registration_date=20161101=1^3=entry_date=20161101=1; tgw_l7_route=f2979fdd289e2265b2f12e4f4a478330'

        self.cookies = {}
        for line in self.cookie_str.split(';'):
            key, value = line.split('=', 1)
            self.cookies[key] = value

        self.header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
        }

    def getMSG(self):
        url = 'https://www.zhihu.com/api/v4/me?include=description%2Clocations%2Cemployments%2Ceducations%2Cbusiness%2Ccover_url%2Cverify_apply%2Ccan_rename'

        response = requests.get(url, headers=self.header, cookies=self.cookies)

        html = response.json()

        print(html)


GetMSG().getMSG()
