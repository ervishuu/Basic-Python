# search element from sequential
from array import *
data = array("i",[])

n = int(input("How many element do you want to store: "))
for i in range(n):
    m = int(input("Enter the element: "))
    data.append(m)

print(data)
search = int(input("Which element do you want to search: "))

flage = False
for i in range(len(data)):
    if search == data[i]:
        print("element {} found at location {}".format(search,i+1))
        flage =True

if flage == False:
    print("Element not found")
