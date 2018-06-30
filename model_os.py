# OS模块简单的来说它是一个Python的系统编程的操作模块，可以处理文件和目录这些我们日常手动需要做的操作。
import os

# 获取当前路径
print(os.getcwd())

# 列出目录下的所有文件
print(os.listdir())
print(os.listdir('flask_blog'))

# # 删除文件
# os.remove('text2.txt')
print(os.path.exists('aaa'))

# # 创建目录
# os.mkdir('text3.txt')

# # 删除目录
# os.rmdir('haha')

# 重命名
# os.rename('text3.txt', 'text2.txt')