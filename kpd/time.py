import time

t = time.time()    # 获得时间戳
a = time.localtime(t)  # 获得当地时间的时间元组
b = time.gmtime(t)     # 获得格林威治时间的时间元组
print(t)
print(a)
print(b)
print(time.strftime('%Y-%m-%d %H:%M:%S', a))  # 获得指定格式的等地时间
print(time.strftime('%Y-%m-%d', a))  # 获得指定格式的等地时间
nowdate = time.localtime(time.time())  # 获得当地时间的时间元组
print(time.strftime('%Y-%m-%d', nowdate))  # 获得指定格式的等地时间
