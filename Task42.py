#retive non zero element from array

from numpy import *

data = array([2,3,5,0,5,0,3,0,3,0,5])
a = nonzero(data)

print(a)  #return only index values
print(data[a])