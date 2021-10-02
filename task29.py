#crate one array from another array
from array import *
arr1 = array("i",[3,4,7,5,3,5])
print("Original Array: ",arr1)
arr2 = array(arr1.typecode,[ x*5 for x in arr1])
print(arr2)