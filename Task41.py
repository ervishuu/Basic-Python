# a python program to comapre two array and retrive those element which is grater
from numpy import *
arr1 = array([11,22,33,4,66,7,554,44,6])
arr2 = array([34,65,65,33,66,88,54,22,45])

arr3 = where(arr1 > arr2 , arr1,arr2)
print(arr3)