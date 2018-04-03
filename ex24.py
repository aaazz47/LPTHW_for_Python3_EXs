# 开场问候一下
print("Let's practice everything.")

# 转义字符练习，这里还有一个英文口语知识点啊 -_-||| 'bout == about
print('You\'d need to know \'bout escapes with \\ that do \nnewlines and \t tabs.')

# 有不熟悉的知识点么？
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("---------------")
print(poem)
# 私货，分割线我喜欢这么用
print("-" * 15)

# 变量
five = 10 - 2 + 3 - 6
# 格式化字符
print("This should be five: %s" % five)

# 函数来了,还悄悄高速我们如何 return 多个值
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# 函数调用和解包
start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: %d" % start_point)
print("We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates))

# 使用变量进行运算，改变变量的值，然后...
start_point = start_point / 10
print("We can also do that this way:")

# 更厉害了，直接在格式化字符的时候使用调用函数并把返回的值解包个格式化字符
print("We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point))
