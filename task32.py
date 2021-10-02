#python program that helps to know the effects of slicing operations on an array
from array import *

data = array("i",(3,5,5,7,4,3,8,4,8,5,8,1,4,3,6,7,8))
print(data[0])
print(data[1])
print(data[0:2])
print(data[5:])
print(data[:3])
print(data[-1])
print(data[4:-2])
print(data[-4:])
print(data[-4:-2])