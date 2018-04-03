# 载入 sys.argv 模块，以获取脚本运行参数。
from sys import argv

# 将 argv 解包，并将脚本名赋值给变量 script ；将参数赋值给变量 filename 。
script, filename = argv

# 将名为 “filename” 的文件打开，并将打开的内容赋值给变量 txt
txt = open(filename)

# 打印文件名，并在读取文件内容后打印
print("Here's youer file %r:" % filename)
print(txt.read())

# ------------上面是通过 argv 获取文件名--------

# 以 input 方式让用户在脚本运行后输入文件名 
print("Type the filename again:")
file_again = input("> ")

# 打开用户输入的文件
txt_again = open(file_again)

# 读取后打印用户输入文件的内容
print(txt_again.read())

# 关闭文件
txt.close()
txt_again.close()
