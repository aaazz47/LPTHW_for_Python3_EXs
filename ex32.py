# 定义列表
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']    # 列表内可以放入不同类型的数据

# this first kind of for-loop goes through a list
# 首选 for 循环一个列表
for number in the_count:
    print("This is count %d" % number)

# same as above 和上面一样
for fruit in fruits:
    print("A fruit of type: %s" % fruit)

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
# 对于混合列表我们需要注意使用 %r 因为其中可能有各种不同类别的东西
for i in change:
    print("I got %r" % i)

# we can also build lists, first start with an empty one
# 演示如何创建一个空列表
elements = []
# 另一种方法
elements = list()

# then use the range function to do 0 to 5 counts
# 使用函数 range 创建一个包含整数 0 到 5 的列表
for i in range(0, 6):
    print("Adding %d to list." % i)
    # append is function that lists understand.
    # "append" 是列表的一个方法（函数)
    elements.append(i)

# now we can print them out too 打印出来看看
for i in elements:
    print("Element was: %d" % i)
