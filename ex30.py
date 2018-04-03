people = 30
cars = 30
buses = 30

# 比较 cars 和 people 的大小，根据情况打印不同的语句。
if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We shoule not take the cars.")
else:
    print("We can't decide.")

# 这次是比较 buses 和 cars
if buses > cars:
    print("That's too many buses.")
elif buses < cars:
    print("Maybe we could take the buses.")
else:
    print("We still can't decide.")

# 判断 people 和 buses 的大小。并打印相应的内容
if people > buses:
    print("Alright, let's just take the buses.")
else:
    print("Fine, let's stay home then.")
