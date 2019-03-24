# 保持登录状态，面对对象方向写

import requests

class GetMSG:
    def __init__(self):
        self.cookie = {
            'Cookie': '_zap=661a71df-e82f-47df-88df-6cb7bfe0b9d9; d_c0="AFBj_nHjIQ-PTgF80MMxa87XdDmsGpR2rPg=|1552752253"; q_c1=4c48aecd555749bfa1d46fc7763dd6a8|1552752254000|1552752254000; tgw_l7_route=66cb16bc7f45da64562a077714739c11; _xsrf=lBtIfr0dIh0iPzxjLEkztj082Bhlti4a; capsion_ticket="2|1:0|10:1553351587|14:capsion_ticket|44:MjQ3ZTFjMzE4ZGQ4NGY2ZTk0ZGUyNDc3N2MzN2FkNzE=|8ef84dcb39efc96666c34957d3b21392d1e985e52d4c6e563ad09fa05431c0a3"; z_c0="2|1:0|10:1553351590|4:z_c0|92:Mi4xLV9lakF3QUFBQUFBVUdQLWNlTWhEeVlBQUFCZ0FsVk5wcEdEWFFDT1pUOHRGVFQ5TC0zVElpSHNJS1l6dTFMbUVB|10c3c17c05c99fc8b06e5489faf5a3661a155fb4bd70ab14a48b4d245a9f38d6"; tst=r'
        }

        self.header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
        }

    def getMSG(self):
        url = 'https://www.zhihu.com/people/edit'

        response = requests.get(url, headers=self.header, cookies=self.cookie)

        html = response.text

        print(html)

GetMSG().getMSG()





