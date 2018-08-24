# coding=utf-8
import os
import json
import importlib
import sys
importlib.reload(sys)
listData = [
    {'id': '10531',
     'url': 'https://www.44kpd.com/d/file/whmm/2018-08-24/08542a6ae6dc07e35cab0672b7fc90a4.jpg',

        'title': '全球首发熊猫TV美娜酱BABY露点下海直播1'},
    {'id': '10536',
     'url': 'https://www.44kpd.com/d/file/whmm/2018-08-24/b3442d7826adacefa5aa7b5dc65519bd.jpg',

        'title': '斗鱼女主播谭晓彤elise小兔子視頻合集1'},
    {'id': '10510',
     'url': 'https://www.44kpd.com/d/file/whmm/2018-08-24/7ad98cd6f522db36e072014ded8139fe.jpg',

        'title': '门票挺贵的明星脸蛋美女穿着性感女仆丝袜和帅哥露脸啪啪'},
    {'id': '10507',
     'url': 'https://www.44kpd.com/d/file/whmm/2018-08-24/b16b5320cc991d65e0f6ee4c90c5cc0a.jpg',

        'title': '小狸姑娘没有改变的小网红3'},
    {'id': '10512',
     'url': 'https://www.44kpd.com/d/file/whmm/2018-08-24/2e51ca6d2830010457e983b1399ce10b.jpg',

        'title': 'HanMei小姐姐解锁新姿势'},
    {'id': '10479',
     'url': 'https://www.44kpd.com/d/file/whmm/2018-08-23/1e2e5478ceadad3d369e44e987f484b2.jpg',

        'title': 'UT明星脸蛋气质美女笑醉红颜大尺度走私自慰呻吟给力'},
    {'id': '10476',
     'url': 'https://www.44kpd.com/d/file/whmm/2018-08-23/bcf179c2e2509613d667da2a3c593940.jpg',

        'title': '皮肤白皙逼逼粉嫩超漂亮美女主播红衣诱惑全裸漏逼秀不要错过'},
    {'id': '10495',
     'url': 'https://www.44kpd.com/d/file/whmm/2018-08-23/e5e4da6395916f2d63ee05380c55a131.jpg',
     'title': 'HanMei的幸福生活'},
    {'id': '10494',
     'url': 'https://www.44kpd.comhttps://play.cdmbo.com/20180822/bmKSAUqM/1.jpg',

        'title': '小狸姑娘没有改变的小网红2'},
    {'id': '10450',
     'url': 'https://www.44kpd.com/d/file/whmm/2018-08-22/fe5b22ecf28d89e1e17c28a37651c1e5.jpg',

        'title': '杜蕾斯王中王和HanMei的故事'},
    {'id': '10449',
     'url': 'https://www.44kpd.com/d/file/whmm/2018-08-22/a72f0d4a4594bcf16f70f95b5b8c5be3.jpg',

        'title': '重磅福利最新购买最近抖音很火的淫钰儿唯一一部露脸剧情视频老师裸体上课在教室自慰'},
    {'id': '10428',
     'url': 'https://www.44kpd.com/d/file/whmm/2018-08-21/2484ec3ac9913a54b7e9d1ef6149418a.jpg',

        'title': '抖音和网上最火的小视频合集 精彩不容错过'},
    {'id': '10408',
     'url': 'https://www.44kpd.com/d/file/whmm/2018-08-21/8d6a955cd58c286a143e942966f657c7.jpg',
     'title': '姐给你留灯HanMei'},
    {'id': '10404',
     'url': 'https://www.44kpd.com/d/file/whmm/2018-08-21/2e5f1ca2291d9b3e10b8996d22003b17.jpg',

        'title': '小狸姑娘没有改变的小网红1'},
    {'id': '10427',
     'url': 'https://www.44kpd.com/d/file/whmm/2018-08-21/54eb9eb09c34fca7911eb5e26738bc2e.jpg',

        'title': '抖音黑森林事件原版视频完整版'},
    {'id': '10403',
     'url': 'https://www.44kpd.com/d/file/whmm/2018-08-21/8c11177f58afdc23bc7addc0e7b5603b.jpg',
     'title': 'FC2高颜值萌妹春丽沙发上扣逼自慰'},
    {'id': '10405',
     'url': 'https://www.44kpd.com/d/file/whmm/2018-08-21/b9f5e5dba05862f6c5d06e441261da29.jpg',

        'title': '无毛骚穴萝莉各种东西往逼逼里饮料瓶底部拳 茄 香蕉最后换一个妹子坐插自慰棒_'},
    {'id': '10406',
     'url': 'https://www.44kpd.com/d/file/whmm/2018-08-21/a8735b40b0d45188d77d173c1956c8c3.jpg',

        'title': '绝色花多多811露脸一多情趣连体黑丝极品诱惑'},
    {'id': '10365',
     'url': 'https://www.44kpd.com/d/file/whmm/2018-08-20/0aab15c47d8bbbdbb49656ea4d41a458.jpg',

        'title': '最火抖音门事件第七季 有亮点哦'},
    {'id': '10368',
     'url': 'https://www.44kpd.com/d/file/whmm/2018-08-20/5ca148ba61ada12cf4808e4281c53ee2.jpg',

        'title': '抖音黑森林事件女主第七季 You dirve me'},
    {'id': '10366',
     'url': 'https://www.44kpd.com/d/file/whmm/2018-08-20/61bbb3d4070d6cceaa9dd6ab467c048e.jpg',

        'title': '漂亮萌妹子身材苗条全裸跳蛋自摸秀喜欢不要错过'},
    {'id': '10396',
     'url': 'https://www.44kpd.com/d/file/whmm/2018-08-20/35d064150efa8f3653b8155cfeb789a5.jpg',

        'title': '手机直播双人啪啪秀黑丝骚女口交后入大屁股金手指玩BB喜欢不要错过_1'},
    {'id': '10359',
     'url': 'https://www.44kpd.com/d/file/whmm/2018-08-19/032a7853f4b06d084aff180b4519ba9a.jpg',

        'title': '最火抖音门事件第六季 有亮点哦'},
    {'id': '10330',
     'url': 'https://www.44kpd.com/d/file/whmm/2018-08-19/5a3500fecfa85213fbf3c5eb70b14063.jpg',
     'title': '话教的小姐姐小乔'},
]

with open('./whmm.js', 'w') as f:
    json.dump(listData, f, ensure_ascii=False, sort_keys=True, indent=4)
    # json.dump(bb, f, ensure_ascii=False, indent=4)
    # json.dump(listData, f)
    print('输入成功')
# with open('./test.txt', 'w') as f:
#     f.write('Hello, world!')
