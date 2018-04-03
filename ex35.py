# sys.exit 用于结束程序
from sys import exit

# 进入黄金房间后的逻辑
def gold_room():
    print("This room is full of gold. How much do you take?")

    # 如果输入不包含 0 或 1 则死
    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    # 如果输入的数字大于等于 50 则死
    if how_much < 50:
        print("Nice, you're not greedy, you  win!")
        exit(0)
    else:
        dead("You greedy bastard!")

# 实现熊房间的逻辑
def bear_room():
    print("There is a bear hear.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    # 如果熊离开后直接开门就用不到 while 循环了.
    while True:
        next = input("> ")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

# 恶魔房逻辑
def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee your life or eat your head?")

    next = input("> ")
    
    # 二选一，否则恶魔放循环
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

# 惨死函数
def dead(why):
    print(why, "Good job")
    exit(0)

# 启动函数
def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_roome()
    else:
        dead("You stumble around the room until you starve.")

# 开始游戏
start()
