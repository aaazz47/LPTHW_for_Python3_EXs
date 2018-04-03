# 要求用 argv 方式，所有相见载入
from sys import argv

# 解包
script, filename = argv

print("脚本 %r 正在读取文件: %r ..." % (script, filename))

# 打开文件
file_open = open(filename)
# 用 print 打印出读取到的内容
print(file_open.read())
