from sys import argv

script, from_file, to_file = argv

# 一行读取源文件
indata = open(from_file).read()
# 一行写入
open(to_file, 'w').write(indata)

print("拷贝完成，共复制 %d 个字" % len(indata))



# 极限
from sys import argv
script, from_file, to_file = argv
open(to_file, 'w').write(open(from_file).read())
