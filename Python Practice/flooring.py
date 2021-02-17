'''
FlOORING CALCULATOR
a Python program that accepts at least three values as input, performs some
computation and displays at least two values as the result. The program must
include an if statement that performs different computations based on the value
of one of the inputs. Include comments in your program that describe what the
program does.
'''

import math

tile_size = input("Please choose a floor type - laminate or ceramic: ")

if (tile_size == "laminate"):
    size = 0.25
    cost = 1.78
elif(tile_size == "ceramic"):
    size = 0.5625
    cost = 1.19
else:
    print("That is an incorrect flooring type")


room_w = eval(input("Please enter the width of the room (ft): "))
room_l = eval(input("Please enter the length of the room (ft): "))

floor = float(room_w * room_l)

total = round(float(floor/size), 2)

f_cost = round(cost * total, 2)

print("You will need: ", math.ceil(total), "tiles of ", tile_size)
print (total)
print("It will cost $", f_cost)
