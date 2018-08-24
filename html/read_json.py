import os
import json


# 读取json
with open('./whmm.js', 'r') as f:
    load_dict = json.load(f)
    print(load_dict)
