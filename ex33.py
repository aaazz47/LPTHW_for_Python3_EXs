# i = 0
# numbers = []

# while i < 6:
#     print("At the top i is %d" % i)
#     numbers.append(i)
#     i = i + 1
#     print("Numbers now: ", numbers)
#     print("At the bottom i is %d" % i)

# print("The numbers:")

# for num in numbers:
#     print(num)



# def my_while(loops, step):
#     i = 0
#     numbers = []
#     while i < loops:
#         print("At the top i is %d" % i)
#         numbers.append(i)
#         i += step
#         print("Numbers now:", numbers)
#         print("At the bottom i is %d" % i)
#         print("\n---------------")

#         print("The numbers:")
#         for num in numbers:
#             print(num)


# my_while(7,2)


numbers = []

for i in range(6):
    print("At the top i is %d" % i)
    numbers.append(i)
    print("Numbers now:", numbers)
    print("At the bottom i is %d" % i)
    print("\n---------------")

print("The numbers:")

for num in numbers:
    print(num)
