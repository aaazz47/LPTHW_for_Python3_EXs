# 引入库
from sys import argv
from os.path import exists

# 解包参数
script, from_file, to_file = argv

# 打印任务目标
print("Copying from %s to %s" % (from_file, to_file))

# we could do these two on one line too, how?
# 如何把这两行写到一行？
in_put = open(from_file)
indata = in_put.read()

# 打印文件字符长度。
print("The input file is %d bytes long" % len(indata))

# 打印目标文件是否已经存在。
print("Does the output file exist? %r" % exists(to_file))
# 用户决定是否完成复制操作
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# 以写入模式打开目标文件
out_put = open(to_file, 'w')
# 写入复制的内容
out_put.write(indata)

# 打印操作完成（实际打印这段话的时候根本没完成）
print("Alright, all done.")

# 关闭文件（真保存至硬盘）
out_put.close()
in_put.close()
