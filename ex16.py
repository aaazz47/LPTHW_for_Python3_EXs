from sys import argv

# 通过解包 argv 获取 脚本名 和将要保存的 文件名
script, filename = argv

# 询问是否继续编辑文件 filename
print("We're going to erase %r" % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
# 等待用户输入是否继续编辑
input("?")

# 如果用户未输入 ctrl-c 则会继续执行
print("Opening the file...")
# 打开文件对象
target = open(filename, 'w')

# 没有指定 truncate() 的大小，所有实际上删除了文件的内容
print("Truncating the file. Goodbye!")
target.truncate()

# 获取三个 input 变量的内容
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# 将内容写入文件（只在内存中，并未写入硬盘）
print("I'm going to write there to the file.")
# 太罗嗦了 16.3 题优化掉
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
nl = '\n'
target.write(line1 + nl + line2 + nl + line3 + nl )

# 关闭文件，将文件写入硬盘
print("And finally, we close it.")
target.close()
