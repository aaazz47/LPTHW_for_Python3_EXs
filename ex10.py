tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

# 单引号和双引号是一样的。
fat_cat = ("""
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
""")

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


# 转义字符演示
# r''是原始字符串，和 %r 有点像——保持原始数据不会转义字符
print(r"\n 【换行】演示：", "\n第一行\n第二行")
print("-" * 20)
print(r"\\ 【反斜杠】演示：", "\n一个反斜杠：\\")
print("-" * 20)
print(r"\' 和 \" 【引号】演示：", "\n英文双引号：\", 英文单引号：\'")
print("-" * 20)
print(r"行末\ 【不换行】演示：", "\n我不想\
换行")
print("-" * 20)
print(r"\t 【制表符】演示：", "\n\t横向制表符")
print("-" * 20)
print(r"\v 【纵向制表符】演示：", "\n\v纵向制表符")
print("-" * 20)
print(r"\a 【响铃】演示：", "\n打开音响哦\a")
print("-" * 20)
print(r"\b 【退格】演示：", "\n退格键\b（后面要有东西才行）")
print("-" * 20)
print(r"\000 【空】演示：", "\n--\000--", ' ' == '\000')    # 和空格不相等 False
print("-" * 20)
print(r"\r 【回车】演示：", "\naaa\r6666\r2333")
print("-" * 20)
print(r"\f 【翻页】演示：", "\n翻页\f翻页后")
print("-" * 20)
print(r"\ooo 【八进字符】演示：", "\n\044")
print("-" * 20)
print(r"\xhh 【十六进字符】演示：", "\n\x44")

# 转义字符 + 格式化字符
print("简单换个行%s" % "\n")
print("这次不换行%s" % "\\n")
