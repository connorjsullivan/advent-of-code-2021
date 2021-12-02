import numpy as np


def movement(direction, distance):
    #will return (depth change ,horizontal change) dependent
    #on direction/distance
    travelled = int(distance)
    if direction == "down":
        return (travelled * 1, 0)
    elif direction == "up":
        return (travelled * -1, 0)
    elif direction == "forward":
        return (0, travelled)
    else:
        return (0,0)

depth = 0
horizontal = 0
input = 'd2_input.txt'
my_file_handle=open(input)
data = my_file_handle.read().split('\n')

format_data = [line.split() for line in data]
format_data.pop()
print(format_data)
    #formats to [distance,change]
for dir,dist in format_data:
    depth_change, horiz_change = movement(dir,dist)
    depth += depth_change 
    horizontal += horiz_change
print((horizontal*depth))
