#a python program to accept two matrix and find their product
import sys
from numpy import *

r1,  c1 =[ int(a) for a in input("Enter row and column for 1st matrix: ").split()]
r2 , c2 = [ int(a) for a in input("Enter row and column for 2st matrix: ").split()]

if c1 != r2:
    print("Multification is not possible: ")

data1 = input("Enter the element for 1st matrix: ")
data2 =  input("Enter the element for the 2nd matrix: ")

x1 = reshape(matrix(data1),(r1,c1))
x2 = reshape(matrix(data2),(r2,c2))

x3 = x1 * x2
print("product of two matrix is: ")
print(x3)