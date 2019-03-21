# 文档地址：https://cloud.baidu.com/doc/OCR/OCR-Python-SDK.html#.E6.96.B0.E5.BB.BAAipOcr

# 验证码识别
# 先安装
# pip install baidu-aip

from aip import AipOcr


APP_ID = '15810878'
API_KEY = 'Dpe3UTmkf1LyFUCm5N60yDOj'
SECRET_KEY = 'VQouvu1zsHGQVlEaitf12rNca279vdce'


client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file_content('C:/Users/Administrator/Desktop/code.png')

result = client.basicGeneral(image)

options = {
    # 定义的图片方向
    'detect_direction': 'true',
    #识别的语言类型 默认是中英文混合
    'language_type': 'CHN_ENG',
    # 带参数调用通用文字识别（高精度版）
    'probability': 'true'

}

# 普通文字识别
# results = client.basicGeneral(image, options)

# """ 带参数调用通用文字识别（高精度版） """
results = client.basicAccurate(image, options)

print(results)





