###############
# and 关键字
if (1+1 == 2) and ("The boy" != "Your girl friend"):
    print("你精神很正常，同时不是 Gay ：P")

print("-------------------------\n")


#############
# or 关键字
n = 5
if n<7 or n>7:
    print("n 不等于 7")

print("-------------------------\n")

#################
# not 关键字
if not 3>5:
    print("3 小于等于 5")

print("-------------------------\n")


##############
# del 关键字
l = ['a', 'b', 'c', 'd', 'e']
print(l)
# 删除指定索引的值
del l[2]
print("删除索引 2：\n", l)

# 切片删除
del l[1:3]
print("删除切片 1-3：\n", l)

# pop 会返回被抛出的值
l_pop = l.pop(-1)
print("pop -1：\n", l_pop)

# 删除变量
del l
#print(l)

print("-------------------------\n")


##################
# from 和 import 关键字
# import 引入并通过 argv 功能打印脚本的名字
import sys
# 使用时需要库的名字
print(sys.argv)

# from 配合引入，并通过 argv 打印脚本名字
from sys import argv
print(argv)

print("-------------------------\n")


############
# while 关键字
i = 0
print("开始 i + 1")
while i < 1000:
    i += 1
print("while 循环结束，i =", i)

print("\n\n\n-------------------------\n")


#############
# as 关键字
# import 重命名
import sys as my_sys
from sys import argv as ar
print(my_sys.argv)
print(ar)

print("\n\n\n-------------------------\n")



###############
# if、elif、else 关键字
def age_of_marriage(age):
    if age < 22:
        print("年龄还小，不用着急找女朋友")
    elif age == 22:
        print("现在可以合法结婚啦")
    else:
        if age < 28:
            print("差不多找个女盆友结婚吧")
        else:
            print("快快快！不然你和馆主一样啦！！！")
            
# your_age = int(input('您今年贵庚？\n> '))
# age_of_marriage(your_age)

print("\n\n\n-------------------------\n")


###############
# global 关键字
x = 6

def my_print():
    print("函数中使用全局变量 x，其值是：", x)
    
def my_print2():
    x = "局部变量"
    print("函数中更改 x 的值：", x)

def my_global():
    print("使用 global 在函数这个局部中改变全局变量 x")
    global x
    x = "全局变量"
    

print("全局中 x 的值是：", x)
my_print()
my_print2()
print("即便函数中更改了 x 的值，但现在全局中 x 的值还是：", x)
print("*********")
my_global()
print("现在，全局中 x 的值是：", x)
my_print()
my_print2()

print("\n\n\n-------------------------\n")


############
# with 关键字
# 通过 as 关键字把打开的文件命名为 f
with open("test.txt") as f:
    print(f.read())

print("\n\n\n-------------------------\n")


###############
# assert 关键字
# assert 1+1==2,"1+1 不等于 2"
# assert 1+1!=2,"1+1 等于 2"

print("\n\n\n-------------------------\n")


#############
# pass 关键字
if 1+1 > 5:
    print("宇宙要毁灭了")
else:
    # 宇宙不会毁灭，但是我们暂时还不知道会发生什么
    pass

print("\n\n\n-------------------------\n")


##############
# yield 关键字
def yield_keyword():
    for i in [1,2,3,4,5]:
        yield i

for i in yield_keyword():
    print(i)

print("\n\n\n-------------------------\n")


##################
# yield 关键字
# 构造一个生成器用格式化字符生成字母
def my_yield():
    for i in range(10):
        yield "%c" % (97 + i)    # ascii 码 97 是字母 a

# 实例化生成器
y = my_yield()

# 生成器无法打印其中内容，因为
# 未迭代时，其中不包含元素，而生成新的元素时旧元素抛弃
# 所有占用内存低
print(y)

# 迭代打印 生成器
for i in y:
    print(i)

# 再次迭代无法再次获取，只能迭代一次
print("再次迭代：")

for i in y:
    print(i)

print("迭代结束")

print("\n\n\n-------------------------\n")


#################
# break 关键字
print("break :")
for i in range(10):
    if i == 5:
        break
    print(i)

# continue 关键字
print("contiune :")
n = 11
while n > 0:
    n -= 1
    if n == 10:
         print("开始倒数！")
         continue
    print(n)

print("\n\n\n-------------------------\n")


################
# try except finally 关键字
try:
    print(name)
except NameError:
    print("变量名 name 不存在，将引发 NameError 错误")

# 可以使用 try-except-else 代码块在无错误的时候引发 else 语句。
try:
    print("没有问题吧？")
except NameError:
    print(NameError)
else:
    print("运行正常")

# 有时候我们不知道会是什么误类型的情况下，可以不指定 except 的错误类型。
try:
    print(int(name))
except:
    print("出错啦,捕获到某种错误")

# 也可以用 as 把错误信息打印出来
try:
    print(1/0)
except Exception as e:    # Exception 是错误的基类
    print("错误信息:", e)

# 可以写多行 except 获取不同的错误（前面的 except 触发后，后面的将不会再触发)
# 或者某几种错误放在一个括号中使用一个应该策略
try:
   foo()
except (NameError, TypeError) as e:
    print("发生意料之中的错误：", e)
except Exception as e:
    print("发生意料之外的错误：", e)

print("\n\n\n-------------------------\n")


###########
# exec 和 eval 内置函数
a = "print(1+1)"
exec(a)
eval(a)

print("\n\n\n-------------------------\n")


###########
# raise 关键字
#raise NameError("哈哈，名字错啦")

print("\n\n\n-------------------------\n")


#############
# is 关键字
a = 2
b = a
if a is b:
    print("a 和 b 是同一个引用对象")
else:
    print("a 和 b 是不同的引用对象")

print("\n\n\n-------------------------\n")


##############
# return 关键字
def my_add(number):
    for i in range(10):
        number = number + i
    return(number)
print("运行函数 my_add(3)")
my_add(3)
print("打印函数 my_add(5)")
print(my_add(5))

print("\n\n\n-------------------------\n")


#############
# lambda 关键字
x = 10
f = lambda x:x*3
x = f(x)
print(x)

# 相当于
x = 10
def x3(x):
    x *= 3
    return x

x = x3(10)
print(x)

print("lambda 表达式可以简洁的生成一个函数")

print("\n\n\n-------------------------\n")
