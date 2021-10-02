# a python program to retrive the element from 2D element
from numpy import *

data = array([[[1,2,3],[4,5,6]],
        [[7,8,9],[10,11,12]]
        ])
# print(data)
# print(type(data))
# print(data.ndim)

for i in range(len(data)):
    for j in range(len(data[i])):
        for k in range(len(data[i][j])):
            print(data[i][j][k],end="\t")
        print()
    print()