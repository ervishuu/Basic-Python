#A python program to sort the array element using bubble sort technique
from array import *
data = array("i",[])

n = int(input("enter the how many element do you want to store: "))
for i in range(n):
    m = int(input("Enter the element: "))
    data.append(m)

print("before sorting data: ",data)
flag = False
for i in range(n-1):
    for j in range(n-1-i):
        if data[j] > data[j+1]:
            temp = data[j]
            data[j] = data[j+1]
            data[j+1] = temp
            flag = True

        if flag == False:
            break
        else:
            flag = False
print("After sorting data: ",data)

