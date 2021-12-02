import numpy as np

input = 'd1p1_input.txt'
data = np.loadtxt(input, delimiter='\n')

moving_data = []
for i in range(len(data)):
    if (i+2) >= len(data):
        print(i)
        print(len(data))
        break
    #Instruction is to stop when there is not enough 
    #measurements for 3 measurement sum
    moving_data.append(data[i] + data[i+1] + data[i+2])


# print(len(data))
total_deeper = 0
last_depth = moving_data[0]
# print(last_depth)
# print(data[0])
for depth in moving_data:
    if depth > last_depth:
        total_deeper += 1
    last_depth = depth    
print(total_deeper)