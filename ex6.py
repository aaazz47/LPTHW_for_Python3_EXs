# 在变量中使用格式化字符
x = "There are %d types of people." % 10
# 在变量中使用格式化字符，并且格式化其他变量
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary, do_not)  # 第一、二处 迭代字符串

print(x)
print(y)

# 利用 %r 格式化格式化字符显示原始字符的引号
# 打印字符串和格式化的变量
print("I said: %r." % x)    # 三处
print("I also said: '%s'." % y)    #四处

# 这里格式化了一个布尔型变量 False
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)

# 下面演示了字符串的拼接打印
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
