# A python program to retrive the element from 2D array and display them using for loop

from numpy import *
data = [[1,2,3],[4,5,6],[7,8,9]]
#
# for i in range(len(data)):
#     print(data[i])

for i in range(len(data)):
    for j in range(len(data)):
        print(data[i][j],end=" ")
