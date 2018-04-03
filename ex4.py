# 表示汽车数量的变量
cars = 100
# 表示车内空间的变量
space_in_a_car = 4.0
# 表示司机数量的变量
drivers = 30
# 表示乘客数量的变量
passengers = 90
# 变量表示无法行驶车辆数量的变量
cars_not_driven = cars - drivers
# 表示可以行驶车辆数量的变量
cars_driven = drivers
# 表示最大拼车容量的变量
carpool_capacity = cars_driven * space_in_a_car
# 表示平均每辆车中乘客数量的变量
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool tody.")
print("We need to put about", average_passengers_per_car, "in each car.")
