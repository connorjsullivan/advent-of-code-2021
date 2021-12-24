import numpy as np
import copy
input = 'd5_input.txt'
input_read = open(input)
input_split = input_read.read().split('\n')
input_noarrow = []
input_coordpairs = []
input_coordints = []
int_coords = []
for input_row in input_split:
    input_noarrow.append(input_row.split(' -> '))
for coord_pair in input_noarrow:
    for inner_pair in coord_pair:
        print(inner_pair)
        input_coordpairs.append(inner_pair.split(','))

for coord_pair in input_coordpairs:
    for inner_pair in coord_pair:
        input_coordints.append(int(inner_pair))
for i in range(0,len(input_coordints),4):
    int_coords.append([input_coordints[i],input_coordints[i+1],input_coordints[i+2],input_coordints[i+3]])
print(int_coords)
#int_array_picks = list(map(int, array_picks))


def slope(four_val_array):
    slope_array = []
    for values in four_val_array:
        (a,b,c,d) = values

        if a == c:
            diff = abs(d - b)
            min_db = min(d,b)
            for i in range(diff+1):
                slope_array.append([a,min_db+i])
        if b == d:
            diff = abs(c -a)
            min_ca = min(c,a)
            for i in range(diff+1):
                slope_array.append([min_ca+i,b]) 

           
    return slope_array

def make_map(all_array_values):
    max_x_array = []
    max_y_array = []
    max_x = int
    max_y = int
    for values in all_array_values:
        (a,b,c,d) = values
        max_x_array.append(a)
        max_x_array.append(c)
        max_y_array.append(b)
        max_y_array.append(d)

    max_x = np.max(max_x_array)
    max_y = np.max(max_y_array)
    base_map = np.zeros((max_x+1,max_y+1), dtype='int')
    return base_map

def map_change(slope_array,map):
    new_map = copy.deepcopy(map)

    for (x_coord,y_coord) in slope_array:
         new_map[y_coord,x_coord] += 1

    return new_map


#make map
int_map = make_map(int_coords)
print(int_map)
#get all slopes
int_slopes = slope(int_coords)
print(int_slopes)
#update map with slopes
updated_map = map_change(int_slopes,int_map)
print(updated_map)


##############
#Results Calc#
total_danger = 0
for row in updated_map:
    for value in row:
        if value >= 2:
            total_danger += 1

print(total_danger)