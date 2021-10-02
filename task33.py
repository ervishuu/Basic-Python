# understand various method of array class
from array import *
data = array("i",(1,2,3,4,5,6,7,8,9))
print("original array:",data)
#append
data.append(45)
print("append 45: ",data)

#insert
data.insert(2,444)
print("Insert 44 at 3 position: ",data)

#remove
data.remove(2)
print("remove 2 :",data)

#remove the last element
data.pop()
print("remove last element: ",data)

#find the position of index
m = data.index(5)
print("return index of 5: ",m)

#convert array to list
data1 = data.tolist()
print(type(data))
print(type(data1))