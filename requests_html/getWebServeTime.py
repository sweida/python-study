import http.client
import time


def get_webservertime(host):
    conn = http.client.HTTPConnection(host)
    conn.request("GET", "/")
    r = conn.getresponse()
    #r.getheaders() #获取所有的http头
    ts = r.getheader('date')  # 获取http头date部分
    print(ts)

    # #将GMT时间转换成北京时间
    ltime = time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
    # 时间转时间戳，修改时差
    timestamp = time.mktime(ltime) + 8*60*60
    print('服务器时间戳', timestamp)
    # 时间戳转时间
    ttime = time.localtime(timestamp)
    dat = "%u-%02u-%02u %02u:%02u:%02u" % (ttime.tm_year, ttime.tm_mon,
                                           ttime.tm_mday, ttime.tm_hour, ttime.tm_min, ttime.tm_sec)
    print('服务器时间：', dat)
    return timestamp


TargetTime = '2019-03-27 22:53:00'
timeArray2 = time.strptime(TargetTime, "%Y-%m-%d %H:%M:%S")
TargetTimeTamp = time.mktime(timeArray2)

print('目标时间：', TargetTime)
print('目标时间戳：', TargetTimeTamp)



while get_webservertime('www.baidu.com') < TargetTimeTamp:
    get_webservertime('www.baidu.com')
else:
    print('时间到了')
