# 本练习通过脚本的参数获取被打印的文件名
# 因此需要 argv 获取脚本参数。
from sys import argv

# 第一个函数，打印整个文档。
def print_all(f):
    print(f.read())

# 第二个函数，用来重置指针（相当于光标）到文件开头的位置
def rewind(f):
    f.seek(0)

# 函数：打印一个数字代表行号后，打印打印一行文件
def print_a_line(line_count, f):
    print(line_count, f.readline())

# 运用以上函数把脚本参数中的文件打印一遍。

# 获取脚本参数
script, input_file = argv

# 从函数可以看出其中对参数 f 使用的方法都是
# Py2 的 file 对象（在15题中得知在 Py3中是 TextIOWrapper）
# 它们都是被 open 后才出现的，所有我们需要打开文件已被被函数调用
current_file = open(input_file)

# 首先打印全文
print("First let's print the whole file:\n")
print_all(current_file)

# 打印全文之后指针已经移动到了文档的末尾，想要做其他打印需要复位一下。
# Zed 比喻这个过程像倒带一样
print("Now let's rewind, kind of like a tape.")
rewind(current_file)

# 然后指针已经回到起始位置了（0的位置）
# 逐行打印
print("Let's print three lines:")
# 设置一个代表航好的变量，打印第一行
current_line = 1
print_a_line(current_line, current_file)

# 变更行号，打印第二行（这里设置行号并不会改变
# f.readline 的行，这个被打印的行号只是给人看的，写100 也行
# 打印过一行之后，指针其实已经在第二行开头等着了）
current_line = current_line + 1
print_a_line(current_line, current_file)

# 重复上一步在打印一行
current_line = current_line + 1
print_a_line(current_line, current_file)


###############################
print("=" * 20 + "一下是加分练习的打印" + "=" * 20 + "\n")

def print_a_line(line_count, f):
    print(line_count, f.readline())

# 对调函数调用时的参数
current_line = 1
print_a_line(current_file, current_line)
