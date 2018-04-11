def print_type(x):
    print("    正在测试的数据 %r 是 %s 类型的数据" % (x, type(x)))


# 数字(Number)类型的数据
print("测试数字类型的数据：")
print_type(2333)
print_type(666.6)
print_type(True)
print_type(1 != 1)
print_type(3+4j)

# 字符串 str 类型的数据
print("\n\n测试字符串类型的数据：")
print_type("""三引号字符串""")
print_type("双引号字符串")
print_type('单引号字符串')
print_type(r'原始字符串')


# 列表 list 类型的数据
print("\n\n测试列表类型的数据")
print_type([1,2,'s'])
print_type(list(range(1,5)))


# 元组 tuple 数据类型
print("\n\n测试元组数据类型")
print_type((1,))
print_type(("s"))
print_type(tuple())


# 字典 dict 数据类型
print("\n\n测试字典数据类型")
t = {'a' : 1, 'b' : 2, 'c' : 'c'}
print_type(t)
print_type(dict())
print_type(t['c'])


# 集合 set 数据类型
print("\n\n测试集合数据类型")
set_a = {1,2,'a','b'}
set_b = set()
for i in range(6):
    set_b.add(i)

print_type(set_a)
print_type(set_b)
print_type(set_a | set_b)
print_type(set_a & set_b)
print_type(set_b - set_a)
print_type(set_a ^ set_b)


# 空值 None 数据类型
print("\n\n测试 None 数据类型")
print_type(None)
