import numpy as np
from numpy.core.numeric import binary_repr

input = 'd3_input.txt'
my_file_handle=open(input)
data = my_file_handle.read().split('\n')

length_row = len(data[1])
i = 0
j = 0 

#data.pop()

zero_count = 0
one_count = 0
oxyg_arr = data[:] #02 
carb_arr = data[:] #c02 

# for i in range(length_row):
#     zero_arr = []
#     one_arr = []
#     zero_count = 0
#     one_count = 0
#     for j in range(len(data)):
#         if data[j][i] == '0':
#             zero_count += 1
#             zero_arr.append(j)
#         else:
#             one_count += 1
#             one_arr.append(j)
#     if zero_count >= one_count:
#         for y in len(range(oxyg_arr)):
#             if oxyg_arr[y][i] == 1:
#                 oxyg_arr[y][i] = ""
#             if carb_arr[y][i] == 0:
#                 carb_arr[y][i] = ""
#     else: 
#         for z in len(range(oxyg_arr)):
#             for z in len(range(oxyg_arr)):
#                 if oxyg_arr[z][i] == 1:
#                     oxyg_arr[z][i] = ""
#                 if carb_arr[z][i] == 0:
#                     carb_arr[z][i] = ""
#popular value to assign to o2 
#unpopular to assign to co2
one_oxyg_arr = []
zero_oxyg_arr = [] 
rem_oxyg = data[:]
for i in range(length_row):
    if len(rem_oxyg) == 1:
        break
    zero_count = 0
    one_count = 0
    one_oxyg_arr = []
    zero_oxyg_arr = [] 
    for j in range(len(rem_oxyg)):
        if rem_oxyg[j][i] == '0':
            zero_count += 1
            zero_oxyg_arr.append(rem_oxyg[j])
        else:
            one_count += 1
            one_oxyg_arr.append(rem_oxyg[j])
    if zero_count > one_count:
        one_oxyg_arr = zero_oxyg_arr
        rem_oxyg = zero_oxyg_arr
    else:
        zero_oxyg_arr = one_oxyg_arr
        rem_oxyg = one_oxyg_arr
print(rem_oxyg)

rem_carb = data[:]
for i in range(length_row):
    if len(rem_carb) == 1:
        break
    zero_count = 0
    one_count = 0
    one_carb_arr = []
    zero_carb_arr = [] 
    for j in range(len(rem_carb)):
        if rem_carb[j][i] == '0':
            zero_count += 1
            zero_carb_arr.append(rem_carb[j])
        else:
            one_count += 1
            one_carb_arr.append(rem_carb[j])
    print(rem_carb, zero_count, one_count)
    if zero_count <= one_count:
        rem_carb = zero_carb_arr
    else:
        rem_carb = one_carb_arr
print(rem_carb)
    
unbin_oxyg = int(rem_oxyg[0],2)
unbin_carb = int(rem_carb[0],2)
print(unbin_oxyg*unbin_carb)





#C02
