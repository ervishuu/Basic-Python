# a python program to retrive element from a matrix and display them
from numpy import *
mat = [[1,2,3],[4,5,6],[7,8,9]]
print("Dispplay the list",mat)
print("----------------------------------------------------------------------")
# matrix = matrix(mat)
# print(matrix)
for i in mat:
    for j in i:
        print(j,end=" ")
    print()

print("----------------------")
for i in range(len(mat)):
    for j in range(len(mat[i])):
        print(mat[i][j],end=" ")
    print()