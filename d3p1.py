
import numpy as np
from numpy.core.numeric import binary_repr
input = 'd3_input.txt'
my_file_handle=open(input)
data = my_file_handle.read().split('\n')

length_row = len(data[1])
i = 0
j = 0 
store_popular = [] #gamma
store_unpopular =[] #epsilon

data.pop()

for i in range(length_row):
    zero_count = 0
    one_count = 0
    for j in range(len(data)):
        if data[j][i] == '0':
            zero_count += 1
        else:
            one_count += 1
    if zero_count > one_count:
        store_popular.append('0')
        store_unpopular.append('1')
    else:
        store_popular.append('1')
        store_unpopular.append('0')


string_pop = "".join(store_popular)
string_unpop = "".join(store_unpopular)

print(string_pop)
print(string_unpop)


unbinary_pop = int(string_pop,2) #converts the binary to int
unbinary_unpop = int(string_unpop,2)
print ((unbinary_pop * unbinary_unpop))
