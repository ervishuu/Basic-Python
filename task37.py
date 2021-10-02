# search the position of element using index method

from array import *

data = array("i",[])


n = int(input("How many element do you want to store: "))
for i in range(n):
    m = int(input("Enter the element: "))
    data.append(m)

print(data)

element = int(input("Which element do you want to search: "))

try:
    loc = data.index(element)
    print("Element {} found at location {}".format(element,loc+1))
except:
    print("element not found")