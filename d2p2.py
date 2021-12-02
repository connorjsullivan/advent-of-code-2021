import numpy as np


def movement(direction, distance, aim):
    #will return (depth change ,horizontal change) dependent
    #on direction/distance
    travelled = int(distance)
    if direction == "down":
        return (0, 0, travelled)
    elif direction == "up":
        return (0, 0, travelled * -1)
    elif direction == "forward":
        return (aim*travelled, travelled, 0)
    else:
        return (0,0)

depth = 0
horizontal = 0
aim = 0
input = 'd2_input.txt'
my_file_handle=open(input)
data = my_file_handle.read().split('\n')

format_data = [line.split() for line in data]
format_data.pop()
print(format_data)
    #formats to [distance,change]
for dir,dist in format_data:
    depth_change, horiz_change, aim_change = movement(dir,dist,aim)
    depth += depth_change 
    horizontal += horiz_change
    aim += aim_change
print((horizontal*depth))
