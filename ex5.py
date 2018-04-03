name = 'Zed A. Shaw'
age = 35
height = 74 # 英寸
weight = 180 # 磅
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print("let's talk about %s." % name)
print("He's %d inches tall." % height)
print("He's %d pounds heavy." % weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (eyes, hair))
print("His teeth are usually %s depending on the coffee." % teeth)
# 下面这行复杂一点
print("If i add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight
))

# 打印两个空行
print("\n" * 2)

# 试用 %r 格式化字符
print("这里尝试使用新的格式化字符占位符，看看效果: %r" % "放个字符串")
print("在试试放个数字：%r" % 666)
print("这次是数字字符串：%r" % '2333')

# 打印两个空行
print("\n" * 2)

# 单位换算
print("Zed A. Shaw 高 %.2f 厘米" % (height * 2.54))
print("Zed A. Shaw 重 %.2f 千克" % (weight * 0.45))
