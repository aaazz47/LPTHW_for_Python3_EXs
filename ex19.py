# 定义我们的函数，我们给参数起了名字，
# 不过我们将在后面的调用时看到，这个名字和
# 引入参数时给引入的变量名没关系
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# 直接为函数传入参数
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# 以变量方式将参数传入函数。
print("OR, we can use variables from our script:")
amount_of_cheese =10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# 函数的参数可以进行运算
# 实际上是运算后传入函数的。
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# 变量进行运算后作为函数的参数
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100,
amount_of_crackers + 1000)
