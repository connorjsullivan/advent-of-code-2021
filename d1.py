import numpy as np

print("Started code")
input = 'd1p1_input.txt'
data = np.loadtxt(input, delimiter='\n')


# print(len(data))
total_deeper = 0
last_depth = data[0]
# print(last_depth)
# print(data[0])
for depth in data:
    if depth > last_depth:
        total_deeper += 1
    last_depth = depth    
print(total_deeper)



