# a python program to copy an array as another array

from numpy import *

arr1= arange(1,20)
arr2= arr1.copy()

print("original array: ",arr1)
arr2[1]=500
print("modified 2nd array:",arr2)