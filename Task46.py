# A python program to accept a matrix form keyboard and display its transpose matrix

from numpy import *

r,c = [int(a) for a in input("Enter the rows and columns: ").split()]

data = input("Enter the element: ")

x = reshape(matrix(data),(r,c))
print("original matrix is ")
print(x)

# transpose of the matrix is
x2 =  x.transpose()
print("transpose of the x is ")
print(x2)