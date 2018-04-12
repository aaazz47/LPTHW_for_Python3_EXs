ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there's not 10 things in that list, let's fix that.")

# 字符串的 split 方法会把字符串按照参数隔开生成一个列表
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# 不断从 more_stuff 中取出元素加入 stuff 中直到
# stuff 的长度等于10，确认 while 循环会正确结束
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding:", next_one)
    stuff.append(next_one)
    print("There's %d items now." % len(stuff))

print("There we go:", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
