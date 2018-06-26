# print('hello world')

# height = 1.75
# weight = 80.5
# # height = float(height)
# # weight = float(weight)
# bmi = weight / (height*height)
# print('小明，你的BMI是：%.2f' % bmi)
# if bmi < 18.5:
#     print('小明，你的体重过轻')
# elif 18.5 <= bmi < 25:
#     print('小明，你的体重正常')
# elif 25 <= bmi < 28:
#     print('小明，你的体重过重')
# elif 28 <= bmi < 32:
#     print('小明，你的体重肥胖')
# else:
#     print('小明，你的体重严重肥胖，该减肥了！')

# names = ['ss', 'aa', 'dd']
# for na in names:
#     print(na)

# L = ['Bart', 'Lisa', 'Adam']
# for name in L:
#     print('hello', name+'!')

# # n = 0
# # while n <=20:
# #     n += 1
# #     if n > 10:
# #         break
# #     print(n)
# # print('end')

# n = 0
# while n <=20:
#     n += 1
#     if n % 2 == 0:
#         continue
#     print(n)
# print('end')

# # 数组和对象
# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# c = {'iw': 33, 'we': 44}
# print(d['Bob'])
# print('Bob' in d)
# print(d.get('Bob'))
# print(d)
# d.pop('Bob')
# print(d)
# e = {1, 2, 3}
# d['ss'] = 5
# print(d)
# d.update(asdf=33, sdfff=54)
# d.update({'tom':333, 'honer':54})
# d.update(c)
# print(d)
# print(d['we'])

# # 定义函数
# def funt(x):
#     if x >= 0:
#         return x
#     else:
#         return -x
# print(funt(-4))

# def power(x, n=2):
#     s=1
#     while n>0:
#         n-=1
#         s=s*x
#     return s
# print(power(6,3))

# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L
# print(add_end())
# print(add_end())

# a = {'k1': 2, 'k2': 3, 'k3': 4}

# for key, value in a.items():
#     print (key, value)

# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print(L[0:3])
# K = list(range(10))
# print(K)

# try:
#     f = open('./text.txt', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

# 和上面相等 with自带close
# with open('./text.txt', 'r') as f:
#     print(f.read())

# with open('./text.txt', 'w') as f:
#     f.write('hahaha!')


# import os
# os.rename('text.py', 'text.txt')

# # 时间格式化，时间加减
# from datetime import datetime, timedelta
# now = datetime.now()
# print(now.timestamp())
# nows = now + timedelta(days=3, hours=10)
# print(nows.strftime('%Y-%m-%d %H:%M:%S'))

# deque list的插入和删除
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('yy')
print(q)















