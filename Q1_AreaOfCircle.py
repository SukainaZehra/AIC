#taking radius for user and calculating area of circle
num = int(input("enter radius: "))
area_1 = (22/7)*(num*num) #version 1
area_2 = (22/7)*(num**2) #version 2
import math #version 3
area_3 = (22/7)*(int(math.pow(num, 2)))
print("Area of Circle ver 1 = ", area_1)
print("Area of Circle ver 2 = ", area_2)
print("Area of Circle ver 3 = ", area_3)