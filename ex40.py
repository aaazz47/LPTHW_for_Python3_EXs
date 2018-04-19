# 创建了一个包含多个城市名称的字典
cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

# 为 cities 增加两个新的城市。
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# 创建一个函数，从字典中通过简写获得城市名称
def find_city(themap, state):    # map 是内置函数 所以使用了 themap
    if state in themap:
        return themap[state]
    else:
        return "Not found."

# ok pay attetion!
cities['_find'] = find_city

# 原文中 
#    print "State? (ENTER to quit)", 
#    state = raw_input("> ")
#
# 这种写法 python 3 似乎做不到了，参考打印的结果改下成了下面的写法
while True:
    state = input("State? (ENTER to quit) > ")
    if not state: break

    # this line is the most important ever! study!
    # 据说搞不懂的可以看看下一题
    city_found = cities['_find'](cities, state)
    print(city_found)



# 4.3 加分练习
d = {'1': 'a', '2': 'b', '3': 'c', '4':'d'}

# 使用 for 循环遍历字典
for k in d:
    print("当前的键是 %r, 它的值是：%r" % (k, d.get(k)))


for k, v in d.items():
    print(k, v)
