import os
import time

# 获取今天年月日
nowdate = time.localtime(time.time())  # 获得指定格式的等地时间
today = time.strftime('%Y-%m-%d', nowdate)  # 获得指定格式的等地时间
# 新建今天的文件夹
os.mkdir('data/'+today)

os.system("python ./video_whmm.py")
os.system("python ./video_guoc.py")
os.system("python ./video_fuli.py")
os.system("python ./video_91porn.py")
os.system("python ./video_hanguo.py")
os.system("python ./video_nenmo.py")
os.system("python ./video_siwa.py")
os.system("python ./video_piaoke.py")
os.system("python ./video_sanjipian.py")
os.system("python ./video_zongyi.py")

