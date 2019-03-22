# 保持登录状态
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}


cookie_str = r'__yadk_uid=tBxePnDGBbT0UFU0kAXgyQHAjFS9SjRM; read_mode=day; default_font=font2; locale=zh-CN; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1552997207,1553001678,1553150380,1553221907; signin_redirect=https%3A%2F%2Fwww.jianshu.com%2Fu%2F485658a54869; remember_user_token=W1sxNjk1NjIyNl0sIiQyYSQxMSRWcG95M1hmRG8uZVJCeFovU0hNaU5lIiwiMTU1MzI0OTU2NC44NjM4NDk0Il0%3D--6d9a8b68cb435820370b2e70ae67cfc7e86cc782; _m7e_session_core=7b09221deb5c295f90a463221b2c5e22; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216956226%22%2C%22%24device_id%22%3A%22164cf82a78560f-089dd3166320dd-5b193413-1049088-164cf82a786687%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22oschina-app%22%2C%22%24latest_utm_medium%22%3A%22pc_all_hots%22%2C%22%24latest_utm_campaign%22%3A%22maleskine%22%2C%22%24latest_utm_content%22%3A%22note%22%7D%2C%22first_id%22%3A%22164cf82a78560f-089dd3166320dd-5b193413-1049088-164cf82a786687%22%7D; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1553249585'


#把cookie字符串处理成字典，以便接下来使用
cookies = {}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value

def comment():
    url = 'https://www.jianshu.com/notes/41925104/comments'
    data = {
        'content': '我就是来搞事情的',
        'parent_id': ''
    }
    response = requests.post(url, data=data, headers=headers, cookies=cookies)

    responseData = response.text
    print(responseData)
    # if responseData['status'] == 1:
    #     print('留言成功')
    # else:
    #     print('留言失败', '失败原因：', responseData['msg'])


comment()

