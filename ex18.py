# 这就和我们的脚本使用 argv 一样
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" %(arg1, arg2))

# 实际上参数 *args 是没什么意义的，我们实际可以这样写
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))

# 这个是一个参数的
def print_one(arg1):
    print("arg1: %r" % arg1)

# 这个是没有参数的
def print_none():
    print("I got nothin'.")

# 下面是调用函数的演示，
# 不去使用函数的话，它们是不会打印任何东西出来的。
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
